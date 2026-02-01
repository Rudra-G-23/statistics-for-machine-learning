import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from collections import Counter

st.set_page_config(page_title="Stats Playground", layout="wide")

st.title("📊 Statistics Playground")
st.write("Learn statistics by **playing with data** 🎮")

# -------------------- TABS --------------------
tabs = st.tabs([
    "Types of Data",
    "Central Tendency",
    "Dispersion",
    "Univariate Analysis",
    "Bivariate Analysis"
])

# =========================
# 1️⃣ TYPES OF DATA
# =========================
with tabs[0]:
    st.header("📂 Types of Data")

    st.subheader("Categorical Data")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Nominal Data (No Order)")
        fruits = ["Apple", "Banana", "Mango", "Apple", "Mango", "Apple"]
        df_nominal = pd.DataFrame({"Fruit": fruits})
        fig = px.histogram(df_nominal, x="Fruit", title="Favorite Fruits")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("### Ordinal Data (Order Exists)")
        ratings = ["Poor", "Average", "Good", "Excellent", "Good", "Average"]
        df_ordinal = pd.DataFrame({"Rating": ratings})
        fig = px.histogram(df_ordinal, x="Rating", title="Customer Ratings")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Numerical Data")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### Discrete Data (Countable)")
        dice = np.random.randint(1, 7, 50)
        fig = px.histogram(dice, title="Dice Rolls")
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.markdown("### Continuous Data (Measurable)")
        heights = np.random.normal(170, 8, 200)
        fig = px.histogram(heights, title="Heights Distribution")
        st.plotly_chart(fig, use_container_width=True)

# =========================
# 2️⃣ CENTRAL TENDENCY
# =========================
with tabs[1]:
    st.header("📐 Measures of Central Tendency")

    data = st.slider("Choose number of values", 10, 200, 50)
    values = np.random.normal(50, 10, data)

    mean = np.mean(values)
    median = np.median(values)
    mode = Counter(np.round(values)).most_common(1)[0][0]

    fig = px.histogram(values, nbins=30, title="Distribution")
    fig.add_vline(x=mean, line_dash="dash", annotation_text="Mean")
    fig.add_vline(x=median, line_dash="dot", annotation_text="Median")

    st.plotly_chart(fig, use_container_width=True)

    st.metric("Mean", round(mean, 2))
    st.metric("Median", round(median, 2))
    st.metric("Mode", mode)

    st.subheader("Weighted Mean Example")
    scores = [80, 70, 90]
    weights = [0.5, 0.3, 0.2]
    weighted_mean = np.average(scores, weights=weights)
    st.write("Scores:", scores)
    st.write("Weights:", weights)
    st.success(f"Weighted Mean = {weighted_mean}")

# =========================
# 3️⃣ DISPERSION
# =========================
with tabs[2]:
    st.header("📊 Measure of Dispersion")

    values = np.random.normal(100, 20, 100)

    range_val = np.max(values) - np.min(values)
    variance = np.var(values)
    std_dev = np.std(values)
    cv = (std_dev / np.mean(values)) * 100

    fig = px.box(values, title="Spread of Data")
    st.plotly_chart(fig, use_container_width=True)

    st.write(f"Range: {range_val:.2f}")
    st.write(f"Variance: {variance:.2f}")
    st.write(f"Standard Deviation: {std_dev:.2f}")
    st.write(f"Coefficient of Variation: {cv:.2f}%")

# =========================
# 4️⃣ UNIVARIATE ANALYSIS
# =========================
with tabs[3]:
    st.header("📈 Univariate Analysis")

    st.subheader("Categorical Data – Frequency Table")
    categories = ["A", "B", "C", "A", "B", "A"]
    freq = pd.DataFrame(pd.Series(categories).value_counts()).reset_index()
    freq.columns = ["Category", "Frequency"]
    st.dataframe(freq)

    fig = px.bar(freq, x="Category", y="Frequency", title="Frequency Bar Chart")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Numerical Data – Histogram")
    data = np.random.normal(60, 12, 200)
    fig = px.histogram(data, nbins=25)
    st.plotly_chart(fig, use_container_width=True)

# =========================
# 5️⃣ BIVARIATE ANALYSIS
# =========================
with tabs[4]:
    st.header("🔗 Bivariate Analysis")

    st.subheader("Categorical vs Categorical")
    gender = ["Male", "Female", "Male", "Female", "Male"]
    choice = ["Yes", "No", "Yes", "Yes", "No"]
    df = pd.DataFrame({"Gender": gender, "Choice": choice})
    fig = px.histogram(df, x="Gender", color="Choice", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Numerical vs Numerical")
    x = np.random.normal(50, 10, 100)
    y = x * 1.5 + np.random.normal(0, 10, 100)
    fig = px.scatter(x=x, y=y, labels={"x": "Study Hours", "y": "Score"})
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Numerical vs Categorical")
    category = ["A", "B", "C"]
    values = np.random.randn(300)
    cats = np.random.choice(category, 300)
    df = pd.DataFrame({"Category": cats, "Value": values})
    fig = px.box(df, x="Category", y="Value")
    st.plotly_chart(fig, use_container_width=True)

st.success("🎉 You just explored statistics interactively!")
