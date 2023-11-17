# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 16:12:26 2023

@author: Suman
"""
import numpy as np
import pickle
import streamlit as st
# loading the saved model
loaded_model = pickle.load(open('C:/Users/Suman/OneDrive/Desktop/Minor/trained_model_heart_sav_svm','rb'))
# creating a function for Prediction
def Heart_Disease_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
      return 'The person does not has heart_attck'
    else:
      return 'The person has heart_attck'
def main():
      # giving a title
      st.title('Heart_Disease Prediction Web App')
      # getting the input data from the user
      age= st.text_input('Age')
      sex = st.text_input('sex')
      cp= st.text_input('cp')
      trestbps = st.text_input('trestbps')
      chol = st.text_input('chol')
      fbs = st.text_input('fbs')
      restecg = st.text_input('restecg')
      thalach= st.text_input('thalach')
      exang=st.text_input('exang')    
      oldpeak=st.text_input('oldpeak')
      slope=st.text_input('slope')
      ca=st.text_input('ca')
      thal=st.text_input('thal')
      # code for Prediction
      heart_attack = ''
      # creating a button for Prediction
      if st.button('heart_Disease Test Result'):
        heart_attack =Heart_Disease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
         
      st.success(heart_attack)
if __name__ == '__main__':
     main()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

