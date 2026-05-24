# =========================
# IMPORTS
# =========================
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from pathlib import Path

from sklearn.linear_model import Ridge

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Insights Module",
    layout="wide"
)

st.title("📊 Property Insights Module")

# =========================
# LOAD DATA
# =========================
BASE_DIR = Path(__file__).resolve().parents[2]
df = joblib.load(BASE_DIR / "artifacts" / "models" / "houses_df.pkl")

# =========================
# FEATURES
# =========================
feature_cols = [

    'bedrooms',
    'baths',
    'area_sqft',
    'kitchens',
    'store_rooms',
    'is_gym',
    'agePossession',
    'is_servant_room',
    'luxury_category',
    'floor_category',
    'furnishing_type'
]

# =========================
# X and y
# =========================
X = df[feature_cols]

y = df['price']

# =========================
# ONE HOT ENCODING
# =========================
X = pd.get_dummies(

    X,

    drop_first=True
)

# =========================
# TRAIN RIDGE MODEL
# =========================
ridge = Ridge(alpha=1.0)

ridge.fit(X, y)

# =========================
# COEFFICIENT DATAFRAME
# =========================
coef_df = pd.DataFrame({

    'Feature': X.columns,

    'Coefficient': ridge.coef_

})

# =========================
# PERCENT IMPACT
# =========================
coef_df['Percent_Impact'] = (
    coef_df['Coefficient'] * 100
)

# =========================
# SORT FEATURES
# =========================
coef_df = coef_df.sort_values(
    by='Percent_Impact',
    ascending=False
)

# =========================
# HEADER
# =========================
st.subheader("📋 Feature Importance Table")

# =========================
# SHOW TABLE
# =========================
st.dataframe(
    coef_df,
    use_container_width=True
)

# =========================
# FEATURE SELECTOR
# =========================
selected_feature = st.selectbox(

    "🔍 Select Feature",

    coef_df['Feature'].tolist()
)

# =========================
# GET IMPACT
# =========================
impact = coef_df[
    coef_df['Feature'] == selected_feature
]['Percent_Impact'].values[0]

# =========================
# INSIGHT SECTION
# =========================
st.subheader("💡 Feature Insight")

# clean feature name
clean_name = selected_feature.replace('_', ' ')

if impact > 0:

    st.success(
        f"✅ {clean_name} increases property price by approximately {impact:.2f}%"
    )

else:

    st.error(
        f"📉 {clean_name} decreases property price by approximately {abs(impact):.2f}%"
    )

# =========================
# TOP POSITIVE FEATURES
# =========================
st.subheader("🚀 Top Price Increasing Features")

top_positive = coef_df.head(5)

st.dataframe(
    top_positive,
    use_container_width=True
)

# =========================
# TOP NEGATIVE FEATURES
# =========================
st.subheader("📉 Top Price Decreasing Features")

top_negative = coef_df.tail(5)

st.dataframe(
    top_negative,
    use_container_width=True
)

# =========================
# BAR CHART
# =========================
st.subheader("📈 Feature Impact Visualization")

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(
    coef_df['Feature'],
    coef_df['Percent_Impact']
)

ax.set_xlabel("Percent Impact")

ax.set_ylabel("Features")

ax.set_title("Feature Importance Analysis")

plt.tight_layout()

st.pyplot(fig)

# =========================
# SUMMARY
# =========================
st.subheader("📝 Model Summary")

st.info(
    """
    This module explains how different property features 
    influence house prices using Ridge Regression.

    Positive values increase property prices.
    Negative values decrease property prices.
    """
)
