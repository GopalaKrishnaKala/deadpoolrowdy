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



df = yf.download(option,start= start_date,end= end_date, progress=False)
                                     
if option == 'AUS':
    df_aus = pd.read_csv("flight_data_and_price_history_AUS_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of Austin to San Antonio</h2>", unsafe_allow_html=True)
    df_aus.head()                                     
elif option == 'BOS':
    df_bos = pd.read_csv("flight_data_and_price_history_BOS_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of Boston to San Antonio</h2>", unsafe_allow_html=True)
    df_bos.head()
elif option == 'DFW':
    df_dfw = pd.read_csv("flight_data_and_price_history_DFW_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of Dallas to San Antonio</h2>", unsafe_allow_html=True)
    df_dfw.head()
elif option == 'FLL':
    df_fll = pd.read_csv("flight_data_and_price_history_FLL_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of Florida to San Antonio</h2>", unsafe_allow_html=True)
    df_fll.head()
elif option == 'IAH':
    df_iah = pd.read_csv("flight_data_and_price_history_IAH_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of Houston to San Antonio</h2>", unsafe_allow_html=True)
    df_iah.head()
elif option == 'JFK':
    df_jfk = pd.read_csv("flight_data_and_price_history_JFK_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of New York to San Antonio</h2>", unsafe_allow_html=True)
    df_jfk.head()
elif option == 'MIA':
    df_mia = pd.read_csv("flight_data_and_price_history_MIA_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of Miami to San Antonio</h2>", unsafe_allow_html=True)
    df_mia.head()
elif option == 'SEA':
    df_sea = pd.read_csv("flight_data_and_price_history_SEA_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of Seattle to San Antonio</h2>", unsafe_allow_html=True)
    df_sea.head()
elif option == 'SFO':
    df_sfo = pd.read_csv("flight_data_and_price_history_SFO_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of San Fransisco to San Antonio</h2>", unsafe_allow_html=True)
    df_sfo.head()
elif option == 'SLC':
    df_slc = pd.read_csv("flight_data_and_price_history_SLC_to_SAT.csv")
    st.markdown("<h2 style='text-align: center; color: black;'>Previous Data of Salt Lake City to San Antonio</h2>", unsafe_allow_html=True)
    df_slc.head()

#st.line_chart(df_stock)



