# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

Car_prices = pickle.load(open('C:/Users/Danish/Desktop/Python ML Projects/Car_Prices.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Car Prices Prediction using ML',
                          
                          ['Price Prediction'], icons=['car'], default_index=0)
    
    

    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        year = st.text_input('Car Registration Year')
        
    with col2:
        km_driven = st.text_input('Km_Driven')
    
    with col3:
        fuel = st.text_input('Fuel Type')
    
    with col1:
        seller_type = st.text_input('Seller Type')
    
    with col2:
        transmission = st.text_input('Transmission Type')
    
    with col3:
        owner = st.text_input('Owner')
    
  
    
    
    # code for Prediction
    Car_Prices1 = ''
    
    # creating a button for Prediction
    
st.button('Car Price Prediction')

prediction = float(Car_prices.predict([[year,km_driven,fuel,seller_type,transmission,owner]]))
        
print(prediction)
st.success(Car_Prices1)
