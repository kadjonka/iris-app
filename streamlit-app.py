import streamlit as st
import pandas as pd 
#titre

# Charger les données
data = pd.read_csv('Iris.csv', delimiter=';')
st.title('mon premier dashboard avec Streamlit')
# Créer un titrest.title("Mon premier tableau de bord Streamlit") 
# Afficher les données dans un tableau
#st.table(data)
         
 chart = alt.chart(data).mark_bar().encode(x='SepalLength', y='SepalWidth')
st.altair_chart(chart, use_container_width= True)

st.altair_chart(chart, use_container_width=True)

                                                      


