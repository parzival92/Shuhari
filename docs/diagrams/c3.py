#!/usr/bin/env python3
from pathlib import Path

WIDTH = 1800
HEIGHT = 1100
SVG_PATH = Path(__file__).with_suffix('.svg')


def esc(text: str) -> str:
    return (text.replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;'))


def box(svg, x, y, w, h, label, fill="#f5f5f5"):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" ry="10" fill="{fill}" stroke="#333" />')
    lines = label.split('\n')
    line_height = 14
    total_h = line_height * len(lines)
    start_y = y + (h - total_h) / 2 + line_height - 3
    for i, line in enumerate(lines):
        text_y = start_y + i * line_height
        svg.append(f'<text x="{x + w/2}" y="{text_y}" font-family="Arial" font-size="12" text-anchor="middle" fill="#111">{esc(line)}</text>')


def boundary(svg, x, y, w, h, label):
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#777" stroke-dasharray="6,4" />')
    svg.append(f'<text x="{x + 10}" y="{y + 16}" font-family="Arial" font-size="12" fill="#555">{esc(label)}</text>')


def arrow(svg, x1, y1, x2, y2):
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)" />')


def main():
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        '<defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#333" /></marker></defs>',
        f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="white" />'
    ]

    # Component boundary
    boundary(svg, 200, 80, 900, 740, "Backend API Container (Microservices)")

    # Components
    box(svg, 240, 140, 220, 70, "API Controllers", fill="#e8f4ff")
    box(svg, 240, 230, 220, 70, "Auth/RBAC", fill="#e8f4ff")
    box(svg, 240, 320, 220, 70, "Assessment Service", fill="#e8f4ff")
    box(svg, 240, 410, 220, 70, "Plan Service", fill="#e8f4ff")
    box(svg, 240, 500, 220, 70, "Training Service", fill="#e8f4ff")
    box(svg, 240, 590, 220, 70, "Evaluation Service", fill="#e8f4ff")

    box(svg, 520, 230, 220, 70, "Hint Bot Component", fill="#fff3e6")
    box(svg, 520, 320, 220, 70, "File/Artifact Service", fill="#fff3e6")
    box(svg, 520, 410, 220, 70, "Event Publisher", fill="#fff3e6")
    box(svg, 520, 500, 220, 70, "Audit Logger", fill="#fff3e6")
    box(svg, 520, 590, 220, 70, "Data Access Layer", fill="#fff3e6")

    # External dependencies
    box(svg, 1160, 180, 200, 70, "Postgres", fill="#e8f4ff")
    box(svg, 1160, 270, 200, 70, "Redis", fill="#e8f4ff")
    box(svg, 1160, 360, 200, 70, "Object Storage", fill="#e8f4ff")
    box(svg, 1160, 450, 200, 70, "LLM Gateway", fill="#fff3e6")
    box(svg, 1160, 540, 200, 70, "Orchestrator", fill="#fff3e6")

    # Arrows inside container
    arrow(svg, 460, 175, 520, 265)  # Controllers to Hint Bot
    arrow(svg, 460, 175, 520, 625)  # Controllers to Data Access
    arrow(svg, 460, 265, 520, 625)  # Auth to DAL
    arrow(svg, 460, 355, 520, 625)  # Assessment to DAL
    arrow(svg, 460, 445, 520, 625)  # Plan to DAL
    arrow(svg, 460, 535, 520, 625)  # Training to DAL
    arrow(svg, 460, 625, 520, 625)  # Evaluation to DAL

    arrow(svg, 740, 265, 1160, 485)  # Hint Bot to LLM Gateway
    arrow(svg, 740, 355, 1160, 395)  # File Service to Object Storage
    arrow(svg, 740, 445, 1160, 575)  # Event Publisher to Orchestrator
    arrow(svg, 740, 625, 1160, 215)  # DAL to Postgres
    arrow(svg, 740, 625, 1160, 305)  # DAL to Redis

    svg.append('</svg>')
    SVG_PATH.write_text("\n".join(svg))
    print(f"Wrote {SVG_PATH}")


if __name__ == "__main__":
    main()
