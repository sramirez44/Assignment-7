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