import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Visualizing Multiple Variables")

# ----------------------------
# Sample Dataset
# ----------------------------
np.random.seed(0)
df = pd.DataFrame({
    "Study_Hours": np.random.randint(1, 10, 200),
    "Sleep_Hours": np.random.randint(4, 9, 200),
    "Score": np.random.randint(40, 100, 200),
    "Gender": np.random.choice(["Male", "Female"], 200),
    "Department": np.random.choice(["CS", "EE", "ME"], 200)
})

tabs = st.tabs([
    "3D Scatter Plot",
    "Bar Chart with Hue",
    "Facet Grids",
    "Pair Plots",
    "Bubble Charts"
])

# ==================================================
# 1️⃣ 3D SCATTER PLOT
# ==================================================
with tabs[0]:
    st.header("🔵 3D Scatter Plot")

    fig = px.scatter_3d(
        df,
        x="Study_Hours",
        y="Sleep_Hours",
        z="Score",
        color="Gender",
        title="Study vs Sleep vs Score"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **What it solves**
    - Shows relationship among **3 numerical variables**
    - Rotation helps spot clusters and trends
    """)

# ==================================================
# 2️⃣ BAR CHART WITH HUE
# ==================================================
with tabs[1]:
    st.header("📊 Bar Chart with Hue")

    grouped = df.groupby(["Department", "Gender"])["Score"].mean().reset_index()

    fig = px.bar(
        grouped,
        x="Department",
        y="Score",
        color="Gender",
        barmode="group",
        title="Average Score by Department & Gender"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **What it solves**
    - Compare **categories inside categories**
    - Hue = second categorical variable
    """)

# ==================================================
# 3️⃣ FACET GRIDS (Small Multiples)
# ==================================================
with tabs[2]:
    st.header("🧩 Facet Grids (Small Multiples)")

    fig = px.scatter(
        df,
        x="Study_Hours",
        y="Score",
        facet_col="Department",
        color="Gender",
        title="Study vs Score across Departments"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **What it solves**
    - Same relationship repeated across groups
    - Easy comparison without clutter
    """)

# ==================================================
# 4️⃣ PAIR PLOTS (Scatter Matrix)
# ==================================================
with tabs[3]:
    st.header("🔗 Pair Plots (Scatter Matrix)")

    fig = px.scatter_matrix(
        df,
        dimensions=["Study_Hours", "Sleep_Hours", "Score"],
        color="Gender",
        title="Pairwise Relationships"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **What it solves**
    - Shows **all 2-variable relationships at once**
    - Diagonal = distributions
    - Great for feature selection
    """)

# ==================================================
# 5️⃣ BUBBLE CHARTS
# ==================================================
with tabs[4]:
    st.header("🫧 Bubble Charts")

    fig = px.scatter(
        df,
        x="Study_Hours",
        y="Score",
        size="Sleep_Hours",
        color="Department",
        title="Bubble Chart: 4 Variables",
        size_max=10
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **What it solves**
    - X & Y → numerical variables
    - Bubble size → magnitude
    - Color → category
    """)

st.success("🎉 You just visualized up to **4 variables at once!**")
