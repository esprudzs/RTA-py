import streamlit as st
from datetime import date
import pandas as pd
import numpy as np

#For weather
import requests, json

def GetTemp(location_str):
  temp = "15C"
  return temp

def GetLocation():
  pass


#Setup
today = date.today()
location = GetLocation()
temperature = GetTemp(location)

#Page header
st.title("Solar panel efficiency calculator")


#Set up two columns
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
  st.subheader("Today: ")
with col2:
  st.subheader(today)
with col5:
  st.subheader("Outside: ")
with col6:
  st.subheader(temperature)

