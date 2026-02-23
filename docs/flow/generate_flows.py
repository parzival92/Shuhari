#!/usr/bin/env python3
from pathlib import Path

WIDTH = 2000
HEIGHT = 1200

OUT_DIR = Path(__file__).parent


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


def svg_start():
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        '<defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7" fill="#333" /></marker></defs>',
        f'<rect x="0" y="0" width="{WIDTH}" height="{HEIGHT}" fill="white" />'
    ]


def write_svg(name: str, svg):
    svg.append('</svg>')
    path = OUT_DIR / f"{name}.svg"
    path.write_text("\n".join(svg))
    print(f"Wrote {path}")


def data_flow():
    svg = svg_start()
    # Users
    box(svg, 100, 220, 180, 70, "Trainee", fill="#eef7ff")
    box(svg, 100, 330, 180, 70, "Trainer", fill="#eef7ff")

    # Core
    box(svg, 380, 275, 200, 70, "Web UI", fill="#e8f4ff")
    box(svg, 650, 275, 220, 70, "API Gateway", fill="#e8f4ff")

    # Services
    box(svg, 980, 160, 220, 70, "Assessment Service")
    box(svg, 980, 275, 220, 70, "Plan Service")
    box(svg, 980, 390, 220, 70, "Training Service")

    # Data stores
    box(svg, 1300, 170, 220, 70, "Postgres", fill="#e8f4ff")
    box(svg, 1300, 285, 220, 70, "Object Storage", fill="#e8f4ff")
    box(svg, 1300, 400, 220, 70, "Redis", fill="#e8f4ff")

    # External systems
    box(svg, 1600, 160, 220, 70, "LLM Gateway", fill="#fff3e6")
    box(svg, 1600, 275, 220, 70, "Notification Service", fill="#fff3e6")
    box(svg, 1600, 390, 220, 70, "Sandbox Runner", fill="#fff3e6")
    box(svg, 1600, 505, 220, 70, "Observability", fill="#fff3e6")

    # Arrows
    arrow(svg, 280, 255, 380, 310)
    arrow(svg, 280, 365, 380, 310)
    arrow(svg, 580, 310, 650, 310)

    arrow(svg, 870, 310, 980, 195)
    arrow(svg, 870, 310, 980, 310)
    arrow(svg, 870, 310, 980, 425)

    arrow(svg, 1200, 195, 1300, 205)
    arrow(svg, 1200, 310, 1300, 320)
    arrow(svg, 1200, 425, 1300, 435)

    arrow(svg, 1520, 205, 1600, 205)
    arrow(svg, 1520, 320, 1600, 320)
    arrow(svg, 1520, 435, 1600, 435)
    arrow(svg, 1200, 425, 1600, 520)

    write_svg("data-flow", svg)


def functional_flow():
    svg = svg_start()
    steps = [
        "Onboarding",
        "Baseline\nAssessment",
        "Plan\nGeneration",
        "Human\nReview",
        "Sprint\nModules",
        "Deliverable\nReview",
        "Sprint\nReview",
        "Readiness\nGates",
        "Exam",
        "Post-Exam\nReport",
    ]
    x = 100
    y = 250
    w = 160
    h = 80
    gap = 30
    for i, label in enumerate(steps):
        box(svg, x, y, w, h, label, fill="#e8f4ff")
        if i < len(steps) - 1:
            arrow(svg, x + w, y + h/2, x + w + gap, y + h/2)
        x += w + gap
    write_svg("functional-flow", svg)


def modules_flow():
    svg = svg_start()
    # Core modules
    box(svg, 200, 200, 220, 90, "C1\nAssessment", fill="#e8f4ff")
    box(svg, 480, 200, 220, 90, "C2\nPlan", fill="#e8f4ff")
    box(svg, 760, 200, 220, 90, "C3\nTraining", fill="#e8f4ff")
    box(svg, 1040, 200, 220, 90, "C4\nEvaluation", fill="#e8f4ff")

    # Supporting
    box(svg, 200, 380, 220, 90, "Memory\nSystem", fill="#fff3e6")
    box(svg, 480, 380, 220, 90, "Orchestrator", fill="#fff3e6")
    box(svg, 760, 380, 220, 90, "LLM\nGateway", fill="#fff3e6")
    box(svg, 1040, 380, 220, 90, "Trainer\nReview", fill="#fff3e6")

    # Arrows
    arrow(svg, 420, 245, 480, 245)
    arrow(svg, 700, 245, 760, 245)
    arrow(svg, 980, 245, 1040, 245)

    arrow(svg, 310, 290, 310, 380)
    arrow(svg, 590, 290, 590, 380)
    arrow(svg, 870, 290, 870, 380)
    arrow(svg, 1150, 290, 1150, 380)

    write_svg("modules", svg)


def technical_flow():
    svg = svg_start()
    # Pipeline
    box(svg, 120, 260, 180, 80, "Client", fill="#eef7ff")
    box(svg, 340, 260, 200, 80, "API Gateway", fill="#e8f4ff")
    box(svg, 580, 260, 200, 80, "Auth/RBAC", fill="#e8f4ff")
    box(svg, 820, 260, 220, 80, "Service Router", fill="#e8f4ff")
    box(svg, 1080, 260, 220, 80, "Domain Service", fill="#e8f4ff")
    box(svg, 1340, 260, 220, 80, "Queue/Worker", fill="#fff3e6")
    box(svg, 1600, 260, 220, 80, "LLM Gateway", fill="#fff3e6")

    box(svg, 1080, 420, 220, 80, "Postgres", fill="#e8f4ff")
    box(svg, 1340, 420, 220, 80, "Object Storage", fill="#e8f4ff")
    box(svg, 1600, 420, 220, 80, "Sandbox Runner", fill="#fff3e6")

    # Arrows
    arrow(svg, 300, 300, 340, 300)
    arrow(svg, 540, 300, 580, 300)
    arrow(svg, 780, 300, 820, 300)
    arrow(svg, 1040, 300, 1080, 300)
    arrow(svg, 1300, 300, 1340, 300)
    arrow(svg, 1560, 300, 1600, 300)

    arrow(svg, 1190, 340, 1190, 420)
    arrow(svg, 1450, 340, 1450, 420)
    arrow(svg, 1710, 340, 1710, 420)

    write_svg("technical-flow", svg)


def main():
    data_flow()
    functional_flow()
    modules_flow()
    technical_flow()


if __name__ == "__main__":
    main()
