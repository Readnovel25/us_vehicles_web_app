# -------------------------------- Import libraries -------------------------------- #
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
# -------------------------------- End of imports -------------------------------- #

# Web App Header
st.header('Market of Used Cars')
# Allow user to filter the data
st.write('Filter the data below to see the ads by manufacturer and cylinder engine')

# Read the data into a dataframe
df = pd.read_csv('vehicles_us.csv')

# -------------------------------- Process the data -------------------------------- #
# Add a manufacturer column to the dataframe
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])
df.insert(3, 'manufacturer', df.pop('manufacturer'))

# Replace the missing values in 'is_4wd' with 0 and change type to boolean
df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)

# Replace missing paint colors with the most frequent value for each model
df['paint_color'] = df.groupby('model')['paint_color'].transform(lambda x: x.fillna(x.mode()[0]))

# Replace missing cylinders with the most frequent value for each model
df['cylinders'] = df.groupby('model')['cylinders'].transform(lambda x: x.fillna(x.mode()[0])).astype(int)

# Replace missing model years with the most frequent value for each model
df['model_year'] = df.groupby('model')['model_year'].transform(lambda x: x.fillna(x.mode()[0])).astype(int)

# Replace missing odometer values with the median odometer value for each model
df['odometer'] = df.groupby('model')['odometer'].transform(lambda x: x.fillna(x.median()))

# Replace remaining missing odometer values with the median odometer value for each cylinder type
df['odometer'] = df.groupby('cylinders')['odometer'].transform(lambda x: x.fillna(x.median()))

# Create dictionary of values to replace
replacements = {
    'ford f150': 'ford f-150',
    'ford f250': 'ford f-250',
    'ford f350': 'ford f-350',
    'ford f250 super duty': 'ford f-250 sd',
    'ford f-250 super duty': 'ford f-250 sd',
    'ford f350 super duty': 'ford f-350 sd',
}

# Replace values in dataframe
df['model'] = df['model'].replace(replacements)
# -------------------------------- End of Data Processing -------------------------------- #

# -------------------------------- Start of Web App -------------------------------- #
# Get the manufacturers
manufacturer_names = df['manufacturer'].unique()

selected_manufacturer = st.selectbox('Select a manufacturer', manufacturer_names)

# Get the cylinders
cylinders_choice = df['cylinders'].unique()
selected_cylinder = st.selectbox('Select a cylinder engine', cylinders_choice)

# Filter the data according to user's choices
df_filtered = df[(df.manufacturer == selected_manufacturer) & (df.cylinders == selected_cylinder)]

# Show filtered dataframe
df_filtered
