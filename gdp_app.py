# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import requests as rq
import bs4
from io import StringIO

# create app title
st.title("GDP by Region")
st.write("This app displays GDP of different world regions in a stacked bar chart.")

# create cache of the wiki data
@st.cache_data
def load_data():
    url = "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_GDP_(nominal)&oldid=1187446467"
    response = rq.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    # extract tables
    tables = pd.read_html(StringIO(str(soup)))
    df = tables[2]

    # parse table 
    try:
        clean_df = df.iloc[:, [0, 1, 2, 4, 6]].copy()
    except IndexError:
        clean_df = df.iloc[:, [0, 1, 2, 3, 4]].copy()
        
    clean_df.columns = ['Country', 'Region', 'IMF', 'WorldBank', 'UN']

    # convert to numeric
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

    # missing values
    clean_df['IMF'] = clean_df['IMF'].fillna(clean_df['WorldBank']).fillna(clean_df['UN'])
    clean_df['WorldBank'] = clean_df['WorldBank'].fillna(clean_df['IMF']).fillna(clean_df['UN'])
    clean_df['UN'] = clean_df['UN'].fillna(clean_df['IMF']).fillna(clean_df['WorldBank'])

    return clean_df

# load data
df = load_data()

#create dropdown for region selection
source = st.selectbox("Select GDP Source:", ['IMF', 'WorldBank', 'UN'])

#create plot
fig = px.bar(df, x='Region', y=source, color='Country', title=f'GDP by Region ({source})', labels={source: 'GDP (in USD)'})

# display plot
st.plotly_chart(fig, use_container_width=True)