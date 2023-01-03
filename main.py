import streamlit as st

#Page header
st.title("Welcome to the coolest solar panel efficiency calculator this side of Equator!")
left_side, right_side = st.column(2)

with left_side:
  st.header("Today is ")

with right_side:
  st.header("Outside is ")
  
