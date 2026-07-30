import streamlit as st
import pandas as pd

from analysis.kpi import calculate_kpis
from analysis.country_analysis import country_analysis
from analysis.operator_analysis import operator_analysis

from reports.report_builder import generate_report

from ai.prompt_builder import build_prompt
from ai.ai_engine import generate_summary

st.set_page_config(
    page_title="Telecom AI Traffic Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Telecom AI Traffic Analyzer")

uploaded_file = st.file_uploader(
    "Upload Telecom Log",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    filtered_df = df.copy()

    #Date Filter
    selected_date = st.selectbox(
    "📅 Select Date",
    ["All"] + sorted(df["date"].unique().tolist())
    )


    # Country Filter

    selected_country = st.selectbox(
    "🌍 Select Country",
    ["All"] + sorted(df["country"].unique().tolist())
    )

    if selected_country != "All":
        filtered_df = filtered_df[
        filtered_df["country"] == selected_country
    ]

    # Operator Filter

    selected_operator = st.selectbox(
    "📡 Select Operator",
    ["All"] + sorted(df["operator"].unique().tolist())
    )

    if selected_operator != "All":
        filtered_df = filtered_df[
        filtered_df["operator"] == selected_operator
    ]


    #overall = calculate_kpis(df)
    #country = country_analysis(df)
    #operator = operator_analysis(df)


    overall = calculate_kpis(filtered_df)
    country = country_analysis(filtered_df)
    operator = operator_analysis(filtered_df)



    # KPI
    st.header("📈 Overall KPI")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Traffic", overall["total"])
    col2.metric("Delivered", overall["delivered"])
    col3.metric("Failed", overall["failed"])
    col4.metric(
        "Delivery %",
        f'{overall["delivered_percentage"]:.2%}'
    )

    st.divider()

    # Country
    st.header("🌍 Country Summary")

    st.dataframe(
        country["country_summary"],
        use_container_width=True
    )

    #Top countries.
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌍 Top Countries")
        st.dataframe(country["top_traffic"])

    with col2:
        st.subheader("📊 Country Traffic")
        st.bar_chart(
            country["top_traffic"].set_index("country")["total_traffic"]
    )

    st.divider()

    # Operator
    st.header("📡 Operator Summary")

    st.dataframe(
        operator["operator_summary"],
        use_container_width=True
    )

# ==============================
# AI Executive Summary
# ==============================

st.divider()

st.subheader("🤖 AI Executive Summary")

if st.button("Generate AI Summary"):

    with st.spinner("Generating AI Summary..."):

        try:

            # Step 1 - Generate Report
            report = generate_report(
                overall,
                country,
                operator
            )

            # Step 2 - Build Prompt
            prompt = build_prompt(report)

            # Step 3 - Generate AI Summary
            ai_report = generate_summary(prompt)

            st.success("AI Summary Generated Successfully!")

            st.markdown(ai_report)

        except Exception as e:

            st.error(f"AI generation failed: {e}")