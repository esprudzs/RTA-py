import streamlit as st
from datetime import datetime
import pandas as pd
import numpy as np

#Page header
st.title("Welcome to the coolest solar panel efficiency calculator this side of Equator!")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Today is ", datetime(2022,10,22))

with col2:
  st.subheader("Outside is ")
  
