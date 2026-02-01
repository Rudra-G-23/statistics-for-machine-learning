import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("📊 Statistics Visual Playground")

# -------------------------------
# Generate Base Data
# -------------------------------
np.random.seed(42)
data = np.random.normal(50, 10, 200)

# -------------------------------
# TABS
# -------------------------------
tabs = st.tabs([
    "Quantile & Percentile",
    "5 Number Summary",
    "Box Plots",
    "Scatter, Covariance & Correlation",
    "Correlation vs Causation"
])

# ======================================================
# 1️⃣ QUANTILE & PERCENTILE
# ======================================================
with tabs[0]:
    st.header("📌 Quantile & Percentile")

    q = st.slider("Choose Percentile", 1, 99, 50)
    value = np.percentile(data, q)

    fig = px.histogram(data, nbins=30, title="Distribution")
    fig.add_vline(x=value, line_dash="dash",
                  annotation_text=f"{q}th Percentile")

    st.plotly_chart(fig, use_container_width=True)

    st.info(
        f"""
        **Meaning:**  
        {q}th percentile = {value:.2f}  
        👉 {q}% of data lies **below** this value.
        """
    )

# ======================================================
# 2️⃣ FIVE NUMBER SUMMARY + STEPS
# ======================================================
with tabs[1]:
    st.header("📌 Five Number Summary")

    minimum = np.min(data)
    q1 = np.percentile(data, 25)
    median = np.percentile(data, 50)
    q3 = np.percentile(data, 75)
    maximum = np.max(data)

    summary = pd.DataFrame({
        "Metric": ["Min", "Q1", "Median", "Q3", "Max"],
        "Value": [minimum, q1, median, q3, maximum]
    })

    st.dataframe(summary)

    fig = px.box(data, title="Five Number Summary Visual")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Step-by-step intuition:**
    1. Sort the data  
    2. Find middle → Median  
    3. Left middle → Q1  
    4. Right middle → Q3  
    5. Ends → Min & Max  
    """)

# ======================================================
# 3️⃣ BOX PLOTS
# ======================================================
with tabs[2]:
    st.header("📦 Box Plots")

    st.subheader("Single Box Plot")
    fig = px.box(data)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Side-by-Side Box Plot")

    group = np.random.choice(["Group A", "Group B"], 200)
    df = pd.DataFrame({"Value": data, "Group": group})

    fig = px.box(df, x="Group", y="Value", color="Group")
    st.plotly_chart(fig, use_container_width=True)

    st.info("""
    **Why box plots are powerful**
    - Detect outliers
    - Compare distributions
    - See spread + symmetry
    """)

# ======================================================
# 4️⃣ SCATTER, COVARIANCE & CORRELATION
# ======================================================
with tabs[3]:
    st.header("🔗 Scatter, Covariance & Correlation")

    relation = st.selectbox(
        "Choose Relationship",
        ["Positive", "Negative", "No relationship"]
    )

    if relation == "Positive":
        x = np.arange(100)
        y = x + np.random.normal(0, 10, 100)
    elif relation == "Negative":
        x = np.arange(100)
        y = -x + np.random.normal(0, 10, 100)
    else:
        x = np.random.rand(100)
        y = np.random.rand(100)

    df = pd.DataFrame({"X": x, "Y": y})

    cov = np.cov(x, y)[0][1]
    corr = np.corrcoef(x, y)[0][1]

    fig = px.scatter(df, x="X", y="Y", title="Scatter Plot")
    st.plotly_chart(fig, use_container_width=True)

    table = pd.DataFrame({
        "Measure": ["Covariance", "Correlation"],
        "Value": [cov, corr]
    })

    st.dataframe(table)

    st.markdown("""
    ### 📌 Covariance
    | Sign | Meaning |
    |-----|--------|
    | + | X ↑ → Y ↑ |
    | − | X ↑ → Y ↓ |
    | 0 | No linear relation |

    **Problem:** magnitude depends on units ❌

    ### 📌 Correlation
    - Range: **-1 to +1**
    - Unit-free ✅
    """)

# ======================================================
# 5️⃣ CORRELATION VS CAUSATION
# ======================================================
with tabs[4]:
    st.header("⚠️ Correlation ≠ Causation")

    ice_cream = np.random.randint(10, 100, 100)
    drowning = ice_cream + np.random.normal(0, 10, 100)

    df = pd.DataFrame({
        "Ice Cream Sales": ice_cream,
        "Drowning Incidents": drowning
    })

    fig = px.scatter(df, x="Ice Cream Sales", y="Drowning Incidents")
    st.plotly_chart(fig, use_container_width=True)

    st.warning("""
    **They are correlated ❗  
    But ice cream does NOT cause drowning.**

    👉 Hidden variable: **Summer / Temperature**
    """)

    st.success("""
    **Golden Rule**
    - Correlation → pattern
    - Causation → mechanism + experiment
    """)

