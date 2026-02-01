import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from scipy.stats import norm
import streamlit_mermaid as stmd

st.set_page_config(layout="wide")
st.title("🎯 Probability & Distributions – Visual Playground")

tabs = st.tabs([
    "Random Variables",
    "PMF (Die)",
    "CDF of PMF",
    "PDF (Height)",
    "Density Estimation",
    "CDF of PDF"
])

# ======================================================
# 1️⃣ RANDOM VARIABLES
# ======================================================
with tabs[0]:
    st.header("🎲 Random, Algebraic & Probability Variables")

    st.markdown("""
    **Algebraic Variable**
    - Fixed value
    - No randomness

    **Random Variable**
    - Outcome of experiment → number

    **Probability Variable**
    - Random variable + probability
    """)

    outcomes = [1, 2, 3, 4, 5, 6]
    probs = [1/6] * 6

    df = pd.DataFrame({
        "Outcome (Ω)": outcomes,
        "Random Variable X": outcomes,
        "P(X)": probs
    })

    st.dataframe(df)

    mind_map_chart = """
    flowchart TD
        A[Random Variable] --> B[Probability Distribution]

        B --> C[Discrete Random Variable]
        B --> D[Continuous Random Variable]

        C --> E[Probability Mass Function]
        E --> F[Cumulative Distribution Function]

        D --> G[Probability Density Function]
        G --> H[Cumulative Distribution Function]

        G --> I[Density Estimation]

        I --> J[Parametric Density Estimation]
        I --> K[Non Parametric Density Estimation]

        K --> L[Kernel Density Estimation]
        K --> HE[histogram Estimation]
        K --> GMM[Gaussian mixture models GMMs]
        """
    stmd.st_mermaid(mind_map_chart)
    
# ======================================================
# 2️⃣ PMF – DIE
# ======================================================
with tabs[1]:
    st.header("📌 Probability Mass Function (PMF)")

    st.markdown("""
    **Why PMF exists**
    - Discrete outcomes
    - Probabilities must sum to 1
    """)

    df_pmf = pd.DataFrame({
        "x": outcomes,
        "P(X=x)": probs
    })

    fig = px.bar(df_pmf, x="x", y="P(X=x)", title="PMF of Fair Die")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Set Format**
    ```
    X = {1, 2, 3, 4, 5, 6}
    P(X=x) = 1/6
    ```
    """)

# ======================================================
# 3️⃣ CDF OF PMF
# ======================================================
with tabs[2]:
    st.header("📈 CDF of PMF")

    df_pmf["CDF"] = np.cumsum(df_pmf["P(X=x)"])

    fig = px.line(
        df_pmf, 
        x="x", 
        y="CDF", 
        title="CDF of Die Roll", 
        markers=True,
        labels={"x": "Die Roll", "CDF": "Cumulative Probability"}
    )
    fig.update_traces(line_shape='hv')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Meaning**
    ```
    F(x) = P(X ≤ x)
    ```
    Step shape → because data is discrete.
    """)

# ======================================================
# 4️⃣ PDF – CONTINUOUS VARIABLE
# ======================================================
with tabs[3]:
    st.header("📏 Probability Density Function (PDF)")

    mu = st.slider("Mean height (cm)", 150, 180, 170)
    sigma = st.slider("Std Dev", 5, 20, 8)

    x = np.linspace(140, 200, 400)
    y = norm.pdf(x, mu, sigma)

    fig = px.line(x=x, y=y, labels={"x": "Height", "y": "Density"},
                  title="PDF of Human Height")

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Key idea**
    - PDF value ≠ probability
    - Area under curve = probability
    """)

# ======================================================
# 5️⃣ DENSITY ESTIMATION
# ======================================================
with tabs[4]:
    st.header("🌊 Density Estimation")

    st.markdown("""
    **What is Density Estimation?**
    - Estimate unknown distribution from data

    **Why needed?**
    - Real data does NOT come with formula
    """)

    data = np.random.normal(170, 8, 300)

    fig = px.histogram(
        data,
        nbins=30,
        histnorm="probability density",
        title="Histogram (Non-parametric)"
    )

    fig.add_scatter(
        x=x,
        y=norm.pdf(x, np.mean(data), np.std(data)),
        mode="lines",
        name="Parametric (Normal)"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Types**
    - Parametric → assume normal
    - Non-parametric → KDE (data-driven)
    """)

# ======================================================
# 6️⃣ CDF OF PDF
# ======================================================
with tabs[5]:
    st.header("📈 CDF of PDF")

    cdf = norm.cdf(x, mu, sigma)

    fig = px.line(
        x=x,
        y=cdf,
        labels={"x": "Height", "y": "P(X ≤ x)"},
        title="CDF of Height"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Meaning**
    - Smooth curve
    - No steps (continuous)
    """)

st.success("🎉 You now understand probability visually & intuitively!")
