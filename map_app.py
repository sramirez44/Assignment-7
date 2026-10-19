# import libraries
import streamlit as st
import pandas as pd

# app title
st.title("Map Locator by Coordinates")
st.write("Enter longitude and latitude to locate a place on the map.")

# input fields for longitude and latitude
long = st.number_input("Enter Longitude:", value=0.0, format="%.5f")
lat = st.number_input("Enter Latitude:", value=0.0, format="%.5f")

# create dataframe from inputs
df = pd.DataFrame({
    'lat': [lat],
    'lon': [long]
})

# display map
st.map(df, zoom=10)
