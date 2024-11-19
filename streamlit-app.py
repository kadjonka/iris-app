import streamlit as st
import pandas as pd 
#titre
st.title('ceci est mon dashboard')
# Charger les données
data = pd.read_csv('Iris.csv', delimiter=';')

# Créer un titrest.title("Mon premier tableau de bord Streamlit") 
# Afficher les données dans un tableau
#st.table(data)
st.write(data.head())
           



