import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Sectoral Impact Analysis of COVID-19 in the UK', page_icon=':chart_with_upwards_trend:', layout='wide')

# App Title
st.title(":chart_with_upwards_trend: Sectoral Impact Analysis of COVID-19 in the UK")
st.markdown("Upload your dataset and explore time-based trends for different sectors and themes.")

# --- Upload CSV ---
uploaded_file = st.file_uploader(":file_folder: Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader(":receipt: Preview of Uploaded Data")
    st.dataframe(df.head())

    # --- Column Detection ---
    all_columns = df.columns.tolist()

    date_col = st.selectbox(":calendar: Select the Date column", all_columns)
    value_columns = st.multiselect(":bar_chart: Select Value Metric(s) to Explore", [col for col in all_columns if col != date_col])

    chart_type = st.selectbox(":bar_chart: Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])

    # --- Chart Plotting ---
    st.subheader(":chart_with_upwards_trend: Visualisation")

    for val_col in value_columns:
        if chart_type == "Line Chart":
            fig = px.line(df, x=date_col, y=val_col, markers=True, title=f"{val_col} Over Time")
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x=date_col, y=val_col, title=f"{val_col} Over Time")
        else:
            fig = px.area(df, x=date_col, y=val_col, title=f"{val_col} Over Time")

        fig.update_layout(xaxis_title='Date', yaxis_title=val_col)
        st.plotly_chart(fig, use_container_width=True)

    # --- Time Series Analysis ---
    if st.checkbox(":brain: Show Timeseries Breakdown"):
        st.markdown("### :chart_with_downwards_trend: Detailed Timeseries Analysis")
        melted = df.melt(id_vars=[date_col], value_vars=value_columns,
                         var_name="Metric", value_name="Value")
        ts_fig = px.line(melted, x=date_col, y="Value", color="Metric", title="Timeseries by Metric")
        st.plotly_chart(ts_fig, use_container_width=True)

    # --- Insight Box (manual entry) ---
    st.markdown("### :writing_hand: Add Observations or Insights")
    insight = st.text_area("Write your insights based on the chart above...")
    if insight:
        st.success(":memo: Insight saved!")
        st.write(insight)

else:
    st.info(":leftwards_arrow_with_hook: Please upload a CSV file to get started.")
