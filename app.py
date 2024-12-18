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

# Price Analysis
st.header('Price Analysis')
st.write("""
### What factor influences the price the most?
         Let's check how distribution of price varies depending on transmission, type, fuel type, condition, and paint color
""")

hist_variables = ['transmission', 'type', 'fuel', 'condition', 'paint_color']
selected_factor = st.selectbox('Split for price distribution', hist_variables)

fig1 = px.histogram(df, x="price", color=selected_factor)
fig1.update_layout(title= "<b> Split of price by {}</b>".format(selected_factor))
st.plotly_chart(fig1)

# Scatterplot based on numerical variables
def age_category(x):
    if x<5: return '<5'
    elif  x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'

df['age'] = 2024 - df['model_year']

df['age_category'] = df['age'].apply(age_category)

scatter_variables = ['odometer', 'cylinders', 'days_listed']

choice_for_scatter = st.selectbox('Price dependency on', scatter_variables)

fig2 = px.scatter(df, x="price_usd", y=choice_for_scatter, color="age_category", hover_data=['model_year'])
fig2.update_layout(title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)
