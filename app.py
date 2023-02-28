import pandas as pd
import altair as alt
import streamlit as st

# Load data
data = pd.read_csv('trafficking_data.csv')

print(data)
# Set page title
st.set_page_config(page_title="Trafficking in Persons Dashboard")

# Add page title and subtitle
st.title("Trafficking in Persons Dashboard")
st.write("This dashboard provides an overview of trafficking in persons in Canada from 2017 to 2021.")

# # Create dropdown to select year
# year = st.selectbox("Select a year:", options=data["Year"].unique())

# # Create dataframe for selected year
# year_data = data[data["Year"] == year]

# # Display number of actual incidents for selected year
# st.subheader(f"Number of Actual Incidents in {year}:")
# st.write(year_data["Actual incidents"].sum())

# # Display rate per 100,000 population for selected year
# st.subheader(f"Rate per 100,000 Population in {year}:")
# st.write(year_data["Rate per 100,000 population"].values[0])

# # Create bar chart showing number of incidents and unfounded incidents for selected year
# chart_data = year_data[["Actual incidents", "Unfounded incidents"]]
# chart_data = chart_data.rename(columns={"Actual incidents": "Actual Incidents", "Unfounded incidents": "Unfounded Incidents"})
# chart = alt.Chart(chart_data).mark_bar().encode(x="index", y=alt.Y("value", stack=None), color="variable").properties(width=500)
# st.subheader(f"Number of Actual and Unfounded Incidents in {year}:")
# st.altair_chart(chart)

# # Display percentage change in rate for selected year
# st.subheader(f"Percentage Change in Rate in {year}:")
# st.write(year_data["Percentage change in rate"].values[0])

# # Display total cleared and cleared by charge for selected year
# st.subheader(f"Total Incidents Cleared in {year}:")
# st.write(year_data["Total cleared"].values[0])
# st.subheader(f"Incidents Cleared by Charge in {year}:")
# st.write(year_data["Cleared by charge"].values[0])

# # Create bar chart showing total persons charged for selected year
# charge_data = year_data[["Total, persons charged", "Total, adult charged", "Total, youth charged"]]
# charge_data = charge_data.rename(columns={"Total, persons charged": "Total Persons Charged", "Total, adult charged": "Adults Charged", "Total, youth charged": "Youth Charged"})
# charge_chart = alt.Chart(charge_data).mark_bar().encode(x="index", y="value", color="variable").properties(width=500)
# st.subheader(f"Total Persons Charged in {year}:")
# st.altair_chart(charge_chart)
