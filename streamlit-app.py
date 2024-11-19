import streamlit as st
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt


data =pd.read_csv('Iris.csv', delimiter = ';')
st.title('Mon premier dashboard avec Streamlit')
 #st. table(data)
import altair as alt
import pandas as pd

   # Créer un chart Altair
chart = alt.Chart(data).mark_bar().encode( x='SepalLength', y='SepalWidth')
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)
                                           
chart = alt.Chart(data).mark_point().encode( x='SepalLength', y='PetalLength')
# Afficher le chart sur Streamlit
st.altair_chart(chart, use_container_width=True)


import streamlit as st

# Title for the main app
st.title("Main App Area")

# Title for the sidebar
st.sidebar.title("Sidebar")

# Add widgets to the sidebar
option = st.sidebar.selectbox(
    "Select an option:",
    ["Option iris", "Option data", "Option github"]
)

# Display selected option
st.write(f"You selected: {option}")
