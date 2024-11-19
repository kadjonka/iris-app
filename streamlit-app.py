import streamlit as st
import pandas as pd 
#titre
st.title('ceci est mon dashboard')
# Charger les données
data = pd.read_csv('Iris.csv', delimiter=';')

# Créer un titrest.title("Mon premier tableau de bord Streamlit") 
# Afficher les données dans un tableau
#st.table(data)
st.write(data.head()
         
 chart = alt.chart (data). mark_bar(), encode( x='sepallenght', y='sepalwidth')
st.altair_chart (chart, use_container_width= True)
chart = alt.chart( data),mark_point().encode(x='sepallenght', y='sepalwidth')
st.altair_char(chart, use contenair_width=True

                                                      


