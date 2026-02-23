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


def arrow(svg, x1, y1, x2, y2):
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#333" stroke-width="1.5" marker-end="url(#arrow)" />')


def main():
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        '<defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#333" /></marker></defs>',
        f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="white" />'
    ]

    # Users
    box(svg, 80, 140, 180, 70, "Trainee", fill="#eef7ff")
    box(svg, 80, 260, 180, 70, "Trainer", fill="#eef7ff")

    # System
    box(svg, 520, 200, 360, 140, "CKA Mentor AI Platform", fill="#e8f4ff")

    # External systems
    box(svg, 1080, 120, 220, 70, "LLM Providers", fill="#fff3e6")
    box(svg, 1080, 220, 220, 70, "Notification Service", fill="#fff3e6")
    box(svg, 1080, 320, 220, 70, "Sandbox/Cluster Provider", fill="#fff3e6")
    box(svg, 1080, 420, 220, 70, "Identity Provider", fill="#fff3e6")

    # Arrows
    arrow(svg, 260, 175, 520, 240)  # Trainee to system
    arrow(svg, 260, 295, 520, 300)  # Trainer to system

    arrow(svg, 880, 240, 1080, 155)  # System to LLM
    arrow(svg, 880, 270, 1080, 255)  # System to Notification
    arrow(svg, 880, 300, 1080, 355)  # System to Sandbox
    arrow(svg, 880, 330, 1080, 455)  # System to Identity

    svg.append('</svg>')
    SVG_PATH.write_text("\n".join(svg))
    print(f"Wrote {SVG_PATH}")


if __name__ == "__main__":
    main()
