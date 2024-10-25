# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:34:29 2024

@author: Alumne_mati1

Activitat 3

Pensa un formulari i programa`l amb streamlit.
Posa el teu nick name com a nom de l’aplicació.
Recorda arrencar el programa a la consola amb el nom que li has posat
streamlit run nick-name.py
"""

# Import streamlit Library
import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




# #------ Declaration of Definition -------

# def triangle_of_power (parameter_active_power, parameter_reactive_power):
    
#     apparent_power = math.sqrt(parameter_active_power**2 + parameter_reactive_power**2)
    
#     return apparent_power

# #def cosphi (parameter_active_power, parameter_reactive_power):
#     #cosphi_tang = math.atan(parameter_reactive_power/parameter_active_power)
# #    cosphi_tang = math.tan(parameter_reactive_power/parameter_active_power)
    
# #    return cosphi_tang

# def active_power_output (parameter_voltage, parameter_current,tang_phi):
    
#     #angle_phi = math.atan(tang_phi)
#     angle_degree = math.degrees(tang_phi)
#     cos_phi      = math.cos(math.radians(angle_degree))
#     sinus_phi    = math.sin(math.radians(angle_degree))
#     print(angle_degree)
#     #print(cos_phi)
#     #print(sinus_phi)
#     print("bring Values")
   
#     print ("Inside def Voltage",parameter_voltage)
#     print ("Inside def Current",parameter_current)
    
#     calculated_active_power = math.sqrt(3)*parameter_voltage*parameter_current*cos_phi
#     calculated_reactive_power = math.sqrt(3)*parameter_voltage*parameter_current*sinus_phi
        
#     return calculated_active_power,calculated_reactive_power



# #------- Variables -------
# apparent_power = 0 
# #cosphi_tang    = 0
# calculated_active_power   = 0
# calculated_reactive_power = 0
# tang_phi       = 0.434 # Angle is similar than 25 degree
taula_images = {''}
var_iloc_P     = []
var_iloc_Q     = []
var_iloc_time  = []
        
        
#-----------------Upload CSV file ----------------------------------

WTG_File_df = pd.read_csv("WTG_Step.csv")  # read a CSV file inside the 'data" folder next to 'app.py'
#df_WTG_File = pd.read_excel(WTG_File_df)  # will work for Excel files
st.write(WTG_File_df)
st.title("Instantaneous Performance of Wind Turbines")  # add a title

st.header("Analysis of Grid Compliance Tests based in the IEC International Standard")# add a Header fro Title
  
#--------------Sidebar---------------
is_wind = st.sidebar.selectbox(
    "International Standard: Wind turbines –Part 21",
    ("Active Power", "Reactive Power", "FRT for LVRT", "FRT for HVRT", "PQ capability","Tolerance Band")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose Requeriment:",
        ("Pass", "No Passed")
    )    

#---------Split Screen into 2 Columns Comparation

col_Req_1, col_Data_2 = st.columns(2)

with col_Req_1:

#--------------Import png file----------
# Adding Requeriment Images and create a Table
#   I can sellect the image
    try: 

        taula_images = { "Active Power"  :"ActiveSet_Point.png", 
                     "Reactive Power":"Reactive_set_point.png",
                     "FRT for LVRT"  :"LVRT.png", 
                     "FRT for HVRT"  :"HVRT.jpg",
                     "PQ capability" :"PQ_Capability.png",
                     "Tolerance Band":"Tole_band.png"}
    
#--- I select the image from the folder using the Sidebar Selector (above)
   
        image_name = "./img/"+ taula_images[is_wind]
   
    ####-- Header and Subheader
        st.subheader("Requeriment Selected:"  + is_wind)
        st.image(image_name, caption= is_wind)
    
    except Exception as e:
        st.error(" No he pogut carregar la imatge" + image_name)
        print (e)


with col_Data_2:
    if is_wind == "Active Power":
        # ---Varible for the ILOC[]
        var_iloc_time  = WTG_File_df.iloc[2:,0]
        var_iloc_P = WTG_File_df.iloc[2:,1]
        print(var_iloc_time)
        
                
        '## multi select'



        #st.subheader("Requeriment Selected:"  + is_wind)
        #st.image(image_name, caption= is_wind)
        
    
    
    
#         item_quantity = st.number_input("Item Quantity (pieces)",value=0)
#         box_quantity = st.number_input("Box Quantity (pieces)",value=0)
#         total_weight = st.number_input("Total Weight (kgs)",value=weight*box_quantity)
#         cbm = st.number_input("CBM (m3)",value=(((length*width*height)/1000000)*box_quantity))
        
        


#--------------Import image to be linked with the requeriment---------------






#  I have to select the first and second parameter of each table by selecting the name 






#parameter_active_power   = Wind_Farm[WF_choice]['Active Power']
#parameter_reactive_power = Wind_Farm[WF_choice]['Reactive Power']

#apparent_power = round(triangle_of_power(parameter_active_power,parameter_reactive_power),2)

# Print the result from the First choose value and the Apparent Power
#st.write (f"The analysed value is {Wind_Farm[WF_choice][parameter_select]}, \n The Aparent Power is {apparent_power}")

#st.write (f"The Aparent Power is {apparent_power}")



