from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Keep the package runnable both from its own folder and through AppTest or a
# host that launches the entry point by absolute path.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from demo_data import (
    SAMPLE_MARKETS,
    SAMPLE_REJECTIONS,
    SAMPLE_SIGNALS,
    filter_signals,
    signal_preview,
    signal_table_row,
)


st.set_page_config(
    page_title="DizaNEX | Public Demo",
    page_icon="D",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
:root { --gold:#d8b365; --purple:#a78bfa; --muted:#a4a3b2; }
.stApp { background:radial-gradient(ellipse at 8% 0%,#241b3828,transparent 38%),#0b0c12; }
section[data-testid="stSidebar"] { background:#10111a; border-right:1px solid #292836; }
div[data-testid="stMetric"] { background:linear-gradient(145deg,#171822,#11121a); border:1px solid #302c3d; border-radius:14px; padding:15px 18px; }
div[data-testid="stMetric"] label { color:#b0aeba; }
.brand { color:var(--gold); font-weight:800; letter-spacing:.2em; font-size:12px; }
.demo-badge { display:inline-block; padding:5px 11px; margin-left:10px; border:1px solid #65512d; border-radius:99px; color:#f2d89f; background:#2b2417; font-size:11px; font-weight:700; letter-spacing:.1em; }
.page-title { font-size:30px; font-weight:800; margin:.15rem 0 .1rem; }
.muted { color:var(--muted); }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="brand">DIZANEX</div>', unsafe_allow_html=True)
    st.markdown("### Institutional Dashboard")
    st.markdown('<span class="demo-badge">STATIC DEMO</span>', unsafe_allow_html=True)
    st.caption("Illustrative sample records only")
    st.divider()
    page = st.radio(
        "Dashboard navigation",
        ["Overview", "Market Scanner", "Signals", "Rejections", "Analytics"],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption("No scanner · No database · No API credentials · No Telegram connection")

st.markdown(
    f'<div class="brand">DIZANEX / CODESTER PREVIEW <span class="demo-badge">DEMO DATA — NOT LIVE</span></div>',
    unsafe_allow_html=True,
)
st.markdown(f'<div class="page-title">{page}</div>', unsafe_allow_html=True)
st.caption("Static illustrative content. This standalone preview is never connected to a live market or trading engine.")

if page == "Overview":
    confidence_values = [float(row["confidence"]) for row in SAMPLE_SIGNALS]
    a, b, c, d = st.columns(4)
    a.metric("Sample signal records", len(SAMPLE_SIGNALS))
    b.metric("Sample rejection events", len(SAMPLE_REJECTIONS))
    c.metric("Sample pairs", len({row["pair"] for row in SAMPLE_MARKETS}))
    d.metric("Mean sample confidence", f"{sum(confidence_values) / len(confidence_values):.1f}")
    st.subheader("Sample market snapshot")
    st.dataframe(SAMPLE_MARKETS[:4], use_container_width=True, hide_index=True)
    st.subheader("Recent sample signals")
    st.dataframe([signal_table_row(row) for row in SAMPLE_SIGNALS[:4]], use_container_width=True, hide_index=True)
    st.caption("All values on this page are static demonstration records, not current market observations.")

elif page == "Market Scanner":
    st.subheader("Illustrative scanner rows")
    st.caption("Sample observed prices and classifications; this package does not scan markets.")
    st.dataframe(SAMPLE_MARKETS, use_container_width=True, hide_index=True)

elif page == "Signals":
    st.subheader("Sample signal history")
    pair_options = ["All pairs", *sorted({row["pair"] for row in SAMPLE_SIGNALS})]
    f1, f2, f3 = st.columns([1, 1, 1.2])
    pair = f1.selectbox("Pair", pair_options)
    direction = f2.selectbox("Direction", ["All directions", "LONG", "SHORT"])
    minimum = f3.slider("Minimum sample confidence", 0, 100, 70)
    rows = filter_signals(
        SAMPLE_SIGNALS, pair=pair, direction=direction,
        minimum_confidence=minimum,
    )
    if rows:
        st.dataframe([signal_table_row(row) for row in rows], use_container_width=True, hide_index=True)
        with st.expander("Read-only sample message preview"):
            st.code(signal_preview(rows[0]), language="text")
            st.caption("Preview only. No message is sent or connected to Telegram.")
    else:
        st.info("No sample signal matches these filters.")

elif page == "Rejections":
    st.subheader("Sample rejection monitor")
    st.dataframe(SAMPLE_REJECTIONS, use_container_width=True, hide_index=True)
    st.caption("Reasons and filter notes are illustrative sample records, not scanner output.")

else:
    st.subheader("Sample history analytics")
    st.caption("Charts summarize only the static sample signal set.")
    long_count = sum(row["direction"] == "LONG" for row in SAMPLE_SIGNALS)
    short_count = sum(row["direction"] == "SHORT" for row in SAMPLE_SIGNALS)
    st.markdown("**Signal direction distribution — sample records**")
    st.bar_chart({"LONG": long_count, "SHORT": short_count})

    st.markdown("**Confidence distribution — sample records**")
    confidence_bins = {"70–79": 0, "80–89": 0, "90–100": 0}
    for row in SAMPLE_SIGNALS:
        score = float(row["confidence"])
        bucket = "70–79" if score < 80 else "80–89" if score < 90 else "90–100"
        confidence_bins[bucket] += 1
    st.bar_chart(confidence_bins)

    st.markdown("**Pair activity — sample records**")
    pair_counts: dict[str, int] = {}
    for row in SAMPLE_SIGNALS:
        pair_counts[row["pair"]] = pair_counts.get(row["pair"], 0) + 1
    st.bar_chart(pair_counts)
    st.caption("No profitability, outcome, or win-rate claims are made.")
