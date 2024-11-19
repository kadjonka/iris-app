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
           

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title('Mon application Streamlit avec graphique')

# Créer des données
data = pd.DataFrame({
    'x': np.arange(0, 10),
    'y': np.random.rand(10)
})

# Graphique avec Matplotlib
plt.figure()
plt.plot(data['x'], data['y'], marker='o')
plt.title('Graphique Exemple')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Afficher le graphique
st.pyplot(plt)
