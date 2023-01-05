import streamlit as st
from datetime import date
from PIL import Image
import requests, json

#For energy price
#some cool .json

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
brand = ""
pcsonsouth = 0
pcsonnorth = 0
totalpcs = 0
southkW = 0
northkW = 0
totalkW = 0

#constants
_solarEnergyS = 1219   #expected solar energy, kWh/m2 per year, facing South, globalsolaratlas.info for Riga
_solarEnergyN = 554    #expected solar energy, kWh/m2 per year, facing North, globalsolaratlas.info for Riga
_hyndai1pcarea = 1.719 * 1.140  #Hyndai, 1 unit area, m2
_hyndai1pcpower = 0.410           #Hyndai, 1 unit max output, kW
_jinko1pcarea = 1.903 * 1.134   #Jinko, 1 unit area, m2
_jinko1pcpower = 0.470            #Jinko, 1 unit max output, kW

#Page header
#st.header("Solar panel efficiency calculator")

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
#  st.write("")
  
#Data collection area
#Set up columns
col1, col2, col3 = st.columns(3)

with col1:
  southarea = st.number_input("Specify your total roof area facing South in" + " $$m^2$$")
with col2:
  northarea = st.number_input("Specify your total roof area facing North in" + " $$m^2$$")
#with col3:
#This ugly crap is not working
#  st.text("While most buildings are not placed along lattitude or longtitude axes, choose areas angled more towards South or North.")

#Set up columns
col1, col2 = st.columns(2)

with col1:
  totarea = southarea + northarea
  st.caption("Total area: " + str(totarea) + " $$m^2$$")
  brand = st.selectbox("Specify solar panel producer", ("", "Hyndai", "JINKO"))
  
with col2:
  if brand != "":           #nothing selected, no image
    if brand == "Hyndai":   #hyndai selected, hyndai panel image
      st.image("https://site-539722.mozfiles.com/files/539722/catitems/220f5a204f9ba99a58c155a0f85d-714ef5bead039c6f108b218f271002c5.jpg?4583301")
    else:                   #jinko selected, jinko image
      st.image("https://site-539722.mozfiles.com/files/539722/catitems/Jinko470-1-511f94d46e72b1fe7e62ce1c1fb6cf24.jpg?4934090")
  
with col1:
  if brand != "":           #do nothing for no producer selected
    if brand == "Hyndai":
      if southarea != 0:
        pcsonsouth = southarea // _hyndai1pcarea                    #calculate how many pieces will fit in the area
        southkW = pcsonsouth * _hyndai1pcpower
        st.caption("Number of panels on S: " + str(pcsonsouth))
      if northarea != 0:
        pcsonnorth = northarea // _hyndai1pcarea
        northkW = pcsonnorth * _hyndai1pcpower
        st.caption("Number of panels on N: " + str(pcsonnorth))      
      totalpcs = pcsonsouth + pcsonnorth                              #add up both sides of the roof
      totalkW = southkW + northkW
    elif brand == "JINKO":
      if southarea != 0:
        pcsonsouth = southarea // _jinko1pcarea
        southkW = pcsonsouth * _jinko1pcpower
        st.caption("Number of panels on S: " + str(pcsonsouth))
      if northarea != 0:
        pcsonnorth = northarea // _jinko1pcarea
        northkW = pcsonnorth * _jinko1pcpower
        st.caption("Number of panels on N: " + str(pcsonnorth)) 
      totalpcs = pcsonsouth + pcsonnorth
      totalkW = southkW + northkW
    st.caption("Total number of panels: " + str(totalpcs))
    st.caption("Total system power: " + str("%.2f" % totalkW) + "kW")

  years = st.slider("Number of years for income calculation:", 1, 10)

st.write = ("")
with col2:
  st.text = ('Hello World')
  
  
  
  
  
  
  
