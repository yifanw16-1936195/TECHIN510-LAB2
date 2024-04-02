import streamlit as st
import pandas as pd
import seaborn as sns
from datetime import datetime
import pytz
import matplotlib.pyplot as plt

# Set up page
st.set_page_config(page_title="Penguins Explorer", layout="wide")

# Title and introduction
st.title("🐧 Penguins Explorer")
st.markdown("Explore the fascinating world of Palmer Archipelago's Penguins.")

# Load data
@st.cache
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

df = load_data()

# Sidebar
species = st.sidebar.multiselect('Select species:', options=df['species'].unique(), default=df['species'].unique())
island = st.sidebar.multiselect('Select island:', options=df['island'].unique(), default=df['island'].unique())
filtered_data = df[(df['species'].isin(species)) & (df['island'].isin(island))]

# Show data
st.dataframe(filtered_data)

# Show statistics
st.subheader("Penguin Size Visualization")
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x="flipper_length_mm", y="body_mass_g", hue="species", style="island", ax=ax)
st.pyplot(fig)
