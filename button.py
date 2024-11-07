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

sentence = st.text_input('Input your sentence here:') 

if sentence:
    st.write(my_model.predict(sentence))



    if option == ‘Text Summarization’:

    max_lengthy = st.slider('Maximum summary length (words)', min_value=30, max_value=150, value=60, step=10)

    num_beamer = st.slider('Speed vs quality of summary (1 is fastest)', min_value=1, max_value=8, value=4, step=1)

    text = st.text_area('Enter Text Below (maximum 800 words):', height=300) 

    submit = st.button('Generate')  

    if submit:

        st.subheader("Summary:")

        with st.spinner(text="This may take a moment..."):

            summWords = sum2(text, max_length=max_lengthy, min_length=15, num_beams=num_beamer, do_sample=True, early_stopping=True, repetition_penalty=1.5, length_penalty=1.5)

        text2 =summWords[0]["summary_text"]

        st.write(text2)


#bt1=st.button('Submit')

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
