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
st.markdown("""
Explore the fascinating world of Palmer Archipelago's Penguins. The dataset contains observations of three penguin species and includes several measurements such as bill length, bill depth, flipper length, body mass, and more.
""")

# Load data
@st.cache
def load_data():
    return pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

df = load_data()
# Dataset columns description
st.markdown("""
### Dataset Columns Description
- **species**: The species of penguin (Adelie, Chinstrap, Gentoo)
- **island**: The island in the Palmer Archipelago, Antarctica, where the penguins were observed
- **bill_length_mm**: The length of the penguin's bill (culmen) in millimeters
- **bill_depth_mm**: The depth of the penguin's bill (culmen) in millimeters
- **flipper_length_mm**: The length of the penguin's flipper in millimeters
- **body_mass_g**: The body mass of the penguin in grams
- **sex**: The sex of the penguin (male, female)
- **year**: The year of the observation
""")

# Sidebar
species = st.sidebar.multiselect('Select species:', options=df['species'].unique(), default=df['species'].unique())
island = st.sidebar.multiselect('Select island:', options=df['island'].unique(), default=df['island'].unique())
year_range = st.sidebar.slider("Select the year of observation:", int(df['year'].min()), int(df['year'].max()), (int(df['year'].min()), int(df['year'].max())))

# Filter data based on sidebar choices
filtered_data = df[(df['species'].isin(species)) & (df['island'].isin(island)) & (df['year'].between(year_range[0], year_range[1]))]

# Show data
st.dataframe(filtered_data)

# Show statistics
st.subheader("Penguin Size Visualization")
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x="flipper_length_mm", y="body_mass_g", hue="species", style="island", ax=ax)
st.pyplot(fig)
