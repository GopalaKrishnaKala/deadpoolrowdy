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

visit_days = st.sidebar.number_input('Enter the number of days of recent data you want', min_value=2, value=3)



