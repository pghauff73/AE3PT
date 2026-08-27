#!/usr/bin/env python3
"""Build the static AE3PT documentation data bundle from docs/**/*.md."""

from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from urllib.parse import quote, urlsplit, urlunsplit


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
HTML_HEADING_RE = re.compile(r"<h([1-6])>(.*?)</h\1>", re.DOTALL)
URL_ATTR_RE = re.compile(r'\b(href|src)="([^"]+)"')
TAG_RE = re.compile(r"<[^>]+>")
INLINE_MATH_RE = re.compile(r"\\\((.+?)\\\)")


MathNode = tuple[str, str]


class LatexMathParser:
    """Convert the small LaTeX subset used by the teaching documents to MathML."""

    COMMANDS: dict[str, MathNode] = {
        "approx": ('<mo>≈</mo>', "approximately"),
        "Delta": ('<mi>Δ</mi>', "delta"),
        "Omega": ('<mi mathvariant="normal">Ω</mi>', "ohms"),
        "pm": ('<mo>±</mo>', "plus or minus"),
        "rho": ('<mi>ρ</mi>', "rho"),
        "theta": ('<mi>θ</mi>', "theta"),
        "times": ('<mo>×</mo>', "times"),
    }
    OPERATORS = {
        "+": "plus",
        "-": "minus",
        "=": "equals",
        "/": "divided by",
        "×": "times",
    }

    def __init__(self, expression: str):
        self.expression = expression.strip()
        self.position = 0

    def parse(self) -> MathNode:
        nodes = self._parse_sequence()
        if self.position != len(self.expression):
            raise ValueError(f"unexpected mathematical input near {self.expression[self.position:]!r}")
        markup = "".join(node[0] for node in nodes)
        spoken = " ".join(node[1] for node in nodes if node[1]).strip()
        return f"<mrow>{markup}</mrow>", re.sub(r"\s+", " ", spoken)

    def _parse_sequence(self, stop_character: str | None = None) -> list[MathNode]:
        nodes: list[MathNode] = []
        while self.position < len(self.expression):
            character = self.expression[self.position]
            if stop_character and character == stop_character:
                self.position += 1
                return nodes
            if character.isspace():
                self.position += 1
                continue
            if character in "_^":
                if not nodes:
                    raise ValueError(f"script marker {character!r} has no base")
                self.position += 1
                script = self._parse_script()
                base = nodes.pop()
                if character == "_":
                    nodes.append(
                        (
                            f"<msub>{base[0]}{script[0]}</msub>",
                            f"{base[1]} subscript {script[1]}",
                        )
                    )
                else:
                    power_words = "squared" if script[1] == "2" else f"to the power of {script[1]}"
                    nodes.append((f"<msup>{base[0]}{script[0]}</msup>", f"{base[1]} {power_words}"))
                continue
            nodes.append(self._parse_primary())
        if stop_character:
            raise ValueError(f"missing closing {stop_character!r} in mathematical expression")
        return nodes

    def _parse_script(self) -> MathNode:
        if self.position >= len(self.expression):
            raise ValueError("missing subscript or superscript value")
        if self.expression[self.position] == "{":
            return self._parse_group()
        return self._parse_primary()

    def _parse_group(self) -> MathNode:
        if self.expression[self.position] != "{":
            raise ValueError("mathematical group must start with '{'")
        self.position += 1
        nodes = self._parse_sequence("}")
        markup = "".join(node[0] for node in nodes)
        spoken = " ".join(node[1] for node in nodes if node[1]).strip()
        return f"<mrow>{markup}</mrow>", spoken

    def _parse_primary(self) -> MathNode:
        character = self.expression[self.position]
        if character == "{":
            return self._parse_group()
        if character == "\\":
            return self._parse_command()
        if character in self.OPERATORS:
            self.position += 1
            return f"<mo>{html.escape(character)}</mo>", self.OPERATORS[character]
        if character.isdigit() or (character == "." and self._next_character_is_digit()):
            return self._parse_number()
        if character.isalpha():
            return self._parse_identifier()
        self.position += 1
        return f"<mo>{html.escape(character)}</mo>", character

    def _parse_command(self) -> MathNode:
        self.position += 1
        if self.position >= len(self.expression):
            raise ValueError("trailing backslash in mathematical expression")
        if self.expression[self.position].isspace():
            self.position += 1
            return '<mspace width="0.35em"/>', ""
        start = self.position
        while self.position < len(self.expression) and self.expression[self.position].isalpha():
            self.position += 1
        command = self.expression[start:self.position]
        if command == "frac":
            numerator = self._parse_required_group("fraction numerator")
            denominator = self._parse_required_group("fraction denominator")
            return (
                f"<mfrac>{numerator[0]}{denominator[0]}</mfrac>",
                f"{numerator[1]} divided by {denominator[1]}",
            )
        if command in self.COMMANDS:
            return self.COMMANDS[command]
        if not command:
            escaped = html.escape(self.expression[self.position])
            self.position += 1
            return f"<mo>{escaped}</mo>", escaped
        return f"<mtext>{html.escape(command)}</mtext>", command

    def _parse_required_group(self, description: str) -> MathNode:
        while self.position < len(self.expression) and self.expression[self.position].isspace():
            self.position += 1
        if self.position >= len(self.expression) or self.expression[self.position] != "{":
            raise ValueError(f"missing {description}")
        return self._parse_group()

    def _parse_number(self) -> MathNode:
        start = self.position
        while self.position < len(self.expression) and (
            self.expression[self.position].isdigit() or self.expression[self.position] == "."
        ):
            self.position += 1
        number = self.expression[start:self.position]
        return f"<mn>{html.escape(number)}</mn>", number

    def _parse_identifier(self) -> MathNode:
        character = self.expression[self.position]
        if character.isupper():
            self.position += 1
            return f"<mi>{character}</mi>", character
        start = self.position
        while self.position < len(self.expression) and self.expression[self.position].islower():
            self.position += 1
        identifier = self.expression[start:self.position]
        if len(identifier) == 1:
            return f"<mi>{identifier}</mi>", identifier
        return f"<mtext>{html.escape(identifier)}</mtext>", identifier

    def _next_character_is_digit(self) -> bool:
        return self.position + 1 < len(self.expression) and self.expression[self.position + 1].isdigit()


def mathml_from_latex(expression: str, display: bool) -> str:
    markup, spoken = LatexMathParser(expression).parse()
    display_value = "block" if display else "inline"
    class_name = "math-equation" if display else "math-inline"
    math = (
        f'<math xmlns="http://www.w3.org/1998/Math/MathML" display="{display_value}" '
        f'class="{class_name}" aria-label="{html.escape(spoken, quote=True)}">{markup}</math>'
    )
    return f'<div class="math-display">{math}</div>' if display else math


def render_mathematics(markdown_text: str) -> str:
    """Replace display and inline LaTeX delimiters outside code fences with MathML."""

    lines = markdown_text.splitlines()
    output: list[str] = []
    in_fence = False
    fence_marker = ""
    line_index = 0

    while line_index < len(lines):
        line = lines[line_index]
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
            output.append(line)
            line_index += 1
            continue

        if not in_fence and line.strip() == "$$":
            expression_lines: list[str] = []
            line_index += 1
            while line_index < len(lines) and lines[line_index].strip() != "$$":
                expression_lines.append(lines[line_index].strip())
                line_index += 1
            if line_index >= len(lines):
                raise ValueError("unclosed display-math delimiter")
            expression = " ".join(part for part in expression_lines if part).strip()
            if not expression:
                raise ValueError("empty display-math expression")
            output.append(mathml_from_latex(expression, display=True))
            line_index += 1
            continue

        if not in_fence:
            line = INLINE_MATH_RE.sub(lambda match: mathml_from_latex(match.group(1), display=False), line)
        output.append(line)
        line_index += 1

    return "\n".join(output) + ("\n" if markdown_text.endswith("\n") else "")


def clean_inline_markdown(value: str) -> str:
    value = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", value)
    value = re.sub(r"[`*_~]", "", value)
    return html.unescape(value).strip()


def slugify(value: str, seen: dict[str, int]) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    normalized = "".join(character for character in normalized if not unicodedata.combining(character))
    normalized = normalized.lower().replace("—", "-").replace("–", "-")
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized).strip("-") or "section"
    seen[normalized] = seen.get(normalized, 0) + 1
    return normalized if seen[normalized] == 1 else f"{normalized}-{seen[normalized]}"


def extract_headings(markdown_text: str) -> list[dict[str, object]]:
    headings: list[dict[str, object]] = []
    seen: dict[str, int] = {}
    in_fence = False
    fence_marker = ""

    for raw_line in markdown_text.splitlines():
        stripped = raw_line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(raw_line)
        if not match:
            continue
        text = clean_inline_markdown(match.group(2))
        headings.append({"level": len(match.group(1)), "text": text, "id": slugify(text, seen)})

    return headings


def render_markdown(markdown_text: str, markdown_executable: str) -> str:
    process = subprocess.run(
        [markdown_executable, "-G"],
        input=markdown_text,
        text=True,
        capture_output=True,
        check=False,
    )
    if process.returncode != 0:
        raise RuntimeError(process.stderr.strip() or "Markdown renderer failed")
    return process.stdout


def inject_heading_ids(rendered_html: str, headings: list[dict[str, object]]) -> str:
    heading_iterator = iter(headings)

    def replace(match: re.Match[str]) -> str:
        heading = next(heading_iterator, None)
        if heading is None:
            return match.group(0)
        return (
            f'<h{match.group(1)} id="{heading["id"]}" data-heading-level="{heading["level"]}">'
            f"{match.group(2)}</h{match.group(1)}>"
        )

    return HTML_HEADING_RE.sub(replace, rendered_html)


def normalize_relative_path(source_path: str, target: str) -> str:
    source_parent = PurePosixPath(source_path).parent
    return posixpath.normpath(str(source_parent / target))


def rewrite_urls(rendered_html: str, source_path: str, document_paths: set[str]) -> str:
    def replace(match: re.Match[str]) -> str:
        attribute, raw_url = match.groups()
        if raw_url.startswith(("#", "/", "//", "data:", "mailto:", "tel:")):
            return match.group(0)

        split = urlsplit(raw_url)
        if split.scheme:
            return match.group(0)

        normalized = normalize_relative_path(source_path, split.path)
        if attribute == "href" and normalized in document_paths:
            route = f"#doc={quote(normalized, safe='')}"
            if split.fragment:
                route += f"&section={quote(split.fragment, safe='')}"
            return f'href="{route}" data-doc-link="{html.escape(normalized)}"'

        rewritten = urlunsplit(("", "", normalized, split.query, split.fragment))
        return f'{attribute}="{html.escape(rewritten, quote=True)}"'

    return URL_ATTR_RE.sub(replace, rendered_html)


def html_to_text(rendered_html: str) -> str:
    text = TAG_RE.sub(" ", rendered_html)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def build_document(path: Path, docs_root: Path, markdown_executable: str, document_paths: set[str]) -> dict[str, object]:
    relative_path = path.relative_to(docs_root).as_posix()
    markdown_text = path.read_text(encoding="utf-8")
    headings = extract_headings(markdown_text)
    rendered_html = render_markdown(render_mathematics(markdown_text), markdown_executable)
    rendered_html = inject_heading_ids(rendered_html, headings)
    rendered_html = rewrite_urls(rendered_html, relative_path, document_paths)
    text = html_to_text(rendered_html)
    title = next((str(item["text"]) for item in headings if item["level"] == 1), path.stem.replace("-", " ").title())
    paragraph_match = re.search(r"<p>(.*?)</p>", rendered_html, re.DOTALL)
    summary_text = html_to_text(paragraph_match.group(1)) if paragraph_match else text
    summary = summary_text[:240].rsplit(" ", 1)[0] + ("…" if len(summary_text) > 240 else "")

    return {
        "path": relative_path,
        "title": title,
        "summary": summary,
        "wordCount": len(text.split()),
        "headings": headings,
        "html": rendered_html,
        "text": text,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=None)
    arguments = parser.parse_args()

    project_root = arguments.project_root.resolve()
    docs_root = project_root / "docs"
    output_path = arguments.output or docs_root / "assets" / "document-data.js"
    markdown_executable = shutil.which("markdown")

    if markdown_executable is None:
        print("error: the 'markdown' executable is required to build the documentation site", file=sys.stderr)
        return 2
    if not docs_root.is_dir():
        print(f"error: documentation directory does not exist: {docs_root}", file=sys.stderr)
        return 2

    markdown_paths = sorted(
        path for path in docs_root.rglob("*.md") if not any(part.startswith(".") for part in path.relative_to(docs_root).parts)
    )
    document_paths = {path.relative_to(docs_root).as_posix() for path in markdown_paths}
    documents = [build_document(path, docs_root, markdown_executable, document_paths) for path in markdown_paths]
    payload = {
        "version": 1,
        "documentCount": len(documents),
        "documents": documents,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    serialized = serialized.replace("</script", "<\\/script").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    output_path.write_text(f"window.AE3PT_DOCS={serialized};\n", encoding="utf-8")
    print(f"generated {output_path.relative_to(project_root)} from {len(documents)} Markdown document(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
