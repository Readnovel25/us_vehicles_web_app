# -------------------------------- Import libraries --------------------------------
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
# -------------------------------- End of imports --------------------------------

# Web app start
st.header('Market of used cars')
st.write('Filter the data below to see the ads by manufacturer')

# Read the data into a dataframe
df = pd.read_csv('vehicles_us.csv')

# -------------------------------- Process the data --------------------------------
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
