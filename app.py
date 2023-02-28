# import pandas as pd
# import streamlit as st
# import altair as alt

# # Load the data
# data = pd.read_csv("trafficking_data.csv")

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
# st.write(filtered_data)
# # Create a chart
# chart_data = filtered_data[["REF_DATE", "VALUE"]]
# chart_data = chart_data.set_index("REF_DATE")
# chart_data.index = chart_data.index.astype(str)
# st.write(chart_data)
# # # #chart_data.index = pd.to_datetime(chart_data.index)
# # chart = alt.Chart(chart_data).mark_bar().encode(
# #      x=alt.X("REF_DATE", title="Year"),
# #     y=alt.Y("VALUE", title=selected_option)
# # #     tooltip=["REF_DATE", alt.Tooltip("VALUE", format=".2f")]
# #  ).properties(width=700, height=400)

# # # Display the chart and the data table
# # st.altair_chart(chart)
# # st.write(filtered_data)

# # #chart_data.index = pd.to_datetime(chart_data.index)
# # chart = alt.Chart(chart_data).mark_bar().encode(
# #      x="REF_DATE",y="VALUE")
# st.line_chart(chart_data)

# # Display the chart and the data table
# #st.altair_chart(chart)
# st.write(filtered_data)


import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data
data = pd.read_csv("trafficking_data.csv")

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

# Create a line chart
fig = px.line(filtered_data, x="REF_DATE", y="VALUE", title=selected_option)

# Display the chart and the data table
st.plotly_chart(fig)
st.write(filtered_data)

