import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration:
st.set_page_config(
    page_title='Sectoral Impact Analysis of COVID-19 Pandemic in the UK',
    page_icon=':chart_with_upwards_trend:',
    layout='wide'
)

# Sidebar Navigation:
st.sidebar.title(":compass: Navigation")
section = st.sidebar.radio(":arrow_right: Go to", ["Dashboard", "Add Insights"])

# File uploader
uploaded_file = st.sidebar.file_uploader(":file_folder: Upload your CSV file", type=["csv"])

# When file is uploaded...
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    all_columns = df.columns.tolist()

    if section == "Dashboard":
        st.title(":chart_with_upwards_trend: Sectoral Impact Analysis of COVID-19 in the UK")
        st.markdown("Explore time-based trends for different sectors and themes.")

        st.subheader(":receipt: Preview of Uploaded Data")
        st.dataframe(df.head())

        # Column selectors:
        date_col = st.selectbox(":calendar: Select the Date column", all_columns)

        # Convert and sort date:
        df[date_col] = pd.to_datetime(df[date_col], dayfirst=True, errors='coerce')
        df = df.dropna(subset=[date_col])
        df = df.sort_values(by=date_col)

        value_columns = st.multiselect(
            ":bar_chart: Select Value Metric(s) to Explore",
            [col for col in all_columns if col != date_col]
        )

        if value_columns:
            chart_type = st.selectbox(":chart_with_upwards_trend: Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])

            # Date Summary:
            st.markdown("### :calendar: Date Range")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(":calendar: Start Date", df[date_col].min().strftime("%d/%m/%Y"))
            with col2:
                st.metric(":calendar: End Date", df[date_col].max().strftime("%d/%m/%Y"))

            # Chart section:
            st.markdown("### :bar_chart: Trend Visualisation")
            for val_col in value_columns:
                if chart_type == "Line Chart":
                    fig = px.line(df, x=date_col, y=val_col, markers=True, title=f"{val_col} Over Time")
                elif chart_type == "Bar Chart":
                    fig = px.bar(df, x=date_col, y=val_col, title=f"{val_col} Over Time")
                else:
                    fig = px.area(df, x=date_col, y=val_col, title=f"{val_col} Over Time")

                fig.update_layout(
                    xaxis_title='Date',
                    yaxis_title=val_col,
                    title_font_size=18,
                    font=dict(size=14),
                    plot_bgcolor="#f9f9f9",
                    paper_bgcolor="#f9f9f9"
                )
                st.plotly_chart(fig, use_container_width=True)

            # Timeseries expander:
            with st.expander(":mag_right: Click to View Combined Timeseries"):
                st.markdown("### :bar_chart: Detailed Timeseries Analysis")
                melted = df.melt(id_vars=[date_col], value_vars=value_columns,
                                 var_name="Metric", value_name="Value")
                ts_fig = px.line(melted, x=date_col, y="Value", color="Metric", title="Timeseries by Metric")
                ts_fig.update_layout(plot_bgcolor="#f9f9f9", paper_bgcolor="#f9f9f9")
                st.plotly_chart(ts_fig, use_container_width=True)

            # Download:
            @st.cache_data
            def convert_df(dataframe):
                return dataframe.to_csv(index=False).encode('utf-8')

            csv = convert_df(df)
            st.download_button(":arrow_down: Download Processed Data", csv, "sector_analysis.csv", "text/csv")

        else:
            st.warning(":warning: Please select at least one metric column to visualize.")

    elif section == "Add Insights":
        st.title(":memo: Observations and Insights")
        st.markdown("Write your observations or insights based on your visual analysis.")
        insight = st.text_area(":pencil: What patterns or takeaways do you see from the charts above?")

        if insight:
            st.success(":white_check_mark: Insight saved!")
            st.write(insight)

else:
    st.info(":leftwards_arrow_with_hook: Please upload a CSV file from the sidebar to get started.")
