import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

#Setup
col1, col2 = st.columns(2)     #Set up 2 columns
today = datetime.now()


#Page header
st.title("Welcome to the coolest solar panel efficiency calculator this side of Equator!")


with col1:
  st.subheader("Today is ")

with col2:
  st.subheader("Outside is ")
  
