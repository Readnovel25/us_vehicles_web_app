# Import libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
# End of imports

# Web app start
st.header('Market of used cars')
st.write('Filter the data below to see the ads by manufacturer')

# Read the data into a dataframe
df = pd.read_csv('vehicles_us.csv')
