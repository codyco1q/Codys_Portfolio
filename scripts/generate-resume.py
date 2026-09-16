"""
generate-resume.py
Generates a natural, professional, high-impact PDF resume for Moaz Shahin (Cody Axton)
focusing on technical depth, architecture, and systems engineering.
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
        topMargin=32,
        bottomMargin=32,
    )

    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        name='ResumeName',
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=23,
        textColor=DARK_NAVY,
        spaceAfter=2,
    ))
    styles.add(ParagraphStyle(
        name='ResumeTitle',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13.5,
        textColor=ACCENT_BLUE,
        spaceAfter=3,
    ))
    styles.add(ParagraphStyle(
        name='ResumeContact',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=SLATE_GRAY,
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name='SectionHeader',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=DARK_NAVY,
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='JobHeader',
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11.5,
        textColor=DARK_NAVY,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='JobSubHeader',
        fontName='Helvetica-Oblique',
        fontSize=8.0,
        leading=10.5,
        textColor=SLATE_GRAY,
        spaceAfter=2,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name='ResumeBullet',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.0,
        textColor=TEXT_COLOR,
        leftIndent=11,
        firstLineIndent=-11,
        spaceAfter=1.8,
    ))
    styles.add(ParagraphStyle(
        name='SummaryBody',
        fontName='Helvetica',
        fontSize=8.3,
        leading=11.5,
        textColor=TEXT_COLOR,
        spaceAfter=4,
    ))

    def make_section(title_text):
        return [
            Paragraph(title_text.upper(), styles['SectionHeader']),
            HRFlowable(width="100%", thickness=0.75, color=LINE_COLOR, spaceBefore=1, spaceAfter=4),
        ]

    def make_role(title, company, dates, bullets):
        items = [
            Paragraph(f"<b>{title}</b> &mdash; {company}", styles['JobHeader']),
            Paragraph(dates, styles['JobSubHeader']),
        ]
        for b in bullets:
            items.append(Paragraph(f"&bull;&nbsp;&nbsp;{b}", styles['ResumeBullet']))
        items.append(Spacer(1, 3.5))
        return KeepTogether(items)

    story = []

    # ── Header ────────────────────────────────────────────────────────────────
    story.append(Paragraph("Moaz Shahin (Cody Axton)", styles['ResumeName']))
    story.append(Paragraph("Systems & Automation Engineer | Technical Operations", styles['ResumeTitle']))
    contact_line = (
        "Egypt (Remote) &nbsp;|&nbsp; "
        "<a href='mailto:codyaxton@outlook.com' color='#2563EB'>codyaxton@outlook.com</a> &nbsp;|&nbsp; "
        "<a href='https://codys-new-portfolio.vercel.app/' color='#2563EB'>Portfolio</a> &nbsp;|&nbsp; "
        "<a href='https://github.com/codyco1q' color='#2563EB'>GitHub</a> &nbsp;|&nbsp; "
        "<a href='https://www.upwork.com' color='#2563EB'>Upwork Profile</a>"
    )
    story.append(Paragraph(contact_line, styles['ResumeContact']))
    story.append(HRFlowable(width="100%", thickness=1.0, color=DARK_NAVY, spaceBefore=0, spaceAfter=5))

    # ── Summary ───────────────────────────────────────────────────────────────
    story.extend(make_section("Summary"))
    summary_text = (
        "Systems & Automation Engineer with 6+ years of experience designing scalable digital ecosystems, "
        "custom CRM architectures, and high-volume data workflows. Specializes in building reliable backend pipelines, "
        "direct-response web infrastructures, and cross-platform integrations using modern API and automation tools. "
        "Experienced in overseeing technical delivery from initial schema design to deployment and reliability monitoring."
    )
    story.append(Paragraph(summary_text, styles['SummaryBody']))

    # ── Technical Skills ──────────────────────────────────────────────────────
    story.extend(make_section("Technical Stack"))
    skills = [
        ("CRM & Marketing Systems:", "GoHighLevel (GHL), Custom Pipelines, Triggers, Webhooks, Calendar Systems, Smart Lists."),
        ("Integration & Logic Engines:", "Make (Integromat), n8n, Zapier, REST APIs, JSON Parsing, Error Routing."),
        ("Web & Data Infrastructure:", "Supabase, PostgreSQL, React, TypeScript, Tailwind CSS, Vercel, Netlify."),
        ("Operations & Protocols:", "Meta Pixel Server-Side Tracking, DNS/Domain Records, Email/SMS Gateway Delivery, QA Protocols."),
    ]
    for cat, val in skills:
        line = f"<b>{cat}</b> {val}"
        story.append(Paragraph(f"&bull;&nbsp;&nbsp;{line}", styles['ResumeBullet']))
    story.append(Spacer(1, 3))

    # ── Experience ────────────────────────────────────────────────────────────
    story.extend(make_section("Experience"))

    # 1. Fusion 44X
    story.append(make_role(
        title="Lead Funnel Engineer & Systems Architect",
        company="Fusion 44X",
        dates="2026",
        bullets=[
            "Architected full-funnel web application backed by Supabase schemas and custom performance dashboards.",
            "Implemented server-side attribution and Meta Conversions API to ensure zero data drop across user touchpoints.",
            "Constructed instant multi-channel webhook triggers for lead capture, calendar booking, and CRM updates.",
        ]
    ))

    # 2. LingoVantage
    story.append(make_role(
        title="Platform & Systems Architect",
        company="LingoVantage",
        dates="2025 &ndash; 2026",
        bullets=[
            "Built end-to-end LMS infrastructure featuring tiered student portals, automated auth, and admin controls.",
            "Engineered multi-channel dispatch pipelines connecting placement exams to Telegram and WhatsApp notifications in real time.",
            "Designed and deployed auto-grading workflows and assignment submission pipelines, eliminating manual operational bottlenecks.",
        ]
    ))

    # 3. GMC LLC
    story.append(make_role(
        title="Automation & CRM Architect",
        company="GMC LLC",
        dates="2024 &ndash; 2026",
        bullets=[
            "Developed full technical foundation across GoHighLevel, n8n, and Make for lead acquisition and customer operations.",
            "Designed and deployed conversion funnels with automated checkout, upsell logic, and dynamic lifecycle notifications.",
            "Structured CRM pipelines, tagging schemas, and custom fields to maintain clean data integrity and high email/SMS deliverability.",
            "Handled pre-launch testing, domain/DNS routing, and edge-case handling across webhook failure points.",
        ]
    ))

    # 4. Tadarab
    story.append(make_role(
        title="Automation Consultant",
        company="Tadarab",
        dates="2025",
        bullets=[
            "Built complex multi-branch routing scenarios in Make handling high-volume lead qualification and dynamic communications.",
            "Designed pipeline validation tests to maintain zero message loss across large distribution batches.",
        ]
    ))

    # 5. Mortal VA
    story.append(make_role(
        title="Founder & Technical Lead",
        company="Mortal VA",
        dates="2023 &ndash; Present",
        bullets=[
            "Founded and led a digital operations firm providing custom CRM workflows, AI automations, and web solutions.",
            "Managed project scoping, technical milestones, and quality control across 15+ international client deployments.",
            "Deployed AI-driven voice and chat agents integrated with scheduling pipelines and lead capture forms.",
        ]
    ))

    # 6. Total Post N Print
    story.append(make_role(
        title="Operations & Pipeline Lead",
        company="Total Post N Print",
        dates="2024 &ndash; 2025",
        bullets=[
            "Managed daily operational pipelines, customer lifecycle systems, and billing workflows.",
            "Streamlined handoff processes between incoming orders, technical fulfillment, and customer support.",
        ]
    ))

    # 7. Wholesale Real Estate & Solar
    story.append(make_role(
        title="Outreach Specialist & Campaign Coordinator",
        company="Wholesale Real Estate & Solar",
        dates="2019 &ndash; 2022",
        bullets=[
            "Orchestrated outbound acquisition campaigns and managed high-volume lead pipelines across direct markets.",
            "Analyzed call metrics and conversation funnels to optimize qualification workflows.",
        ]
    ))

    # ── Key Highlights ────────────────────────────────────────────────────────
    story.extend(make_section("Selected Achievements"))
    highlights = [
        "<b>System Reliability:</b> Architected 15+ scalable automation infrastructures achieving 30-40% operational efficiency improvements.",
        "<b>Technical Delivery:</b> Successfully launched 6+ complex web funnels and LMS portals with custom backend integrations and zero launch data loss.",
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