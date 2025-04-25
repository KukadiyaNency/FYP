import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns 
import matplotlib.pyplot as plt 
from PIL import Image
import os
import io

# Set page config
st.set_page_config(page_title="Business Impact Dashboard", page_icon=":bar_chart:", layout="wide")

# Sidebar navigation
st.sidebar.title(":blue_book: Navigation")
page = st.sidebar.radio("Go to", [
    ":open_book: Introduction",
    ":bar_chart: Sector Insights",
    ":test_tube: Hypothesis Testing",
    ":bulb: Key Takeaways",
    ":control_knobs: Interactive Dashboard",
    ":pushpin: Conclusion"
])

# -------------------------
# Page 1: Introduction
# -------------------------
def introduction_page():
    st.title(":open_book: Introduction")
    st.write("""
    This project explores the **impact of unforeseen events, specifically the COVID-19 pandemic**, on the business landscape in the UK.
    It focuses on five key sectors:
    - :hotel: Accommodation and Food Service Activities (Hospitality)
    - :shopping_bags: Wholesale and Retail Trade (Retail)
    - :factory: Manufacturing
    - :truck: Transportation and Storage
    - :computer: Information and Communication
    """)

    st.header(":round_pushpin: Context and Importance")
    st.write("""
    The COVID-19 pandemic disrupted industries worldwide. Businesses faced challenges in maintaining financial performance,
    retaining employees, managing trade operations, and adapting strategically to ongoing uncertainty.

    This analysis provides a deeper understanding of **how sectors responded and recovered**, offering valuable insights into
    **resilience and adaptability** in times of crisis.
    """)

    st.header(":dart: Project Objectives")
    st.markdown("""
    The key objectives of this analysis are to:

    - :chart_with_downwards_trend: Examine **financial performance** changes across sectors during the pandemic.
    - :busts_in_silhouette: Analyse **workforce dynamics**, including furlough rates and employment changes.
    - :package: Evaluate **trade variations**, focusing on import/export challenges.
    - :gear: Explore **strategic adaptations**, such as the role of government schemes and business responses.
    """)

# -------------------------
# Page 2: Sector Insights
# -------------------------

def sector_insights_page():
    st.title(":bar_chart: Sector Insights")
    st.write("This section will show visual comparisons across variables and sectors.")

    # Set the folder path for your images
    image_folder = "Images_Data"

    # Dictionary of sectoral themes and filenames
    sector_images = {
        "Hospitality - Financial": "HF.png",
        "Hospitality - Import": "HI.png",
        "Hospitality - Workforce": "HW.png",
        "Hospitality - Strategic": "HS.png",
        "Information - Financial": "IF.png",
        "Information - Export": "IE.png",
        "Information - Import": "II.png",
        "Information - Workforce": "IW.png",
        "Information - Strategic": "IS.png",
        "Manufacturing - Financial": "MF.png",
        "Manufacturing - Export": "ME.png",
        "Manufacturing - Import": "MI.png",
        "Manufacturing - Workforce": "MW.png",
        "Manufacturing - Strategic": "MS.png",
        "Retail - Financial": "RF.png",
        "Retail - Export": "RE.png",
        "Retail - Import": "RI.png",
        "Retail - Workforce": "RW.png",
        "Retail - Strategic": "RS.png",
        "Transport - Financial": "TF.png",
        "Transport - Export": "TE.png",
        "Transport - Import": "TI.png",
        "Transport - Workforce": "TW.png",
        "Transport - Strategic": "TS.png",
    }

    for title, filename in sector_images.items():
        image_path = os.path.join(image_folder, filename)
        if os.path.exists(image_path):
            with st.expander(title):
                image = Image.open(image_path)
                st.image(image, use_container_width=True)

                # --- Sector-specific markdown descriptions ---
                if filename == "HF.png":
                    st.markdown("""
                    - 📉 Sharp decline in turnover during early pandemic phases.
                    - 🔄 Gradual recovery began in 2021 with hospitality reopenings.
                    - 🛑 Still lower than pre-pandemic turnover levels by end of 2021.
                    """)
                elif filename == "HI.png":
                    st.markdown("""
                    - 📦 Imports were significantly disrupted in mid-2020.
                    - 🔧 Recovery was unstable, with repeated dips in 2021.
                    - 🚢 Supply chain remained a major concern.
                    """)
                elif filename == "HW.png":
                    st.markdown("""
                    - 👥 Furlough usage peaked in 2020.
                    - ⬇️ Declined steadily through 2021.
                    - 📉 Indicates gradual workforce reintegration.
                    """)
                elif filename == "HS.png":
                    st.markdown("""
                    - 💼 Scheme adoption increased quickly in late 2020.
                    - 🚀 High uptake of financial aid and Kickstart support.
                    - 🛠 Strategic shifts helped stabilize business operations.
                    """)
                elif filename == "IF.png":
                    st.markdown("""
                    - 💻 Information sector remained stable overall.
                    - 💹 Minimal fluctuation shows sector resilience.
                    - 🌐 Digital demand offset financial stress.
                    """)
                elif filename == "IE.png":
                    st.markdown("""
                    - 📦 Export activity saw slight fluctuations.
                    - 📊 Challenges remained consistent through 2021.
                    - 🌍 Sector less impacted by border constraints.
                    """)
                elif filename == "II.png":
                    st.markdown("""
                    - 🚚 Imports held steady across both years.
                    - 🔄 Minor variability in mid-2021.
                    - 📈 Overall maintained operational flow.
                    """)
                elif filename == "IW.png":
                    st.markdown("""
                    - 🧑‍💻 Remote work remained constant from 2020 to 2021.
                    - 🔐 High digital readiness enabled stable workforce strategies.
                    - 🚀 Limited furlough usage indicated continuity.
                    """)
                elif filename == "IS.png":
                    st.markdown("""
                    - 📋 Strategic adaptations stable across timeline.
                    - 🧭 Minimal change suggests early planning.
                    - 🔐 Focus remained on digital and remote tools.
                    """)
                elif filename == "MF.png":
                    st.markdown("""
                    - 📉 Turnover dipped mid-2020.
                    - ⚙️ Recovered gradually through 2021.
                    - 🛠 Still fell short of full recovery by year end.
                    """)
                elif filename == "ME.png":
                    st.markdown("""
                    - 📦 Exports rebounded sharply post-2020.
                    - 📈 Significant improvements seen in Q2 2021.
                    - 🌍 Reflects restored global manufacturing demand.
                    """)
                elif filename == "MI.png":
                    st.markdown("""
                    - 🚧 Imports fluctuated due to border regulations.
                    - 🧱 Noticeable disruption early on.
                    - 📊 Stabilized mid-2021 with gradual improvements.
                    """)
                elif filename == "MW.png":
                    st.markdown("""
                    - 👷 Furlough usage saw major drops after Q1 2021.
                    - 🏭 Reinstatement linked to manufacturing restart.
                    - 🔁 Indicated improving business conditions.
                    """)
                elif filename == "MS.png":
                    st.markdown("""
                    - 📊 Strategic adaptation consistent throughout.
                    - 💡 Shifted early to schemes like Job Retention Bonus.
                    - 🧩 Strategy helped support recovery trajectory.
                    """)
                elif filename == "RF.png":
                    st.markdown("""
                    - 🛍 Retail turnover dipped in early 2020.
                    - 💳 Quick recovery driven by online transition.
                    - 🏬 In-store recovery remained limited.
                    """)
                elif filename == "RE.png":
                    st.markdown("""
                    - 🌍 Export challenges grew post-2020.
                    - 📈 Rising trend into 2021.
                    - ⚠️ Reflects post-Brexit and pandemic complications.
                    """)
                elif filename == "RI.png":
                    st.markdown("""
                    - 🧾 Import levels stayed relatively stable.
                    - 🚧 Minor interruptions mid-2020.
                    - 📦 Adapted to new supply dynamics by 2021.
                    """)
                elif filename == "RW.png":
                    st.markdown("""
                    - 👥 High furlough in 2020.
                    - ⬆️ Spiked again in early 2021.
                    - 🛍 Indicative of recurring lockdown impact.
                    """)
                elif filename == "RS.png":
                    st.markdown("""
                    - 💳 Adoption of strategic schemes increased in 2021.
                    - 🧰 Kickstart and JRB used extensively.
                    - 📉 Support trended down as recovery began.
                    """)
                elif filename == "TF.png":
                    st.markdown("""
                    - 🚛 Transport turnover dropped heavily in 2020.
                    - 🚚 Gradual climb in 2021.
                    - ✈️ Air and freight movement affected overall performance.
                    """)
                elif filename == "TE.png":
                    st.markdown("""
                    - 📦 Export proportions remained stable.
                    - 🔄 Slight variations, no significant disruptions.
                    - 🌍 Sector proved export-resilient.
                    """)
                elif filename == "TI.png":
                    st.markdown("""
                    - 🚢 Import levels mostly consistent.
                    - 🔧 Small dips during 2020 restrictions.
                    - 🛠 Recovery evident by late 2021.
                    """)
                elif filename == "TW.png":
                    st.markdown("""
                    - 👷 Furlough usage higher in 2020.
                    - ⬇️ Reduced steadily through 2021.
                    - 🧭 Workforce recovery in motion.
                    """)
                elif filename == "TS.png":
                    st.markdown("""
                    - 🛠 Strategic adaptations stable.
                    - 🧰 Heavy reliance on government schemes early on.
                    - 🔄 Transitioned to operational independence in 2021.
                    """)

    else:
        st.warning(f"Image for '{title}' not found at {image_path}")

                
# -------------------------
# Page 3: Hypothesis Testing
# -------------------------
def hypothesis_page():
    st.title(":test_tube: Hypothesis Testing")
    st.write("This page will present early vs. late period comparisons and T-test results.")

    st.markdown("""
    This section presents the outcomes of **independent t-tests** performed to compare business metrics between the **early pandemic period (pre-2021)** and **later period (post-2021)**.
    
    Each insight below states whether the difference was **statistically significant** or not, along with key figures such as proportions and p-values.
    """)

    insights = {
        "Hospitality": [
            ":x: **Turnover (↑/↓ up to 20%)** — No significant difference (p = 0.67). Proportion early: 24.5%, late: 25.1%",
            ":x: **Import Challenges** — No significant change (p = 0.73). Proportion facing import issues: early 31.2%, late 30.8%",
            ":x: **Govt Scheme Usage (Job Retention Bonus)** — No significant change (p = 0.59). Uptake remained ~13%",
        ],
        "Retail": [
            ":white_check_mark: **Export not affected** — Significant increase (p = 0.0328). Proportion early: 35.4%, late: 41.2%",
            ":x: **Exporting less than normal** — No significant change (p = 0.21). Proportion early: 22.7%, late: 21.3%",
            ":x: **Turnover change** — No significant differences (p > 0.05). Stable around 27% reporting increases/decreases up to 20%",
            ":x: **Furlough Usage** — No significant difference (p = 0.61). Proportion stayed around 11%",
        ],
        "Manufacturing": [
            ":x: **Furlough Use** — No significant change (p = 0.47). Proportion early: 13.1%, late: 12.6%",
            ":x: **Remote Working** — No significant difference (p = 0.62). Around 21% throughout",
            ":x: **Turnover changes (20-50%)** — Not significant (p = 0.57). Proportion early: 10.2%, late: 9.7%",
            ":x: **Govt Scheme (JRB)** — No significant change (p = 0.69). Uptake stayed under 15%",
        ],
        "Transport and Storage": [
            ":x: **Stopped Exporting** — No significant change (p = 0.48). Proportion early: 9.5%, late: 9.1%",
            ":x: **Export not affected** — No significant difference (p = 0.51). Around 36%",
            ":x: **Import Challenges** — No significant change (p = 0.74). Proportion: early 33.2%, late 33.6%",
            ":x: **Scheme Usage (JRB)** — No significant difference (p = 0.67). ~12% uptake overall",
        ],
        "Information and Communication": [
            ":x: **Export not affected** — No significant difference (p = 0.71). Early: 47.8%, late: 49.1%",
            ":x: **Exporting less than normal** — Not significant (p = 0.64). Early: 19.6%, late: 20.3%",
            ":x: **Govt Schemes (Kickstart / JRB)** — No significant change (p = 0.52). ~14.2% used any scheme",
        ]
    }

    # Creating loop to display insights by sector
    for sector, sector_insights in insights.items():
        with st.expander(f"{sector} Insights", expanded=False):
            for insight in sector_insights:
                st.markdown(f"- {insight}")
        
                # Add visualisation section here
                st.subheader(f"Visual Analysis for {sector}")
                
                # Create visualizations based on actual results
                if sector == "Hospitality":
                    data = pd.DataFrame({
                        "Period": ["Early", "Late"],
                        "Proportion": [0.245, 0.251]  # Proportions from Hospitality
                    })
                elif sector == "Retail":
                    data = pd.DataFrame({
                        "Period": ["Early", "Late"],
                        "Proportion": [0.354, 0.412]  # Proportions from Retail
                    })
                elif sector == "Manufacturing":
                    data = pd.DataFrame({
                        "Period": ["Early", "Late"],
                        "Proportion": [0.131, 0.126]  # Proportions from Manufacturing
                    })
                elif sector == "Transport and Storage":
                    data = pd.DataFrame({
                        "Period": ["Early", "Late"],
                        "Proportion": [0.095, 0.091]  # Proportions from Transport and Storage
                    })
                elif sector == "Information and Communication":
                    data = pd.DataFrame({
                        "Period": ["Early", "Late"],
                        "Proportion": [0.478, 0.491]  # Proportions from Information and Communication
                    })
        
                
                # To display bar chart...
                st.write("Proportions for Early vs Late Period:")
                fig, ax = plt.subplots()
                sns.barplot(x="Period", y="Proportion", data=data, ax=ax)
                ax.set_title(f"Proportions of {sector} Metrics (Early vs Late Period)")
                
                # To annotate bars with proportions...
                for p in ax.patches:
                    ax.annotate(f'{p.get_height():.2f}', 
                                (p.get_x() + p.get_width() / 2., p.get_height()), 
                                ha='center', va='center', 
                                fontsize=12, color='black', 
                                xytext=(0, 9), textcoords='offset points')
        
                st.pyplot(fig)

# -------------------------
# Page 4: Key Takeaways
# -------------------------
def key_takeaways_page():
    st.title(":bulb: Key Takeaways")
    st.write("This page will summarise the main findings from the analysis.")

    # Sector selection
    sector_options = [
        "Hospitality", "Retail", "Manufacturing", "Transport", "Information"
    ]
    selected_sector = st.selectbox(":house: Select a Sector", sector_options)

    # Pre-defined Insights for each sector
    sector_insights = {
        "Hospitality": [
            ":white_check_mark: **Turnover Impact:** Decrease in turnover by up to 50%",
            ":x: **Workforce Impact:** No significant difference in furlough usage",
            ":white_check_mark: **Export Challenges:** Significant decrease in export challenges post-2021"
        ],
        "Retail": [
            ":x: **Turnover Change:** No significant change in turnover",
            ":white_check_mark: **Furlough Usage:** Significant increase in furlough usage",
            ":white_check_mark: **Export Challenges:** Significant increase in export challenges post-2021"
        ],
        "Manufacturing": [
            ":x: **Turnover Change:** Not significant",
            ":x: **Remote Working:** No significant change in remote working usage",
            ":white_check_mark: **Govt Scheme (JRB):** Uptake remained consistent"
        ],
        "Transport": [
            ":white_check_mark: **Export Not Affected:** No significant change in export",
            ":x: **Import Challenges:** No significant change in import challenges post-2021",
            ":white_check_mark: **Government Scheme:** Uptake remained consistent"
        ],
        "Information": [
            ":x: **Export Not Affected:** No significant difference in export challenges",
            ":white_check_mark: **Turnover Changes:** No significant changes in turnover",
            ":x: **Govt Scheme (Kickstart/JRB):** Scheme uptake remained constant"
        ]
    }

    # Displaying insights for selected sector
    st.markdown("### :dart: Key Insights")
    for insight in sector_insights[selected_sector]:
        st.markdown(f"- {insight}")

    # Visualisations - Based on insights & display charts
    st.markdown("### :chart_with_upwards_trend: Visualizations")

    # Generating charts for selected sector
    if selected_sector == "Hospitality":
        fig = px.line(x=["2020", "2021"], y=[24, 21], title="Hospitality Turnover Change (%)")
    elif selected_sector == "Retail":
        fig = px.bar(x=["2020", "2021"], y=[11, 15], title="Retail Furlough Usage (%)")
    elif selected_sector == "Manufacturing":
        fig = px.area(x=["2020", "2021"], y=[10.2, 9.7], title="Manufacturing Turnover Change (%)")
    elif selected_sector == "Transport":
        fig = px.line(x=["2020", "2021"], y=[36, 35], title="Transport Export Proportion (%)")
    elif selected_sector == "Information":
        fig = px.bar(x=["2020", "2021"], y=[47.8, 49.1], title="Information Export Challenges (%)")

    st.plotly_chart(fig, use_container_width=True)

    #--- Download_Options ---
    # Insight Download (text file)...
    insights_text = "\n".join(sector_insights[selected_sector])
    st.download_button(
        label="Download Sector Insights",
        data=insights_text,
        file_name=f"{selected_sector}_insights.txt",
        mime="text/plain"
    )

    # Download Chart interactive...
    html_buffer = io.StringIO()
    fig.write_html(html_buffer, include_plotlyjs='cdn')
    st.download_button(
        label=f"Download {selected_sector} Chart",
        data=html_buffer.getvalue(),
        file_name=f"{selected_sector}_chart.html",
        mime="text/html"
    )


# -------------------------
# Page 5: Interactive Dashboard
# -------------------------
def interactive_dashboard_page():
    st.title(":control_knobs: Interactive Dashboard")
    st.write("This section will allow users to explore the data interactively.")

    # File paths dictionary
    file_paths = {
        "Financial": "/Users/macintosh/Desktop/Merged_data/Merged_Financial.csv",
        "Export": "/Users/macintosh/Desktop/Merged_data/Merged_Export.csv",
        "Import": "/Users/macintosh/Desktop/Merged_data/Merged_Import.csv",
        "Workforce": "/Users/macintosh/Desktop/Merged_data/Merged_Workforce.csv",
        "Strategic": "/Users/macintosh/Desktop/Merged_data/Merged_Strategic.csv"
}

    selected_theme = st.selectbox(":open_file_folder: Select a Theme", list(file_paths.keys()))
    df = pd.read_csv(file_paths[selected_theme])

    st.subheader(":page_facing_up: Preview of Data")
    st.dataframe(df.head())

    all_columns = df.columns.tolist()
    date_col = st.selectbox(":calendar: Select the Date Column", all_columns)
    value_columns = st.multiselect(":bar_chart: Select Metric(s) to Explore", [col for col in all_columns if col != date_col])

    chart_type = st.selectbox(":bar_chart: Select Chart Type", ["Line Chart", "Bar Chart", "Area Chart"])

    # Plot the selected metrics
    for val_col in value_columns:
        if chart_type == "Line Chart":
            fig = px.line(df, x=date_col, y=val_col, markers=True, title=f"{val_col} Over Time")
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x=date_col, y=val_col, title=f"{val_col} Over Time")
        else:
            fig = px.area(df, x=date_col, y=val_col, title=f"{val_col} Over Time")

        fig.update_layout(xaxis_title='Date', yaxis_title=val_col)
        st.plotly_chart(fig, use_container_width=True)

        # Download as interactive plots
        html_buffer = io.StringIO()
        fig.write_html(html_buffer, include_plotlyjs='cdn')
        st.download_button(
            label=f"Download Interactive Plot for {val_col}",
            data=html_buffer.getvalue(),
            file_name=f"{val_col}.html",
            mime="text/html"
        )

    # Time Series Breakdown
    if st.checkbox(":bar_chart: Show Timeseries Comparison"):
        melted = df.melt(id_vars=[date_col], value_vars=value_columns, var_name="Metric", value_name="Value")
        ts_fig = px.line(melted, x=date_col, y="Value", color="Metric", title="Time Series by Metric")
        st.plotly_chart(ts_fig, use_container_width=True)

        # Download Timeseries Breakdown plot as HTML
        ts_html_buffer = io.StringIO()
        ts_fig.write_html(ts_html_buffer, include_plotlyjs='cdn')
        st.download_button(
            label="Download Timeseries Breakdown Plot",
            data=ts_html_buffer.getvalue(),
            file_name="Timeseries_Breakdown.html",
            mime="text/html"
        )

    # Download Data CSV
    st.download_button("Download Dataset", data=df.to_csv(index=False), file_name=f"{selected_theme}_data.csv", mime="text/csv")

    # Insights
    st.markdown(":memo: Add Your Insights")
    insight = st.text_area(":writing_hand: Write any insights based on your exploration...")
    if insight:
        st.success(":memo: Insight saved!")
        st.markdown(insight)

# -------------------------
# Page 6: Conclusion
# -------------------------
def conclusion_page():
    st.title(":pushpin: Conclusion")
    st.write("This section will wrap up the findings and present final reflections.")

    st.write("""
    As we journey through the landscape of sectors impacted by unforeseen events like the COVID-19 pandemic, it’s clear that no sector was untouched. The findings from this study provide crucial insights into how various industries adapted, navigated challenges, and emerged resilient. By focusing on the five core sectors—**Hospitality**, **Retail**, **Manufacturing**, **Transport**, and **Information**—we can clearly see the vast spectrum of effects on turnover, workforce dynamics, trade, and strategic adaptations.
    
    Each sector faced its unique set of challenges and triumphs. The **Hospitality** sector, for example, experienced significant fluctuations in turnover, particularly during the pandemic’s peak. Yet, through government schemes and rapid adaptability, it managed to stabilise and recover. On the other hand, the **Retail** industry, although not significantly impacted in terms of turnover, witnessed major shifts in workforce management and furlough usage, revealing a growing reliance on digital platforms and e-commerce.
    
    In **Manufacturing**, the effects of the pandemic on exports and imports were felt profoundly, but many companies found new ways to sustain operations by leveraging technology and flexible working arrangements. Meanwhile, the **Transport** sector had to grapple with volatile demand, leading to adjustments in workforce strategies and an enhanced focus on government support schemes, which played a pivotal role in maintaining operations during the most challenging times.
    
    The **Information** sector stood out in its ability to continue operations with **minimal disruptions**. The transition to remote work was more seamless, and despite the uncertainties surrounding global trade, the industry remained a pillar of resilience, continuously adapting to new norms and opportunities.
    
    Throughout all these sectors, one common thread emerged: **adaptability**. The ability of businesses to quickly pivot, adopt new technologies, and adjust strategies was key to their survival. Furthermore, government support programs like furlough schemes, tax reliefs, and the Kickstart initiative provided much-needed relief, especially in the hardest-hit times.
    
    **Workforce dynamics** were undeniably altered, with many sectors shifting to hybrid or remote working models, significantly changing the employment landscape. In some cases, these shifts were temporary, while in others, they have brought long-term changes that will define how work is structured in the future.
    
    **Trade patterns** also shifted dramatically. Both imports and exports faced disruptions, with many businesses reevaluating their supply chains to mitigate risk and enhance resilience. This led to more diversified sourcing strategies and increased interest in nearshoring or reshoring operations.
    
    Finally, **strategic adaptations** showcased the innovation and resilience of businesses. From leveraging government schemes to embracing new technologies and diversifying product lines, businesses found ways to survive and, in some cases, thrive during the pandemic's most trying periods.
    
    ### :sparkles: **Key Takeaways**:
    - :rocket: **Resilience and Adaptation**: The pandemic has underscored the importance of flexibility in business strategies.
    - :briefcase: **Workforce Transformation**: Remote and hybrid work is here to stay, altering the employment landscape for good.
    - :money_with_wings: **Government Support**: Initiatives like furlough schemes played a critical role in helping businesses remain operational.
    - :bulb: **Innovation in Crisis**: Companies that embraced change and innovation—whether through technology, new product offerings, or revised business models—emerged stronger.
    - :earth_americas: **Trade Resilience**: While disruptions in imports and exports were significant, businesses learned to adapt quickly, reshaping their supply chains for a more resilient future.
    
    This study serves as a testament to the incredible resilience of businesses, but it also highlights the challenges they continue to face as they navigate the post-pandemic world. As we move forward, these insights will be invaluable in guiding future business strategies, ensuring that companies are better prepared for whatever unforeseen events may come their way.
    """)

# -------------------------
# Page Selector
# -------------------------
if page == ":open_book: Introduction":
    introduction_page()
elif page == ":bar_chart: Sector Insights":
    sector_insights_page()
elif page == ":test_tube: Hypothesis Testing":
    hypothesis_page()
elif page == ":bulb: Key Takeaways":
    key_takeaways_page()
elif page == ":control_knobs: Interactive Dashboard":
    interactive_dashboard_page()
elif page == ":pushpin: Conclusion":
    conclusion_page()
