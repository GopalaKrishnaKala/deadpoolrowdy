import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import yfinance as yf # https://pypi.org/project/yfinance/
import seaborn
from scipy import stats
import pylab as pl
from pandas.plotting import lag_plot
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose


st.set_page_config(layout="wide",)

st.sidebar.markdown("How many days are you visiting San Antonio?")

days_visit = st.sidebar.number_input('Enter the number of days of recent data you want', min_value=2, value=3)

st.sidebar.markdown("Which month are you planning to visit San Antonio?")

month_visit = st.sidebar.selectbox('Select Month you are visiting', ( 'January', 'February',"March",'April', 'May', 'June',"July",'August', 'September', 'October',"November",'December')

st.sidebar.markdown("From Airport are you planning to come to San Antonio?")

entry_airport = st.sidebar.selectbox('Select Month you are visiting', ( 'AUS', 'BOS',"DFW",'FLL', 'IAH', 'JFK',"MIA",'SEA', 'SFO', 'SLC')




