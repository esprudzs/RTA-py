import streamlit as st
from datetime import date
import pandas as pd
import numpy as np

#For weather
import requests, json

#Setup
today = date.today()

#Page header
st.title("Welcome to the coolest solar panel efficiency calculator this side of Equator!")

#Set up two columns
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
  st.subheader("Today is ")
with col2:
  st.subheader(today)
with col4:
  st.subheader("Outside is ")
  
with col5:
  st.metric(label = "", value = "10C", delta = "5")
