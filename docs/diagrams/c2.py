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

    # Users
    box(svg, 60, 120, 180, 70, "Trainee", fill="#eef7ff")
    box(svg, 60, 220, 180, 70, "Trainer", fill="#eef7ff")

    # System boundary
    boundary(svg, 300, 60, 960, 780, "CKA Mentor AI Platform")

    # Containers inside system
    box(svg, 340, 120, 220, 70, "Web UI\n(Next.js)", fill="#e8f4ff")
    box(svg, 340, 230, 220, 70, "Backend API\n(Microservices)", fill="#e8f4ff")
    box(svg, 340, 340, 220, 70, "LLM Gateway", fill="#fff3e6")
    box(svg, 340, 450, 220, 70, "Orchestrator\n& Workers", fill="#fff3e6")
    box(svg, 340, 560, 220, 70, "Sandbox Runner", fill="#fff3e6")

    box(svg, 640, 200, 220, 70, "Postgres", fill="#e8f4ff")
    box(svg, 640, 300, 220, 70, "Redis", fill="#e8f4ff")
    box(svg, 640, 400, 220, 70, "Object Storage", fill="#e8f4ff")

    # External systems
    box(svg, 980, 120, 220, 70, "LLM Providers", fill="#fff3e6")
    box(svg, 980, 220, 220, 70, "Notification Service", fill="#fff3e6")
    box(svg, 980, 320, 220, 70, "Identity Provider", fill="#fff3e6")

    # Arrows
    arrow(svg, 240, 155, 340, 155)  # Trainee to Web UI
    arrow(svg, 240, 255, 340, 155)  # Trainer to Web UI

    arrow(svg, 560, 155, 340 + 220, 265)  # Web UI to Backend API
    arrow(svg, 560, 265, 640, 235)  # API to Postgres
    arrow(svg, 560, 265, 640, 335)  # API to Redis
    arrow(svg, 560, 265, 640, 435)  # API to Object Storage

    arrow(svg, 560, 265, 340, 375)  # API to LLM Gateway
    arrow(svg, 560, 265, 340, 485)  # API to Orchestrator
    arrow(svg, 560, 265, 340, 595)  # API to Sandbox Runner

    arrow(svg, 560, 375, 980, 155)  # LLM Gateway to LLM Providers
    arrow(svg, 560, 485, 980, 255)  # Orchestrator to Notification
    arrow(svg, 560, 265, 980, 355)  # API to Identity Provider

    svg.append('</svg>')
    SVG_PATH.write_text("\n".join(svg))
    print(f"Wrote {SVG_PATH}")


if __name__ == "__main__":
    main()
