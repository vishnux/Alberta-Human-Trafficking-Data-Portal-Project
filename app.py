import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title="Trafficking in Persons Dashboard")
# Load the data
data = pd.read_csv("trafficking_data.csv")

st.title("Trafficking in Persons Dashboard")
st.write("This dashboard provides an overview of trafficking in persons in Canada from 2017 to 2021.")

# Create a dictionary for selecting options
options = {
    "Actual incidents": "Actual incidents",
    "Rate per 100,000 population": "Rate per 100,000 population",
    "Percentage change in rate": "Percentage change in rate",
    "Unfounded incidents": "Unfounded incidents",
    "Percent unfounded": "Percent unfounded"
}

# Create a sidebar for selecting options
selected_option = st.sidebar.selectbox("Select an option", list(options.keys()))

# Filter the data based on the selected option
filtered_data = data[data["Statistics"] == options[selected_option]]
filtered_data['REF_DATE'] = filtered_data.REF_DATE.astype(str)

# Create a line chart
fig = px.bar(filtered_data, x="REF_DATE", y="VALUE", title=selected_option)

# Display the chart and the data table
st.plotly_chart(fig)
st.write(filtered_data)

st.write("Data Source: Statistics Canada[Table 35-10-0177-01  Incident-based crime statistics, by detailed violations, Canada, provinces, territories, Census Metropolitan Areas and Canadian Forces Military Police](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701)")
