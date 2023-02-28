# import pandas as pd
# import streamlit as st
# import plotly.express as px
# st.set_page_config(page_title="Human Trafficking Dashboard")
# # Load the data
# data = pd.read_csv("trafficking_data.csv")

# st.title("Trafficking in Persons Dashboard")
# st.write("This dashboard provides an overview of trafficking in persons in Canada from 2017 to 2021.")

# # Create a dictionary for selecting options
# options = {
#     "Actual incidents": "Actual incidents",
#     "Rate per 100,000 population": "Rate per 100,000 population",
#     "Percentage change in rate": "Percentage change in rate",
#     "Unfounded incidents": "Unfounded incidents",
#     "Percent unfounded": "Percent unfounded"
# }

# # Create a sidebar for selecting options
# selected_option = st.sidebar.selectbox("Select an option", list(options.keys()))

# # Filter the data based on the selected option
# filtered_data = data[data["Statistics"] == options[selected_option]]
# filtered_data['REF_DATE'] = filtered_data.REF_DATE.astype(str)

# # Create a line chart
# fig = px.bar(filtered_data, x="REF_DATE", y="VALUE", title=selected_option)

# # Display the chart and the data table
# st.plotly_chart(fig)
# st.write(filtered_data)

# st.write("Data Source: Statistics Canada [Table 35-10-0177-01  Incident-based crime statistics, by detailed violations, Canada, provinces, territories, Census Metropolitan Areas and Canadian Forces Military Police](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701)")


import pandas as pd
import streamlit as st
import plotly.express as px
import altair as alt
# Load the data
data = pd.read_csv("trafficking_data.csv")

# Set page title and layout
st.set_page_config(page_title="Human Trafficking Dashboard",layout="wide")

# Title and description
#st.title("Trafficking in Persons Dashboard")
st.markdown("<h1 style='text-align: center;'>Human Trafficking in Alberta Dashboard</h1>", unsafe_allow_html=True)
st.write('''Imagine a world where people are bought and sold as commodities, their bodies, and lives exploited for the profit and pleasure of others. It's a world that's hard to fathom, yet this is the reality for millions worldwide who are victims of human trafficking. Human trafficking is a horrendous crime that involves the exploitation of vulnerable individuals through deceitful tactics such as recruitment, transportation, transfer, harboring, or receipt through force, coercion, or deception. Women, children, and minority communities are particularly vulnerable and often targeted by human traffickers. These individuals are subjected to abuses like sexual exploitation, forced labor, or organ harvesting and are robbed of their fundamental human rights. But there's hope. Multiple organizations and initiatives work tirelessly to combat human trafficking and support its survivors. By advocating and supporting these efforts, we can make a difference and create a world where everyone is free to live their lives without fear of exploitation or abuse. Together, we can ensure that victims receive the support and care they need to heal and rebuild their lives. It's time for us to take action and speak out against this heinous crime. By raising awareness, supporting anti-trafficking organizations, and advocating for stronger laws and policies to combat human trafficking, we can create a world where the dignity and rights of all individuals are respected and protected. Let us work together to end human trafficking and create a brighter, safer future for everyone.
''')
#st.markdown('<div style="text-align: justify;">Imagine a world where people are bought and sold as commodities, their bodies, and lives exploited for the profit and pleasure of others. It's a world that's hard to fathom, yet this is the reality for millions worldwide who are victims of human trafficking.</div>', unsafe_allow_html=True)

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

st.write("The increase in human trafficking is on the rise in Alberta and the fifth consecutive year of increase in incidents.")

# Create a bar chart for selected option
bar_fig = px.bar(filtered_data, x="REF_DATE", y="VALUE", title=selected_option)
st.plotly_chart(bar_fig)

# Create a line chart for trend analysis
trend_data = data.groupby(['Statistics', 'REF_DATE'], as_index=False)['VALUE'].sum()
line_fig = px.line(trend_data, x="REF_DATE", y="VALUE", color='Statistics', title='Trend Analysis')
st.plotly_chart(line_fig)

chart = (
    alt.Chart(
        filtered_data,
        title="Static site generators popularity",
    )
    .mark_bar()
    .encode(
        x=alt.X("REF_DATE", title="'000 stars on Github"),
        y=alt.Y(
            "VALUE",
            sort=alt.EncodingSortField(field="Value", order="descending"),
            title="",
        ),
        color=alt.Color(
            "lang",
            legend=alt.Legend(title="Language")
        ),
        tooltip=[],
    )
)


st.altair_chart(chart, use_container_width=True)
# Display the data table
st.write(filtered_data)

# Data source
st.write("Data Source: Statistics Canada [Table 35-10-0177-01  Incident-based crime statistics, by detailed violations, Canada, provinces, territories, Census Metropolitan Areas and Canadian Forces Military Police](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3510017701)")
