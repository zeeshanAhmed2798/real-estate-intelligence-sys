import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

st.set_page_config(page_title="Recommender System")

st.title("🏡 Society Recommender System")

# ---------------- LOAD FILES ----------------
BASE_DIR = Path(__file__).resolve().parents[2]
cosine_sim1 = pickle.load(open(BASE_DIR / "artifacts" / "recommender" / "cosine_sim1.pkl", 'rb'))
cosine_sim2 = pickle.load(open(BASE_DIR / "artifacts" / "recommender" / "cosine_sim2.pkl", 'rb'))

society_df = pickle.load(open(BASE_DIR / "artifacts" / "recommender" / "society_df.pkl", 'rb'))

# ---------------- RECOMMENDER FUNCTION ----------------
def recommend_societies_with_scores(society_name, top_n=5):

    # weighted similarity
    cosine_sim_matrix = (5 * cosine_sim1) + (3 * cosine_sim2)

    # index
    idx = society_df[
        society_df['Society'] == society_name
    ].index[0]

    # scores
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))

    # sort
    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # top 5
    sim_scores = sim_scores[1:top_n+1]

    # indices
    society_indices = [i[0] for i in sim_scores]

    # dataframe
    recommendations_df = pd.DataFrame({
        'Recommended Society':
        society_df['Society'].iloc[society_indices].values,

        'Similarity Score':
        [round(i[1], 3) for i in sim_scores]
    })

    return recommendations_df


# ---------------- UI ----------------
selected_society = st.selectbox(
    "Select Society",
    sorted(society_df['Society'].unique())
)

# ---------------- BUTTON ----------------
if st.button("Recommend"):

    recommendations = recommend_societies_with_scores(
        selected_society
    )

    st.subheader("🏘 Similar Societies")

    st.dataframe(
        recommendations,
        use_container_width=True
    )
