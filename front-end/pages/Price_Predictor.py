# -------------------- IMPORTS --------------------
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

st.set_page_config(page_title="Price Predictor", layout="wide")

st.title("🏠 Property Price Predictor")

# -------------------- PROPERTY TYPE --------------------
property_choice = st.selectbox(
    "Select Property Type",
    ["Flat", "House"]
)

# =========================================================
# ======================= FLATS ===========================
# =========================================================

if property_choice == "Flat":

    df = joblib.load(BASE_DIR / "artifacts" / "models" / "flats_df.pkl")
    model = joblib.load(BASE_DIR / "artifacts" / "models" / "flats_final_pipeline.pkl")

    st.header("Enter Flat Details")

    bedrooms = float(
        st.selectbox(
            'Bedrooms',
            sorted(df['bedrooms'].dropna().unique())
        )
    )

    baths = float(
        st.selectbox(
            'Bathrooms',
            sorted(df['baths'].dropna().unique())
        )
    )

    floors_in_building = float(
        st.selectbox(
            'Floors in Building',
            sorted(df['floors_in_building'].dropna().unique())
        )
    )

    area_sqft = float(
        st.number_input(
            'Area (sqft)',
            min_value=100.0
        )
    )

    servant_quarters = float(
        st.selectbox(
            'Servant Quarters',
            [0.0, 1.0]
        )
    )

    kitchens = float(
        st.selectbox(
            'Kitchens',
            sorted(df['kitchens'].dropna().unique())
        )
    )

    store_rooms = float(
        st.selectbox(
            'Store Rooms',
            sorted(df['store_rooms'].dropna().unique())
        )
    )

    drawing_room = int(
        st.selectbox(
            'Drawing Room',
            [0, 1]
        )
    )

    agePossession = st.selectbox(
        'Property Age',
        sorted(df['agePossession'].dropna().unique())
    )

    luxury_category = st.selectbox(
        'Luxury Category',
        sorted(df['luxury_category'].dropna().unique())
    )

    floor_category = st.selectbox(
        'Floor Category',
        sorted(df['floor_category'].dropna().unique())
    )

    furnishing_type = st.selectbox(
        'Furnishing Type',
        sorted(df['furnishing_type'].dropna().unique())
    )

    # -------------------- PREDICT --------------------
    if st.button("Predict Flat Price"):

        data = [[
            bedrooms,
            baths,
            floors_in_building,
            area_sqft,
            servant_quarters,
            kitchens,
            store_rooms,
            drawing_room,
            agePossession,
            luxury_category,
            floor_category,
            furnishing_type
        ]]

        columns = [
            'bedrooms',
            'baths',
            'floors_in_building',
            'area_sqft',
            'servant_quarters',
            'kitchens',
            'store_rooms',
            'drawing_room',
            'agePossession',
            'luxury_category',
            'floor_category',
            'furnishing_type'
        ]

        one_df = pd.DataFrame(
            data,
            columns=columns
        )

        pred_log = model.predict(one_df)

        pred = np.expm1(pred_log)[0]
        
        margin = pred * 0.10
        low = pred - margin

        high = pred + margin
        
        

        st.success(
            f"Estimated Flat Price: {round(pred,2)} Cr 💰"
        )
        
        st.success(
            f"Estimated Price Range: {low:.2f} Cr - {high:.2f} Cr"
        )

# =========================================================
# ======================= HOUSES ==========================
# =========================================================

else:

    df = joblib.load(BASE_DIR / "artifacts" / "models" / "houses_df.pkl")
    model = joblib.load(BASE_DIR / "artifacts" / "models" / "house_pipeline.pkl")

    st.header("Enter House Details")

    bedrooms = float(
        st.selectbox(
            'Bedrooms',
            sorted(df['bedrooms'].dropna().unique())
        )
    )

    baths = float(
        st.selectbox(
            'Bathrooms',
            sorted(df['baths'].dropna().unique())
        )
    )

    area_sqft = float(
        st.number_input(
            'Area (sqft)',
            min_value=100.0
        )
    )

    kitchens = float(
        st.selectbox(
            'Kitchens',
            sorted(df['kitchens'].dropna().unique())
        )
    )

    store_rooms = float(
        st.selectbox(
            'Store Rooms',
            sorted(df['store_rooms'].dropna().unique())
        )
    )

    is_gym = int(
        st.selectbox(
            'Gym',
            [0, 1]
        )
    )

    agePossession = st.selectbox(
        'Property Age',
        sorted(df['agePossession'].dropna().unique())
    )

    is_servant_room = int(
        st.selectbox(
            'Servant Room',
            [0, 1]
        )
    )

    luxury_category = st.selectbox(
        'Luxury Category',
        sorted(df['luxury_category'].dropna().unique())
    )

    floor_category = st.selectbox(
        'Floor Category',
        sorted(df['floor_category'].dropna().unique())
    )

    furnishing_type = st.selectbox(
        'Furnishing Type',
        sorted(df['furnishing_type'].dropna().unique())
    )

    # -------------------- PREDICT --------------------
    if st.button("Predict House Price"):

        data = [[
            bedrooms,
            baths,
            area_sqft,
            kitchens,
            store_rooms,
            is_gym,
            agePossession,
            is_servant_room,
            luxury_category,
            floor_category,
            furnishing_type
        ]]

        columns = [
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

        one_df = pd.DataFrame(
            data,
            columns=columns
        )

        pred_log = model.predict(one_df)

        pred = np.expm1(pred_log)[0]
        
        margin = pred * 0.10
        low = pred - margin

        high = pred + margin
        
        st.success(
            f"Estimated House Price: {round(pred,2)} Cr 💰"
        )
        
        st.success(
            f"Estimated Price Range: {low:.2f} Cr - {high:.2f} Cr"
        )
