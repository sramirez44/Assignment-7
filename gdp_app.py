# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import requests as rq
import bs4
from io import StringIO

# app title
st.title("Global GDP by Region")
st.write("This app displays GDP of different world regions in a stacked bar chart.")

# reading the webpage data
url = 'https://en.wikipedia.org/w/index.php?title=List_of_countries_by_GDP_(nominal)&oldid=1187446467'
page = rq.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15"})

# parsing the webpage
soup = bs4.BeautifulSoup(page.text, 'html.parser')

# reading the webpage data and extracting tables
tables = pd.read_html(StringIO(str(soup)))

# selecting the third table 
df = tables[2]

# selecting the columns we need
clean_df = df.iloc[:, [0, 1, 2, 4, 6]].copy()
clean_df.columns = ['Country', 'Region', 'IMF', 'WorldBank', 'UN']

# converting to numeric values
for col in ['IMF', 'WorldBank', 'UN']:
    clean_df[col] = (
        clean_df[col]
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.strip()
    )
    clean_df[col] = pd.to_numeric(clean_df[col], errors='coerce')

# remove the world row
clean_df = clean_df[clean_df['Country'] != 'World'].copy()

# fills in the missing data from Worldbank and UN
clean_df['IMF_imputed'] = clean_df['IMF'].fillna(clean_df['WorldBank']).fillna(clean_df['UN'])

# Create a dropdown to select the reporting organization
source = st.selectbox("Select Reported Numbers:", ["IMF", "WorldBank", "UN"])

# create the stacked plot using the user's selected source
fig = px.bar(clean_df, x="Region", y=source, color="Country")

# display plot
st.plotly_chart(fig, use_container_width=True)