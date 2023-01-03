import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

#Setup
to_day = datetime.ctime()

#Page header
st.title("Welcome to the coolest solar panel efficiency calculator this side of Equator!")

#Set up two columns
col1, col2, col3 = st.columns(3)
with col1:
  st.subheader("Today is ")
with col2:
  st.subheader(to_day)
with col3:
  st.subheader("Outside is ")
  
