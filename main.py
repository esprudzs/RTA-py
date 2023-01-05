import streamlit as st
from datetime import date
import pandas as pd
import numpy as np

#For weather
import requests, json

#some .json magic here
def GetTemp(location_str):
  temp = "15C"
  return temp

#more .json magic here
def GetLocation():
  pass

#Setup
#variables
today = date.today()
location = GetLocation()
temperature = GetTemp(location)

#constants
_solarEnergyS = 1219   #expected solar energy, kWh/m2 per year, facing South
_solarEnergyN = 554    #expected solar energy, kWh/m2 per year, facing North

#Page header
st.header("Solar panel efficiency calculator")

#Set up columns
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
  st.subheader("Today: ")
with col2:
  st.subheader(today)
with col5:
  st.subheader("Outside: ")
with col6:
  st.subheader(temperature)

#Add an empty row for clarity
  st.write("")
  
#Data collection area
#Set up columns
col1, col2, col3 = st.columns(3)

with col1:
  south = st.number_input("Specify your total roof area facing South in m2")
with col2:
  north = st.number_input("Specify your total roof area facing North in m2")
#with col3:
#This ugly crap is not working
#  st.text("While most building are not placed along lattitude or longtitude axes, choose areas angled more towards South or North.")
  
with col1:
  totarea = st.caption("Total area: " + str(south + north) + $m^2$)
  
  
