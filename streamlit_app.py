"""The Survivor's Toolkit — public download page.

Deployed on Streamlit Community Cloud. URL becomes
`https://<app-name>.streamlit.app/`.

Serves three free .xlsx sheets for Indian F&O traders:
  1. Position Sizer
  2. Risk of Ruin Calculator
  3. Trade Review (3-question weekly journal)

Brand: The Quiet Operator — calm, math-aware, contrarian. Deep-ink canvas,
mono numbers, signal-orange accent. Educational disclaimer on every surface.

The Day 6 launch content's `BUILD` DM auto-reply points to this URL.
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

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] { display: none; }
    [data-testid="collapsedControl"] { display: none; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    .stApp { background-color: #0A0E1A; }
    .main .block-container { max-width: 720px; padding-top: 4rem; padding-bottom: 4rem; }

    .qo-eyebrow {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 11px;
        letter-spacing: 3px;
        color: #94A3B8;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }
    .qo-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 36px;
        font-weight: 700;
        color: #E5E7EB;
        line-height: 1.15;
        margin-bottom: 0.5rem;
    }
    .qo-subtitle {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 16px;
        color: #94A3B8;
        line-height: 1.5;
        margin-bottom: 2.5rem;
    }
    .qo-rule {
        height: 2px;
        background: #F26B1F;
        width: 64px;
        margin-bottom: 2.5rem;
    }
    .qo-card {
        background: #111827;
        border: 1px solid #1F2937;
        border-radius: 6px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
    }
    .qo-card-title {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 18px;
        font-weight: 600;
        color: #E5E7EB;
        margin-bottom: 0.25rem;
    }
    .qo-card-lite {
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        font-size: 11px;
        color: #F26B1F;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .qo-card-desc {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 14px;
        color: #94A3B8;
        line-height: 1.5;
        margin-bottom: 1rem;
    }

    .stDownloadButton button {
        background: #1F2937 !important;
        color: #E5E7EB !important;
        border: 1px solid #374151 !important;
        font-family: 'JetBrains Mono', 'Consolas', monospace !important;
        font-size: 13px !important;
        letter-spacing: 1px !important;
        padding: 0.5rem 1.5rem !important;
        border-radius: 4px !important;
        transition: all 0.15s ease;
    }
    .stDownloadButton button:hover {
        background: #F26B1F !important;
        color: #0A0E1A !important;
        border-color: #F26B1F !important;
    }

    .qo-footer {
        font-family: 'Inter', -apple-system, sans-serif;
        font-size: 12px;
        color: #64748B;
        margin-top: 3rem;
        line-height: 1.6;
    }
    .qo-footer-rule {
        height: 1px;
        background: #1F2937;
        margin: 2rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="qo-eyebrow">The Quiet Operator</div>', unsafe_allow_html=True)
st.markdown('<div class="qo-title">The Survivor\'s Toolkit</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="qo-subtitle">Three free spreadsheets. Built by a trader, not a guru.<br>'
    'These are the lite versions of the systems I run. Open in Excel or Google Sheets — '
    'the formulas are baked in. Enter your numbers, the verdict tells you what to do.</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="qo-rule"></div>', unsafe_allow_html=True)


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
        "Win rate, avg-win, avg-loss, risk per trade — outputs the probability of ruin, "
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
        "trade, the rule that existed (or didn't) in writing before. Plus a trade table that "
        "rolls up into win rate, avg win, avg loss — feeds the Risk of Ruin Calculator. "
        "A bargaining-loop detector built in."
    ),
    filename="trade-review.xlsx",
    button_label="DOWNLOAD  trade-review.xlsx",
)

st.markdown('<div class="qo-footer-rule"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="qo-footer">'
    '<strong style="color:#94A3B8;">Educational only.</strong> Not financial advice. '
    'Build your own conviction.<br><br>'
    'These three sheets are the lite versions of the paid systems I run for my own trading. '
    'If you outgrow them, there\'s a paid version waiting. '
    'Until then, the lite sheets do 90% of what the Survivor needs.<br><br>'
    'Thirteen years trading Indian F&amp;O. Nine of them losing. I built these because '
    'I couldn\'t see the chart for the spreadsheet, and the manual work was eating '
    'my attention away from the actual trade.'
    '</div>',
    unsafe_allow_html=True,
)
