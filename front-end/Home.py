import streamlit as st
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]


@st.cache_data(show_spinner=False)
def _safe_joblib_load(path: Path):
    try:
        import joblib

        if path.exists():
            return joblib.load(path)
        return None
    except Exception:
        return None


def _go_to(page_path: str):
    try:
        st.switch_page(page_path)
    except Exception:
        st.info(f"Open this page from the sidebar: `{page_path}`")


st.set_page_config(page_title="Real Estate App", layout="wide")

st.markdown(
    """
    <style>
      :root {
        --card-bg: rgba(255,255,255,0.03);
        --card-border: rgba(255,255,255,0.10);
        --card-border-soft: rgba(255,255,255,0.06);
        --shadow: 0 10px 30px rgba(0,0,0,0.25);
        --shadow-soft: 0 8px 24px rgba(0,0,0,0.18);
      }

      .block-container { padding-top: 1.25rem; padding-bottom: 2.0rem; }

      .app-hero {
        padding: 1.4rem 1.5rem;
        border: 1px solid var(--card-border);
        background:
          radial-gradient(1200px 300px at 10% 0%, rgba(99,102,241,0.25), transparent 60%),
          radial-gradient(900px 260px at 90% 10%, rgba(16,185,129,0.18), transparent 60%),
          linear-gradient(135deg, rgba(99,102,241,0.16), rgba(16,185,129,0.08));
        border-radius: 18px;
        box-shadow: var(--shadow-soft);
      }
      .app-hero h1 { margin: 0 0 .35rem 0; line-height: 1.08; letter-spacing: -0.02em; }
      .app-hero p { margin: 0; opacity: 0.92; max-width: 70ch; }

      .card {
        padding: 1.05rem 1.05rem;
        border: 1px solid var(--card-border-soft);
        border-radius: 16px;
        background: var(--card-bg);
        box-shadow: none;
        transition: transform 120ms ease, box-shadow 120ms ease, border-color 120ms ease;
      }
      .card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow);
        border-color: var(--card-border);
      }

      .muted { opacity: 0.85; }

      [data-testid="stMetric"] {
        padding: 0.85rem 0.95rem;
        border-radius: 16px;
        border: 1px solid var(--card-border-soft);
        background: var(--card-bg);
      }
      [data-testid="stMetric"]:hover { border-color: var(--card-border); }

      div.stButton > button {
        border-radius: 12px;
        padding: 0.55rem 0.85rem;
        border: 1px solid rgba(255,255,255,0.14);
        background: rgba(255,255,255,0.04);
      }
      div.stButton > button:hover {
        border-color: rgba(255,255,255,0.24);
        background: rgba(255,255,255,0.06);
      }

      .pill-row { display: flex; flex-wrap: wrap; gap: .5rem; }
      .pill {
        display: inline-flex;
        align-items: center;
        gap: .4rem;
        padding: .38rem .6rem;
        border-radius: 999px;
        border: 1px solid var(--card-border-soft);
        background: rgba(255,255,255,0.035);
        font-size: 0.92rem;
        white-space: nowrap;
      }
      .pill b { font-weight: 650; }
      .pill .dot {
        width: 8px;
        height: 8px;
        border-radius: 999px;
        background: rgba(255,255,255,0.35);
      }

      .wf-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: .75rem; }
      @media (max-width: 900px) { .wf-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
      @media (max-width: 600px) { .wf-grid { grid-template-columns: 1fr; } }
      .wf-step {
        padding: 0.95rem 1.0rem;
        border-radius: 16px;
        border: 1px solid var(--card-border-soft);
        background: var(--card-bg);
      }
      .wf-top { display: flex; align-items: center; gap: .65rem; margin-bottom: .25rem; }
      .wf-num {
        width: 28px; height: 28px;
        display: inline-flex; align-items: center; justify-content: center;
        border-radius: 999px;
        background: rgba(99,102,241,0.20);
        border: 1px solid rgba(99,102,241,0.25);
        font-weight: 700;
      }
      .wf-title { font-weight: 650; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="app-hero">
      <h1>Lahore Real Estate Intelligence System</h1>
      <p class="muted">AI-powered price prediction, society recommendations, and feature insights — all in one dashboard.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.sidebar.header("Navigation")
if hasattr(st.sidebar, "page_link"):
    st.sidebar.page_link("Home.py", label="🏠 Home", icon="🏠")
    st.sidebar.page_link("pages/Price_Predictor.py", label="🔮 Price Predictor")
    st.sidebar.page_link("pages/recomender_sys.py", label="🎯 Recommendation System")
    st.sidebar.page_link("pages/insight_module.py", label="📊 Insights Module")
    st.sidebar.page_link("pages/Analysis_App.py", label="📈 Analytics")
else:
    if st.sidebar.button("🔮 Price Predictor", use_container_width=True):
        _go_to("pages/Price_Predictor.py")
    if st.sidebar.button("🎯 Recommendation System", use_container_width=True):
        _go_to("pages/recomender_sys.py")
    if st.sidebar.button("📊 Insights Module", use_container_width=True):
        _go_to("pages/insight_module.py")
    if st.sidebar.button("📈 Analytics", use_container_width=True):
        _go_to("pages/Analysis_App.py")

st.markdown("### Project Overview")
st.write(
    "This platform helps you **estimate property prices**, **discover similar societies**, and **understand which features influence prices** "
    "using trained ML pipelines and explainable insights."
)

st.markdown("### Quick Access")
nav1, nav2, nav3 = st.columns(3)
with nav1:
    st.markdown(
        '<div class="card"><b>🔮 Price Predictor</b><div class="muted">Predict house & flat prices.</div></div>',
        unsafe_allow_html=True,
    )
    if st.button("Open Price Predictor", use_container_width=True):
        _go_to("pages/Price_Predictor.py")
with nav2:
    st.markdown(
        '<div class="card"><b>🎯 Recommendation System</b><div class="muted">Find similar societies.</div></div>',
        unsafe_allow_html=True,
    )
    if st.button("Open Recommendations", use_container_width=True):
        _go_to("pages/recomender_sys.py")
with nav3:
    st.markdown(
        '<div class="card"><b>📊 Insights Module</b><div class="muted">Understand feature impacts.</div></div>',
        unsafe_allow_html=True,
    )
    if st.button("Open Insights", use_container_width=True):
        _go_to("pages/insight_module.py")

st.markdown("### Dataset Statistics")
houses_df = _safe_joblib_load(BASE_DIR / "artifacts" / "models" / "houses_df.pkl")
flats_df = _safe_joblib_load(BASE_DIR / "artifacts" / "models" / "flats_df.pkl")
society_df = _safe_joblib_load(BASE_DIR / "artifacts" / "recommender" / "society_df.pkl")

total_houses = int(getattr(houses_df, "shape", [0])[0] or 0) if houses_df is not None else 0
total_flats = int(getattr(flats_df, "shape", [0])[0] or 0) if flats_df is not None else 0
total_properties = total_houses + total_flats


def _avg_price(df):
    try:
        if df is None or "price" not in df.columns:
            return None
        prices = df["price"].dropna().astype(float)
        return float(prices.mean()) if len(prices) else None
    except Exception:
        return None


avg_house = _avg_price(houses_df)
avg_flat = _avg_price(flats_df)
avg_price = None
if avg_house is not None and avg_flat is not None:
    avg_price = (avg_house + avg_flat) / 2.0
elif avg_house is not None:
    avg_price = avg_house
elif avg_flat is not None:
    avg_price = avg_flat

total_societies = 0
try:
    if society_df is not None:
        col = "Society" if "Society" in society_df.columns else ("society" if "society" in society_df.columns else None)
        if col is not None:
            total_societies = int(society_df[col].nunique())
except Exception:
    total_societies = 0

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Total Properties", f"{total_properties:,}")
m2.metric("Total Houses", f"{total_houses:,}")
m3.metric("Total Flats", f"{total_flats:,}")
m4.metric("Total Societies", f"{total_societies:,}")
m5.metric("Avg Price", "—" if avg_price is None else f"{avg_price:,.0f}")

st.markdown("### Visual Analytics")
left, right = st.columns([2, 1])
with left:
    st.markdown(
        '<div class="card"><b>Price Distribution</b><div class="muted">Combined sample from available datasets.</div></div>',
        unsafe_allow_html=True,
    )
    try:
        import pandas as pd

        series_list = []
        if houses_df is not None and "price" in houses_df.columns:
            series_list.append(houses_df["price"])
        if flats_df is not None and "price" in flats_df.columns:
            series_list.append(flats_df["price"])

        if series_list:
            prices = pd.concat(series_list, ignore_index=True).dropna().astype(float)
            st.bar_chart(prices, height=220)
        else:
            st.info("Price chart unavailable (missing `price` column).")
    except Exception:
        st.info("Price chart unavailable (dataset read issue).")

with right:
    st.markdown(
        '<div class="card"><b>Property Mix</b><div class="muted">Houses vs Flats count.</div></div>',
        unsafe_allow_html=True,
    )
    try:
        import pandas as pd

        mix = pd.DataFrame({"Type": ["Houses", "Flats"], "Count": [total_houses, total_flats]}).set_index("Type")
        st.bar_chart(mix, height=220)
    except Exception:
        st.info("Mix chart unavailable.")

st.markdown("### Technologies")
st.markdown(
    """
    <div class="pill-row">
      <span class="pill"><span class="dot"></span><b>Python</b></span>
      <span class="pill"><span class="dot"></span><b>Streamlit</b></span>
      <span class="pill"><span class="dot"></span><b>Pandas</b></span>
      <span class="pill"><span class="dot"></span><b>Scikit-Learn</b></span>
      <span class="pill"><span class="dot"></span><b>XGBoost</b></span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("### ML Workflow / Pipeline")
st.markdown(
    """
    <div class="wf-grid">
      <div class="wf-step"><div class="wf-top"><span class="wf-num">1</span><span class="wf-title">Data Gathering</span></div><div class="muted">Scraping &amp; collection</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">2</span><span class="wf-title">Data Cleaning</span></div><div class="muted">Schema &amp; quality fixes</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">3</span><span class="wf-title">Feature Engineering</span></div><div class="muted">Transformations &amp; derived fields</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">4</span><span class="wf-title">EDA</span></div><div class="muted">Patterns &amp; correlations</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">5</span><span class="wf-title">Outlier Detection</span></div><div class="muted">Robust filtering</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">6</span><span class="wf-title">Missing Value Imputation</span></div><div class="muted">Consistent imputation rules</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">7</span><span class="wf-title">Feature Selection</span></div><div class="muted">Signal-focused inputs</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">8</span><span class="wf-title">Model Selection &amp; Productionization</span></div><div class="muted">Training, pipelines, artifacts</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">9</span><span class="wf-title">Analytics Module</span></div><div class="muted">Exploration &amp; visuals</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">10</span><span class="wf-title">Recommendation System</span></div><div class="muted">Society similarity</div></div>
      <div class="wf-step"><div class="wf-top"><span class="wf-num">11</span><span class="wf-title">Insights Module</span></div><div class="muted">Feature impact explanation</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()
st.caption("Built for Lahore Real Estate Intelligence • Streamlit UI Dashboard")
