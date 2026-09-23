"""
generate-resume.py
Generates a clean, ATS-compliant PDF resume for Moaz Shahin (known professionally as Cody)
preserving the exact design, formatting, links, reverse-chronological order, and all experience items.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    KeepTogether,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'public', 'Moaz-Shahin-Resume.pdf')

DARK_NAVY  = colors.HexColor('#0F172A')
TEXT_COLOR = colors.HexColor('#1E293B')
SLATE_GRAY = colors.HexColor('#475569')
LINE_COLOR = colors.HexColor('#CBD5E1')
ACCENT_BLUE = colors.HexColor('#2563EB')

def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT_PATH,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=28,
        bottomMargin=28,
    )

    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='ResumeName',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=DARK_NAVY,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name='ResumeTitle',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=ACCENT_BLUE,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name='ResumeContact',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=SLATE_GRAY,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontName='Helvetica-Bold',
        fontSize=9.2,
        leading=12.5,
        textColor=DARK_NAVY,
        spaceBefore=5,
        spaceAfter=2,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='JobHeader',
        fontName='Helvetica-Bold',
        fontSize=8.6,
        leading=11.2,
        textColor=DARK_NAVY,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='JobSubHeader',
        fontName='Helvetica-Oblique',
        fontSize=7.8,
        leading=10.0,
        textColor=SLATE_GRAY,
        spaceAfter=1.5,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='ResumeBullet',
        fontName='Helvetica',
        fontSize=8.0,
        leading=10.6,
        textColor=TEXT_COLOR,
        leftIndent=11,
        firstLineIndent=-11,
        spaceAfter=1.5,
    ))
    styles.add(ParagraphStyle(
        name='SummaryBody',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.2,
        textColor=TEXT_COLOR,
        spaceAfter=3,
    ))

    def make_section(title_text):
        return [
            Paragraph(title_text.upper(), styles['SectionHeader']),
            HRFlowable(width="100%", thickness=0.75, color=LINE_COLOR, spaceBefore=1, spaceAfter=3),
        ]

    def make_role(title, company, dates, bullets):
        items = [
            Paragraph(f"<b>{title}</b> &mdash; {company}", styles['JobHeader']),
            Paragraph(dates, styles['JobSubHeader']),
        ]
        for b in bullets:
            items.append(Paragraph(f"&bull;&nbsp;&nbsp;{b}", styles['ResumeBullet']))
        items.append(Spacer(1, 2.5))
        return KeepTogether(items)

    story = []

    # ── Header ────────────────────────────────────────────────────────────────
    story.append(Paragraph("Moaz Shahin", styles['ResumeName']))
    story.append(Paragraph("Systems & Automation Engineer | Technical Operations", styles['ResumeTitle']))
    contact_line = (
        "Egypt (Remote) &nbsp;|&nbsp; "
        "<a href='mailto:codyaxton@outlook.com' color='#2563EB'>codyaxton@outlook.com</a> &nbsp;|&nbsp; "
        "<a href='https://codys-new-portfolio.vercel.app/' color='#2563EB'>Portfolio</a> &nbsp;|&nbsp; "
        "<a href='https://github.com/codyco1q' color='#2563EB'>GitHub</a> &nbsp;|&nbsp; "
        "<a href='https://www.upwork.com' color='#2563EB'>Upwork Profile</a>"
    )
    story.append(Paragraph(contact_line, styles['ResumeContact']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=DARK_NAVY, spaceBefore=0, spaceAfter=4))

    # ── Summary ───────────────────────────────────────────────────────────────
    story.extend(make_section("Summary"))
    summary_text = (
        "Systems & Automation Engineer with 6+ years of experience designing scalable digital ecosystems, "
        "custom CRM architectures, and high-volume data workflows (known professionally as Cody)[cite: 2]. Specializes in building "
        "reliable backend pipelines, direct-response web infrastructures, and cross-platform integrations using modern API "
        "and automation tools[cite: 2]. Experienced in overseeing technical delivery from initial schema design to production deployment, "
        "pre-launch QA protocols, and system reliability monitoring[cite: 2]."
    )
    story.append(Paragraph(summary_text, styles['SummaryBody']))

    # ── Technical Skills ──────────────────────────────────────────────────────
    story.extend(make_section("Technical Stack"))
    skills = [
        ("CRM & Marketing Systems:", "GoHighLevel (GHL), Custom Pipelines, Triggers, Webhooks, Calendar Systems, Smart Lists[cite: 2]."),
        ("Integration & Logic Engines:", "Make (Integromat), n8n, Zapier, REST APIs, JSON Parsing, Error Routing[cite: 1, 2]."),
        ("Web & Data Infrastructure:", "Supabase, PostgreSQL, React, TypeScript, Tailwind CSS, Vercel, Netlify[cite: 1, 2]."),
        ("Operations & Protocols:", "Meta Pixel Server-Side Tracking, DNS/Domain Hygiene, Email/SMS Gateway Delivery, QA Protocols[cite: 1, 2]."),
    ]
    for cat, val in skills:
        line = f"<b>{cat}</b> {val}"
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{line}", styles['ResumeBullet']))
    story.append(Spacer(1, 2))

    # ── Experience (Reverse Chronological: New to Old) ────────────────────────
    story.extend(make_section("Experience"))

    # 1. Fusion 44X (2026)
    story.append(make_role(
        title="Lead Funnel Engineer & Systems Architect",
        company="Fusion 44X",
        dates="2026",
        bullets=[
            "Architected full-funnel direct-response web application backed by Supabase schemas and custom performance dashboards[cite: 1, 2].",
            "Implemented server-side attribution and Meta Conversions API to eliminate drop-off across user acquisition touchpoints[cite: 1, 2].",
            "Constructed instant multi-channel webhook triggers for lead capture, calendar booking, and CRM updates[cite: 1, 2].",
        ]
    ))

    # 2. LingoVantage (2025 - 2026)
    story.append(make_role(
        title="Platform & Systems Architect",
        company="LingoVantage",
        dates="2025 &ndash; 2026",
        bullets=[
            "Built end-to-end LMS infrastructure featuring tiered student portals, automated auth, and admin controls[cite: 2].",
            "Engineered multi-channel dispatch pipelines connecting placement exams to Telegram and WhatsApp notifications in real time[cite: 2].",
            "Designed and deployed auto-grading workflows and assignment submission pipelines, eliminating manual operational bottlenecks[cite: 2].",
        ]
    ))

    # 3. Helping Hands Systems (2025)
    story.append(make_role(
        title="AI Automation Specialist",
        company="Helping Hands Systems",
        dates="2025",
        bullets=[
            "Designed and implemented automated workflows to streamline digital business operations, client onboarding, and lead pipelines[cite: 2].",
            "Engineered cross-platform API integrations connecting CRMs, communication channels, and internal fulfillment tools[cite: 2].",
        ]
    ))

    # 4. Tadarab (2025)
    story.append(make_role(
        title="Automation Consultant",
        company="Tadarab",
        dates="2025",
        bullets=[
            "Built complex multi-branch routing scenarios in Make handling high-volume lead qualification and dynamic communications[cite: 1].",
            "Designed pipeline validation tests to maintain zero message loss across large distribution batches[cite: 1].",
        ]
    ))

    # 5. GMC LLC (2024 - 2026)
    story.append(make_role(
        title="Automation & CRM Architect",
        company="GMC LLC",
        dates="2024 &ndash; 2026",
        bullets=[
            "Developed full technical foundation across GoHighLevel, n8n, and Make for lead acquisition and customer operations[cite: 2].",
            "Designed and deployed conversion funnels with automated checkout, upsell logic, and dynamic lifecycle notifications[cite: 2].",
            "Structured CRM pipelines, tagging schemas, and custom fields to maintain clean data integrity and high email/SMS deliverability[cite: 2].",
            "Handled pre-launch testing, domain/DNS routing, and edge-case handling across webhook failure points[cite: 2].",
        ]
    ))

    # 6. Mortal VA (2023 - Present)
    story.append(make_role(
        title="Founder & Technical Lead",
        company="Mortal VA",
        dates="2023 &ndash; Present",
        bullets=[
            "Founded and led a digital operations firm providing custom CRM workflows, AI automations, and web solutions[cite: 2].",
            "Managed project scoping, technical milestones, and quality control across 15+ international client deployments[cite: 2].",
            "Deployed AI-driven voice and chat agents integrated with scheduling pipelines and lead capture forms[cite: 2].",
        ]
    ))

    # 7. Total Post N Print (2024 - 2025)
    story.append(make_role(
        title="Operations & Pipeline Lead",
        company="Total Post N Print",
        dates="2024 &ndash; 2025",
        bullets=[
            "Managed daily operational pipelines, customer lifecycle systems, and billing workflows[cite: 2].",
            "Streamlined handoff processes between incoming orders, technical fulfillment, and customer support[cite: 2].",
        ]
    ))

    # 8. Wholesale Real Estate & Solar (2019 - 2022)
    story.append(make_role(
        title="Outreach Specialist & Campaign Coordinator",
        company="Wholesale Real Estate & Solar",
        dates="2019 &ndash; 2022",
        bullets=[
            "Orchestrated outbound acquisition campaigns and managed high-volume lead pipelines across direct markets[cite: 2].",
            "Analyzed call metrics and conversation funnels to optimize qualification workflows[cite: 2].",
        ]
    ))

    # ── Key Highlights ────────────────────────────────────────────────────────
    story.extend(make_section("Selected Achievements"))
    highlights = [
        "<b>System Reliability:</b> Architected 15+ scalable automation infrastructures achieving 30-40% operational efficiency improvements[cite: 2].",
        "<b>Technical Delivery:</b> Successfully launched 6+ complex web funnels and LMS portals with custom backend integrations and zero launch data loss[cite: 2].",
    ]
    for h in highlights:
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{h}", styles['ResumeBullet']))
    story.append(Spacer(1, 2))

    # ── Languages ─────────────────────────────────────────────────────────────
    story.extend(make_section("Languages"))
    story.append(Paragraph("<b>English:</b> Fluent &nbsp;|&nbsp; <b>Arabic:</b> Native &nbsp;|&nbsp; <b>German:</b> Intermediate", styles['SummaryBody']))

    # ── Build Document ────────────────────────────────────────────────────────
    doc.build(story)
    print(f"Resume PDF successfully generated at: {OUTPUT_PATH}")

if __name__ == '__main__':
    build_pdf()