# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:31:51 2024

@author: Admin01
"""
# Import streamlit Library
import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# importing subprocess module 
import subprocess
import os



with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
# Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
#if submitted:
#    st.write("slider", slider_val, "checkbox", checkbox_val)
#st.write("Outside the form")



#if st.session_state.get('button') != True:
#            st.session_state['button'] = bt1
#if st.session_state['button'] == True:
        
#            if rno not in keys_length:
#                st.warning('🚨 Roll Number Incorrect! 😱')
#            else:
#                conn=sqlite3.connect('vitap.db')
#                query='select name from vitap2 where roll_number = ?;'
#                old_name=[i[0] for i in conn.execute(query,(rno,))]
#                conn.commit()
 #               conn.close()
  #              st.success('🔑 Roll Number Correct! 🎉')
   #             new_name=st.text_input('Enter new name')
    #            if st.button('Update'):
     #               st.session_state['button'] = False
      #              st.success(updated_new_name_funcion(new_name,rno))
       #             st.balloons()
        #            st.write('Old Name: {}'.format(old_name[0]))
         #           st.write('New Name: {}'.format(new_name))
