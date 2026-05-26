"""The Survivor's Toolkit — public download page.

Deployed on Streamlit Community Cloud. URL: https://disciplined-trader-toolkit.streamlit.app/

Serves three free .xlsx sheets for Indian F&O traders, with a brand-story hero,
a "why these three" framing section, the download cards, a paid-catalog
"when you outgrow these" reveal, soft custom-build CTA via X DM (no
track-specific keyword to avoid preempting Day 15 STACK launch), trust
signals, and an educational disclaimer footer.

Brand: The Quiet Operator. Deep-ink canvas (0A0E1A), mono numbers
(JetBrains Mono / Consolas), signal-orange accent (F26B1F).
"""
from __future__ import annotations

from pathlib import Path

import streamlit as st

TOOLKIT_DIR = Path(__file__).resolve().parent / "toolkit"

st.set_page_config(
    page_title="The Survivor's Toolkit — Disciplined Trader",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Brand CSS -------------------------------------------------------------

st.markdown(
    """
    <style>
    /* Hide chrome */
    [data-testid="stSidebar"] { display: none; }
    [data-testid="collapsedControl"] { display: none; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* Canvas */
    .stApp { background-color: #0A0E1A; }
    .main .block-container { max-width: 760px; padding-top: 3.5rem; padding-bottom: 4rem; }

    /* Type scale */
    .qo-eyebrow {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 11px;
        letter-spacing: 3px;
        color: #94A3B8;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .qo-title {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 42px;
        font-weight: 700;
        color: #E5E7EB;
        line-height: 1.1;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    .qo-subtitle {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 17px;
        color: #94A3B8;
        line-height: 1.55;
        margin-bottom: 1.75rem;
    }
    .qo-rule {
        height: 2px;
        background: #F26B1F;
        width: 64px;
        margin-bottom: 2.75rem;
    }
    .qo-rule-thin {
        height: 1px;
        background: #1F2937;
        margin: 2.5rem 0;
    }

    /* Section headers */
    .qo-section-eyebrow {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 10px;
        letter-spacing: 2.5px;
        color: #F26B1F;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        margin-top: 1.5rem;
    }
    .qo-section-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 26px;
        font-weight: 600;
        color: #E5E7EB;
        line-height: 1.2;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }

    /* Story prose */
    .qo-prose {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 16px;
        color: #CBD5E1;
        line-height: 1.65;
        margin-bottom: 1.25rem;
    }
    .qo-prose-quiet {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 15px;
        color: #94A3B8;
        line-height: 1.6;
        margin-bottom: 1.25rem;
    }

    /* Three-question framing strip */
    .qo-question-row {
        display: flex;
        gap: 0;
        margin-bottom: 0.75rem;
        align-items: baseline;
    }
    .qo-question-num {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 13px;
        color: #F26B1F;
        margin-right: 1rem;
        flex-shrink: 0;
        font-weight: 600;
    }
    .qo-question-text {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 16px;
        color: #E5E7EB;
        line-height: 1.5;
    }

    /* Download cards */
    .qo-card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 6px;
        padding: 1.5rem 1.75rem 1.25rem 1.75rem;
        margin-bottom: 1rem;
    }
    .qo-card-lite {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 10px;
        color: #F26B1F;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .qo-card-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 19px;
        font-weight: 600;
        color: #E5E7EB;
        margin-bottom: 0.3rem;
    }
    .qo-card-desc {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 14px;
        color: #94A3B8;
        line-height: 1.55;
        margin-bottom: 1.1rem;
    }

    /* Download buttons */
    .stDownloadButton button {
        background: #1F2937 !important;
        color: #E5E7EB !important;
        border: 1px solid #374151 !important;
        font-family: 'JetBrains Mono', 'Consolas', monospace !important;
        font-size: 12px !important;
        letter-spacing: 1.2px !important;
        padding: 0.55rem 1.5rem !important;
        border-radius: 4px !important;
        transition: all 0.15s ease;
    }
    .stDownloadButton button:hover {
        background: #F26B1F !important;
        color: #0A0E1A !important;
        border-color: #F26B1F !important;
    }

    /* Paid catalog row */
    .qo-paid {
        background: #0F172A;
        border: 1px solid #1F2937;
        border-left: 2px solid #F26B1F;
        border-radius: 4px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }
    .qo-paid-row {
        display: flex;
        justify-content: space-between;
        align-items: baseline;
        margin-bottom: 0.25rem;
    }
    .qo-paid-name {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 16px;
        font-weight: 600;
        color: #E5E7EB;
    }
    .qo-paid-meta {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 12px;
        color: #94A3B8;
        letter-spacing: 0.5px;
    }
    .qo-paid-desc {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 13.5px;
        color: #94A3B8;
        line-height: 1.5;
    }

    /* CTA */
    .qo-cta-box {
        background: #0F172A;
        border: 1px solid #1F2937;
        border-radius: 6px;
        padding: 1.5rem 1.75rem;
        margin-top: 1.5rem;
    }
    .qo-cta-text {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 15.5px;
        color: #CBD5E1;
        line-height: 1.55;
        margin-bottom: 0.75rem;
    }
    .qo-cta-link {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 13px;
        color: #F26B1F;
        text-decoration: none;
        letter-spacing: 1.2px;
    }
    .qo-cta-link:hover { text-decoration: underline; }

    /* Trust signals */
    .qo-trust {
        background: transparent;
        padding: 1.5rem 0;
        text-align: center;
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 12px;
        color: #64748B;
        letter-spacing: 0.5px;
        line-height: 1.8;
    }
    .qo-trust-number {
        color: #E5E7EB;
        font-weight: 600;
    }

    /* Footer */
    .qo-footer {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 12px;
        color: #64748B;
        margin-top: 2rem;
        line-height: 1.7;
    }
    .qo-footer-strong { color: #94A3B8; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- HERO ------------------------------------------------------------------

st.markdown('<div class="qo-eyebrow">The Quiet Operator</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-title">The Survivor\'s Toolkit</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="qo-subtitle">Three free spreadsheets for Indian F&amp;O traders.<br>'
    'Built by a trader, not a guru.</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="qo-rule"></div>', unsafe_allow_html=True)

# --- STORY -----------------------------------------------------------------

st.markdown('<div class="qo-section-eyebrow">// why these sheets exist</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-section-title">Thirteen years. Nine of them losing.</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="qo-prose">Not because I lacked strategies. I had too many. '
    'I lost because every trade was buried under sizing math, risk checks, '
    'journal entries, and exit rules my brain had to hold in real time. '
    'I couldn\'t see the chart for the spreadsheet.</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="qo-prose">So I learned to code from zero — not to become a '
    'coder, but to put the attention back where it belongs. The first three '
    'tools I built were these. What you\'re about to download are the lite '
    'versions of those tools.</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="qo-prose-quiet">If you only fix three things in your trading process, '
    'fix the three things these sheets check.</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- THREE QUESTIONS FRAMING -----------------------------------------------

st.markdown('<div class="qo-section-eyebrow">// the three checks</div>', unsafe_allow_html=True)
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

st.markdown('<div class="qo-section-eyebrow">// download</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-section-title">The three sheets.</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="qo-prose-quiet">Open in Excel or Google Sheets. The formulas are baked in. '
    'Enter your numbers, the verdict tells you what to do.</div>',
    unsafe_allow_html=True,
)


def _download_card(title: str, lite_of: str, description: str, filename: str, button_label: str) -> None:
    st.markdown(
        f'<div class="qo-card">'
        f'<div class="qo-card-lite">LITE OF — {lite_of}</div>'
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
    title="Position Sizer Sheet",
    lite_of="Risk Management Supervisor (₹2,999)",
    description=(
        "5 inputs — capital, max risk %, entry premium, stop premium, lot size. "
        "Output is the lot count that survives a full stop-out, plus a live verdict. "
        "12 seconds to use. The arithmetic that should run before every order."
    ),
    filename="position-sizer.xlsx",
    button_label="DOWNLOAD  position-sizer.xlsx",
)

_download_card(
    title="Risk of Ruin Calculator",
    lite_of="Smart Portfolio Stats Generator (₹699)",
    description=(
        "Win rate, avg-win, avg-loss, risk per trade. Outputs the probability of ruin, "
        "expected return curve, variance bands at 50 / 100 / 200 trades. Verdict tells "
        "you whether your edge survives variance or your capital won't."
    ),
    filename="risk-of-ruin-calculator.xlsx",
    button_label="DOWNLOAD  risk-of-ruin-calculator.xlsx",
)

_download_card(
    title="Trade Review Sheet",
    lite_of="Smart Portfolio Stats Generator (₹699)",
    description=(
        "Three-question weekly journal. Largest losing day, the position size at the trigger "
        "trade, the rule that existed (or didn't) in writing before. A bargaining-loop detector "
        "built in. Rolls up into win rate, avg win, avg loss — feeds the Risk of Ruin Calculator."
    ),
    filename="trade-review.xlsx",
    button_label="DOWNLOAD  trade-review.xlsx",
)

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- OUTGROW SECTION -------------------------------------------------------

st.markdown('<div class="qo-section-eyebrow">// when you outgrow these</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-section-title">The paid versions, in case the lite sheets stop being enough.</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="qo-prose-quiet">The three sheets above do roughly 90% of what the Survivor needs. '
    'The other 10% is what these paid systems handle — multi-account routing, AI strategy '
    'discovery, sub-second execution, the things you can\'t do in a spreadsheet.</div>',
    unsafe_allow_html=True,
)

paid_products = [
    {
        "name": "Risk Management Supervisor",
        "meta": "₹2,999  ·  4.5★  ·  42 reviews",
        "desc": "The production version of the Position Sizer above. Nine checks before any order leaves your machine — capital tier, state tier, behaviour tier. Daily-loss kill switch built in.",
    },
    {
        "name": "Powerful Riyan Options Engine",
        "meta": "₹6,999  ·  4.6★  ·  52 reviews",
        "desc": "Multi-account NIFTY options. AI strategy discovery. Unwind protection in 200 ms. For the trader who lost a Monday morning because the broker took 400 ms to confirm the stop.",
    },
    {
        "name": "Enterprise Algo Execution Platform",
        "meta": "₹12,999  ·  4.9★  ·  112 reviews",
        "desc": "Full-stack execution platform. Python + Next.js + WebSocket order routing under broker rate-limits. For the trader running size across five accounts who needs sub-second deterministic execution.",
    },
]

for p in paid_products:
    st.markdown(
        f'<div class="qo-paid">'
        f'<div class="qo-paid-row">'
        f'<div class="qo-paid-name">{p["name"]}</div>'
        f'<div class="qo-paid-meta">{p["meta"]}</div>'
        f'</div>'
        f'<div class="qo-paid-desc">{p["desc"]}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

# --- CUSTOM BUILD CTA ------------------------------------------------------

st.markdown(
    '<div class="qo-cta-box">'
    '<div class="qo-cta-text">If you want a custom system built for the way you actually trade — '
    'multi-account, instrument-specific, broker-specific — DM me on X. Not a course. Not a subscription. '
    'A tool built for your workflow.</div>'
    '<a class="qo-cta-link" href="https://twitter.com/Disciplinetrad3" target="_blank">'
    'DM →  @Disciplinetrad3</a>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- TRUST SIGNALS ---------------------------------------------------------

st.markdown(
    '<div class="qo-trust">'
    '<span class="qo-trust-number">24</span> trading systems built  '
    '·  <span class="qo-trust-number">209</span> paying customer reviews '
    'across the top four products  ·  <span class="qo-trust-number">13</span> years trading Indian F&amp;O'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown('<div class="qo-rule-thin"></div>', unsafe_allow_html=True)

# --- FOOTER ----------------------------------------------------------------

st.markdown(
    '<div class="qo-footer">'
    '<span class="qo-footer-strong">Educational only.</span> Not financial advice. '
    'Build your own conviction.<br><br>'
    'These three sheets are the lite versions of the paid systems I run for my own trading. '
    'They are free because the discipline they enforce should be free. '
    'If you find yourself reaching for what the sheets can\'t do — the paid versions are above.'
    '</div>',
    unsafe_allow_html=True,
)
