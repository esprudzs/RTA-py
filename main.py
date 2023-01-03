import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

#Setup
today = datetime.now()

#Page header
st.title("Welcome to the coolest solar panel efficiency calculator this side of Equator!")

#Set up two columns
col1, col2 = st.columns(2)
with col1:
#  st.subheader("Today is ", today)
  st.subheader(today)
with col2:
  st.subheader("Outside is ")
  
