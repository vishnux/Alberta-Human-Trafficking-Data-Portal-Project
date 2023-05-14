import pandas as pd
import streamlit as st
import altair as alt
st.set_page_config(page_title="Human Trafficking Dashboard",layout="wide")

st.title("")
st.markdown("<h1 style='text-align: center;'>Alberta Human Trafficking Dashboard</h1>", unsafe_allow_html=True)

# Load data
data = pd.read_csv("trafficking_data.csv")

# Clean data
data = data[['REF_DATE', 'Statistics', 'VALUE']]
data = data.pivot(index='REF_DATE', columns='Statistics', values='VALUE').reset_index()

# Display charts and additional information using Streamlit

st.markdown("<h3 style='text-align: center;'>This dashboard provides an overview of Key Performance Indicators related to human trafficking in Alberta.</h3>", unsafe_allow_html=True)
col1, col2,col3 = st.columns((1,0.1,1))#gap="large"

with col1:
    # Add some vertical space between the graphs
    # Create line chart for actual incidents
    
    actual_chart = alt.Chart(data).mark_line().encode(
               x=alt.X('REF_DATE:N', axis=alt.Axis(title='Year', labelAngle=0), sort=None),
               y='Actual incidents',
                    tooltip=[
                        alt.Tooltip('REF_DATE:N', title='Year'),
                        alt.Tooltip('Actual incidents', title='Actual Incidents')
                    ]
                    ).properties(
                        title='Trend of actual incidents of trafficking in persons in Alberta from 2017 to 2021'
                    )
    st.subheader('Actual Incidents')
    st.altair_chart(actual_chart, use_container_width=True)
with col2:
    # Add some vertical space between the graphs
    st.write("")
    
with col3:

    # Create line chart for rate per 100,000 population
    rate_chart = alt.Chart(data).mark_line().encode(
        x=alt.X('REF_DATE:N', axis=alt.Axis(title='Year', labelAngle=0), sort=None),
        y='Rate per 100,000 population',tooltip=[
            alt.Tooltip('REF_DATE:N', title='Year'),
            alt.Tooltip('Rate per 100,000 population', title='Rate per 100,000 population')
        ]
            ).properties(
                title='Trend of rate of trafficking in persons per 100,000 population in Alberta from 2017 to 2021'
            )
    st.subheader('Rate per 100,000 population')
    st.altair_chart(rate_chart, use_container_width=True)
    
col1, col2,col3 = st.columns((1,0.1,1))#gap="large"    
   
with col1:    
    # Create line chart for percentage change in rate
    percent_chart = alt.Chart(data).mark_line().encode(
        x=alt.X('REF_DATE:N', 
                axis=alt.Axis(title='Year', labelAngle=0), sort=None),
        y='Percentage change in rate',tooltip=[
        alt.Tooltip('REF_DATE:N', title='Year'),
        alt.Tooltip('Percentage change in rate', title='Percentage change in rate')
    ]
    ).properties(
        title='Percentage change in rate of trafficking in persons in Alberta from 2017 to 2021'
    )
    st.subheader('Percentage Change in Rate')
    st.altair_chart(percent_chart, use_container_width=True)
    
with col2:
    # Add some vertical space between the graphs
    st.write("")
    
with col3:    
    # Create bar chart for unfounded incidents
    unfounded_chart = alt.Chart(data).mark_bar(size=15).encode(
        x=alt.X('REF_DATE:N', axis=alt.Axis(title='Year', labelAngle=0), sort=None),
        y='Unfounded incidents',tooltip=[
        alt.Tooltip('REF_DATE:N', title='Year'),
        alt.Tooltip('Unfounded incidents', title='Unfounded Incidents')
    ]
    ).properties(
        title='Number of unfounded incidents of trafficking in persons in Alberta from 2017 to 2021'
    )
    st.subheader('Unfounded Incidents')
    st.altair_chart(unfounded_chart, use_container_width=True)

# Key Takeaways
with st.expander("Key Insights"):
    st.write(" * The above figures portray the trend of the rate of human trafficking per 100,000 population. This insight combined with the actual incidents rate in Alberta shows that there is an increase in Human trafficking victims in Alberta.")        
    st.write(" * In human trafficking, “unfounded incidents” refer to reported human trafficking cases in which there is insufficient evidence to support the claims or claimed conduct does not comply with the legal definition of human trafficking. We see an increase in these cases but it is crucial to remember that fabricated occurrences shouldn’t diminish the importance of actual instances of human trafficking. Authorities and organizations must ensure that all reported cases are thoroughly investigated while also providing protection and assistance to any prospective victims. The urgent need to confront the widespread problem of human trafficking and help individuals who have actually been harmed should not be overshadowed by unfounded cases.")
# Data source
with st.expander("Data Source"):
    st.write("The following analysis offers a thorough look at the documents connected to human trafficking in Alberta based on official data sources provided by Statistics Canada which primarily focused on the most recent five-year period (2017–2021) since the quality of data for previous years is sparse and cannot be relied upon for accuracy. Statistics Canada [Table 35-10-0177-01  Incident-based crime statistics, by detailed violations, Canada, provinces, territories, Census Metropolitan Areas and Canadian Forces Military Police](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701&pickMembers%5B0%5D=1.33&pickMembers%5B1%5D=2.58&cubeTimeFrame.startYear=2017&cubeTimeFrame.endYear=2021&referencePeriods=20170101%2C20210101)")
