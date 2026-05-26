"""The Survivor's Toolkit — public download page.

Aligned visually with sureshbalaraman.com — the brand owner's primary site.
Electric-cyan accent, uppercase mono system names, sans + mono mix, anti-fluff
voice ("Finance isn't creative writing"), WhatsApp-first contact.

Supports BOTH light and dark themes via prefers-color-scheme media queries.
Default = follow system preference.

Toolkit content is 100% free. The paid catalog lives at sureshbalaraman.com —
this page links there once, in the "when you outgrow these" section.
"""
from __future__ import annotations

from pathlib import Path

import streamlit as st

TOOLKIT_DIR = Path(__file__).resolve().parent / "toolkit"

WHATSAPP_URL = "https://wa.me/919677477233"
EMAIL = "suresh2kb@gmail.com"
MAIN_SITE = "https://www.sureshbalaraman.com/"

st.set_page_config(
    page_title="The Survivor's Toolkit · Suresh Balaraman",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Theme tokens via CSS custom properties --------------------------------
# Two themes: dark (default) + light (via prefers-color-scheme: light).
# All component CSS reads from these tokens — change here, propagate everywhere.

st.markdown(
    """
    <style>
    /* ---------- Theme tokens ---------- */
    :root {
        --bg: #0A0E1A;
        --surface: #111827;
        --surface-alt: #0F172A;
        --border: #1F2937;
        --text-primary: #E5E7EB;
        --text-secondary: #94A3B8;
        --text-quiet: #64748B;
        --accent: #22D3EE;
        --accent-dim: rgba(34, 211, 238, 0.12);
        --btn-bg: #1F2937;
        --btn-bg-hover: #22D3EE;
        --btn-text: #E5E7EB;
        --btn-text-hover: #0A0E1A;
        --btn-border: #374151;
    }

    @media (prefers-color-scheme: light) {
        :root {
            --bg: #FAFAFA;
            --surface: #FFFFFF;
            --surface-alt: #F4F4F5;
            --border: #E4E4E7;
            --text-primary: #18181B;
            --text-secondary: #52525B;
            --text-quiet: #71717A;
            --accent: #0891B2;
            --accent-dim: rgba(8, 145, 178, 0.10);
            --btn-bg: #F4F4F5;
            --btn-bg-hover: #0891B2;
            --btn-text: #18181B;
            --btn-text-hover: #FFFFFF;
            --btn-border: #E4E4E7;
        }
    }

    /* ---------- Chrome hide ---------- */
    [data-testid="stSidebar"] { display: none; }
    [data-testid="collapsedControl"] { display: none; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* ---------- Canvas ---------- */
    .stApp { background-color: var(--bg) !important; }
    .main .block-container {
        max-width: 760px;
        padding-top: 3.5rem;
        padding-bottom: 4rem;
    }

    /* ---------- Hero ---------- */
    .qo-eyebrow {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 11px;
        letter-spacing: 2.5px;
        color: var(--accent);
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .qo-title {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 44px;
        font-weight: 700;
        color: var(--text-primary);
        line-height: 1.05;
        margin-bottom: 0.75rem;
        letter-spacing: -0.025em;
    }
    .qo-subtitle {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 18px;
        color: var(--text-secondary);
        line-height: 1.5;
        margin-bottom: 2rem;
        max-width: 600px;
    }
    .qo-rule {
        height: 2px;
        background: var(--accent);
        width: 56px;
        margin-bottom: 3rem;
    }
    .qo-rule-thin {
        height: 1px;
        background: var(--border);
        margin: 3rem 0;
    }

    /* ---------- Section headers ---------- */
    .qo-section-eyebrow {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 10px;
        letter-spacing: 2.5px;
        color: var(--accent);
        text-transform: uppercase;
        margin-bottom: 0.75rem;
    }
    .qo-section-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 28px;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1.2;
        margin-bottom: 1.25rem;
        letter-spacing: -0.015em;
    }

    /* ---------- Prose ---------- */
    .qo-prose {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 16px;
        color: var(--text-primary);
        line-height: 1.65;
        margin-bottom: 1.25rem;
    }
    .qo-prose-quiet {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 15px;
        color: var(--text-secondary);
        line-height: 1.6;
        margin-bottom: 1.25rem;
    }
    .qo-quote {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 17px;
        font-style: italic;
        color: var(--text-primary);
        line-height: 1.55;
        padding: 0.5rem 0 0.5rem 1.25rem;
        border-left: 2px solid var(--accent);
        margin: 1.5rem 0;
    }

    /* ---------- The three checks ---------- */
    .qo-question-row {
        display: flex;
        gap: 0;
        margin-bottom: 0.85rem;
        align-items: baseline;
    }
    .qo-question-num {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 13px;
        color: var(--accent);
        margin-right: 1.25rem;
        flex-shrink: 0;
        font-weight: 600;
    }
    .qo-question-text {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 16px;
        color: var(--text-primary);
        line-height: 1.5;
    }

    /* ---------- Download cards ---------- */
    .qo-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 6px;
        padding: 1.5rem 1.75rem 1.25rem 1.75rem;
        margin-bottom: 1rem;
    }
    .qo-card-system {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 11px;
        color: var(--accent);
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }
    .qo-card-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 19px;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.4rem;
    }
    .qo-card-desc {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 14px;
        color: var(--text-secondary);
        line-height: 1.55;
        margin-bottom: 1.1rem;
    }

    /* ---------- Download buttons ---------- */
    .stDownloadButton button {
        background: var(--btn-bg) !important;
        color: var(--btn-text) !important;
        border: 1px solid var(--btn-border) !important;
        font-family: 'JetBrains Mono', 'Consolas', monospace !important;
        font-size: 12px !important;
        letter-spacing: 1.2px !important;
        padding: 0.55rem 1.5rem !important;
        border-radius: 4px !important;
        transition: all 0.15s ease;
    }
    .stDownloadButton button:hover {
        background: var(--btn-bg-hover) !important;
        color: var(--btn-text-hover) !important;
        border-color: var(--btn-bg-hover) !important;
    }

    /* ---------- WhatsApp + outgrow CTA ---------- */
    .qo-cta-box {
        background: var(--surface-alt);
        border: 1px solid var(--border);
        border-left: 2px solid var(--accent);
        border-radius: 4px;
        padding: 1.5rem 1.75rem;
        margin: 1.5rem 0;
    }
    .qo-cta-text {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 15.5px;
        color: var(--text-primary);
        line-height: 1.55;
        margin-bottom: 0.75rem;
    }
    .qo-cta-row {
        display: flex;
        gap: 1.5rem;
        flex-wrap: wrap;
        align-items: center;
        margin-top: 0.75rem;
    }
    .qo-cta-link {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 13px;
        color: var(--accent);
        text-decoration: none;
        letter-spacing: 1px;
    }
    .qo-cta-link:hover { text-decoration: underline; }

    /* ---------- Metric badges ---------- */
    .qo-metrics {
        display: flex;
        gap: 2.5rem;
        justify-content: center;
        flex-wrap: wrap;
        padding: 1.5rem 0;
        text-align: center;
    }
    .qo-metric {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .qo-metric-num {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 28px;
        font-weight: 700;
        color: var(--text-primary);
        line-height: 1;
        letter-spacing: -0.02em;
    }
    .qo-metric-label {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 10px;
        color: var(--text-quiet);
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 0.4rem;
    }

    /* ---------- Footer ---------- */
    .qo-footer {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 12.5px;
        color: var(--text-quiet);
        margin-top: 2rem;
        line-height: 1.7;
    }
    .qo-footer-strong { color: var(--text-secondary); font-weight: 600; }
    .qo-footer-quote {
        font-style: italic;
        color: var(--text-secondary);
        margin: 1rem 0;
        padding-left: 1rem;
        border-left: 1px solid var(--border);
    }
    .qo-footer-link {
        color: var(--accent);
        text-decoration: none;
    }
    .qo-footer-link:hover { text-decoration: underline; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HERO ------------------------------------------------------------------

st.markdown('<div class="qo-eyebrow">// THE_SURVIVORS_TOOLKIT</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-title">Three free spreadsheets.<br>Built by a trader, not a guru.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="qo-subtitle">'
    'For Indian F&amp;O traders. Formulas baked in. Open in Excel or Google Sheets, '
    'enter your numbers, the verdict tells you what to do.'
    '</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="qo-rule"></div>', unsafe_allow_html=True)

# --- STORY -----------------------------------------------------------------

st.markdown('<div class="qo-section-eyebrow">// WHY THESE EXIST</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-section-title">Thirteen years. Nine of them losing.</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="qo-prose">Not because I lacked strategies. I had too many. '
    'I lost because every trade was buried under sizing math, risk checks, journal entries, '
    'and exit rules my brain had to hold in real time. I couldn\'t see the chart for the spreadsheet.</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="qo-prose">So I learned to code from zero — not to become a coder, '
    'but to put the attention back where it belongs. '
    'The first three tools I built were these.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="qo-quote">Finance isn\'t creative writing. Ambiguity is expensive.</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- THREE CHECKS ----------------------------------------------------------

st.markdown('<div class="qo-section-eyebrow">// THE THREE CHECKS</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-section-title">Three sheets. Three questions you should answer before every trade.</div>', unsafe_allow_html=True)

questions = [
    ("01", "Are you sized to survive a full stop-out?"),
    ("02", "Does your edge survive variance — or does your capital give out first?"),
    ("03", "Did a rule exist in writing before the trade?"),
]
for num, q in questions:
    st.markdown(
        f'<div class="qo-question-row">'
        f'<div class="qo-question-num">{num}</div>'
        f'<div class="qo-question-text">{q}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- DOWNLOAD CARDS --------------------------------------------------------

st.markdown('<div class="qo-section-eyebrow">// DOWNLOAD</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-section-title">The three sheets.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="qo-prose-quiet">All three are free. No email gate. '
    'No "enter your name and capital." Download, open, enter your numbers, read the verdict.</div>',
    unsafe_allow_html=True,
)


def _download_card(title: str, system_name: str, description: str, filename: str, button_label: str) -> None:
    st.markdown(
        f'<div class="qo-card">'
        f'<div class="qo-card-system">{system_name}</div>'
        f'<div class="qo-card-title">{title}</div>'
        f'<div class="qo-card-desc">{description}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    file_path = TOOLKIT_DIR / filename
    if file_path.exists():
        with file_path.open("rb") as f:
            st.download_button(
                label=button_label,
                data=f.read(),
                file_name=filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key=f"dl_{filename}",
                use_container_width=False,
            )
    else:
        st.error(f"File not found: {filename}")
    st.markdown("<br>", unsafe_allow_html=True)


_download_card(
    title="Position Sizer",
    system_name="POSITION_SIZER.XLSX",
    description=(
        "5 inputs — capital, max risk %, entry premium, stop premium, lot size. "
        "Output is the lot count that survives a full stop-out, plus a live verdict. "
        "12 seconds to use. The arithmetic that should run before every order."
    ),
    filename="position-sizer.xlsx",
    button_label="↓  POSITION_SIZER.XLSX",
)

_download_card(
    title="Risk of Ruin Calculator",
    system_name="RISK_OF_RUIN.XLSX",
    description=(
        "Win rate, avg-win, avg-loss, risk per trade. Outputs the probability of ruin, "
        "expected return curve, variance bands at 50 / 100 / 200 trades. The verdict tells "
        "you whether your edge survives variance or your capital gives out first."
    ),
    filename="risk-of-ruin-calculator.xlsx",
    button_label="↓  RISK_OF_RUIN.XLSX",
)

_download_card(
    title="Trade Review Sheet",
    system_name="TRADE_REVIEW.XLSX",
    description=(
        "Three-question weekly journal. Largest losing day, the position size at the trigger "
        "trade, the rule that existed (or didn't) in writing before. A bargaining-loop detector "
        "built in. Rolls up into win rate, avg win, avg loss — feeds the Risk of Ruin calculator."
    ),
    filename="trade-review.xlsx",
    button_label="↓  TRADE_REVIEW.XLSX",
)

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- METRICS ---------------------------------------------------------------

st.markdown('<div class="qo-section-eyebrow">// DOCUMENTED RESULTS</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-section-title">From live production systems.</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="qo-metrics">'
    '<div class="qo-metric"><div class="qo-metric-num">13+</div>'
    '<div class="qo-metric-label">YEARS<br>TRADING</div></div>'
    '<div class="qo-metric"><div class="qo-metric-num">34</div>'
    '<div class="qo-metric-label">SYSTEMS<br>SHIPPED</div></div>'
    '<div class="qo-metric"><div class="qo-metric-num">209</div>'
    '<div class="qo-metric-label">PAYING<br>REVIEWS</div></div>'
    '<div class="qo-metric"><div class="qo-metric-num">&lt;50ms</div>'
    '<div class="qo-metric-label">EXECUTION<br>LATENCY</div></div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- WHEN YOU OUTGROW THESE ------------------------------------------------

st.markdown('<div class="qo-section-eyebrow">// WHEN YOU OUTGROW THESE</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-section-title">The full system catalog lives on my main site.</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="qo-prose-quiet">The three sheets above do roughly 90% of what the Survivor needs. '
    'The other 10% — multi-account routing, AI strategy discovery, sub-second execution, '
    'the things you can\'t do in a spreadsheet — lives in the 34-system catalog at the link below.</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="qo-cta-box">'
    f'<div class="qo-cta-text">Browse all 34 production systems — trading, AI, and enterprise. '
    f'Or DM me on WhatsApp if you want a custom system built for your trading workflow. '
    f'Not a course. Not a subscription. A tool built for the way you actually trade.</div>'
    f'<div class="qo-cta-row">'
    f'<a class="qo-cta-link" href="{MAIN_SITE}" target="_blank">→  sureshbalaraman.com</a>'
    f'<a class="qo-cta-link" href="{WHATSAPP_URL}" target="_blank">→  WhatsApp +91 96774 77233</a>'
    f'<a class="qo-cta-link" href="mailto:{EMAIL}">→  {EMAIL}</a>'
    f'</div>'
    f'</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- FOOTER ----------------------------------------------------------------

st.markdown(
    f'<div class="qo-footer">'
    f'<div class="qo-footer-quote">Great systems aren\'t flashy. They\'re reliable, scalable, '
    f'and quietly solve hard problems.</div>'
    f'<span class="qo-footer-strong">Educational only.</span> Not financial advice. '
    f'Build your own conviction.<br><br>'
    f'These three sheets are the lite versions of the paid systems I run for my own trading. '
    f'They\'re free because the discipline they enforce should be free. '
    f'If you outgrow them, the full catalog is at '
    f'<a class="qo-footer-link" href="{MAIN_SITE}" target="_blank">sureshbalaraman.com</a>.'
    f'</div>',
    unsafe_allow_html=True,
)
