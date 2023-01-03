import streamlit as st
from datetime import date
import pandas as pd
import numpy as np

#For weather
import requests, json

#Setup
today = date.today()
base_url = "https://api.openweathermap.org/data/2.5/weather?"
url = base_url + "q=" + "Riga" + "&appid=" + "test"
respone = requests.get(url)
if response.status.code == 200:
  data = response.json()
  main = data['data']
  temperature = main['temp']
else:
  st.write("Error")
  
#Page header
st.title("Welcome to the coolest solar panel efficiency calculator this side of Equator!")

#Set up two columns
col1, col2, col3 = st.columns(3)
with col1:
  st.subheader("Today is ")
with col2:
  st.subheader(today)
with col3:
  st.subheader("Outside is ")
  
