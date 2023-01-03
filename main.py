import streamlit as st

#Page header
st.title("Welcome to the coolest solar panel efficiency calculator this side of Equator!")
col1, col2 = st.column(2)

with col1:
  st.header("Today is ")

with col2:
  st.header("Outside is ")
  
