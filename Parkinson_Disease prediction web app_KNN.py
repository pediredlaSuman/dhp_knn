import numpy as np
import pickle
import streamlit as st
# loading the saved model
loaded_model = pickle.load(open("C:/Users/Suman/OneDrive/Desktop/Minor/trained_model_Parkinson_sav_svm",'rb'))
# creating a function for Prediction
def Parkinson_Disease_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
      return 'The person does not has Parkinson'
    else:
      return 'The person has Parkinson'
def main():
      # giving a title
      st.title('Parkinson_Disease Prediction Web App')
      # getting the input data from the user
      Fo= st.text_input('Fo')
      Fhi = st.text_input('Fhi')
      Flo= st.text_input('Flo')
      RAP = st.text_input('RAP')
      PPQ = st.text_input('PPQ')
      DDP= st.text_input('DDP')
      Shimmer=st.text_input('Shimmer')    
      Shimmer_dB=st.text_input('Shimmer_dB')
      Shimmer_APQ3=st.text_input('Shimmer_APQ3')
      Shimmer_APQ5=st.text_input('Shimmer_APQ5')
      APQ=st.text_input('APQ')
      Shimmer_DDA=st.text_input('Shimmer_DDA')
      NHR=st.text_input('NHR')
      HNR=st.text_input('HNR')
      RPDE=st.text_input('RPDE')
      DFA=st.text_input('DFA')
      # code for Prediction
      Parkinson = ''
      # creating a button for Prediction
      if st.button('Parkinson_Disease Test Result'):
       Parkinson =Parkinson_Disease_prediction([Fo,Fhi,Flo,RAP,PPQ,DDP,Shimmer,Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA])
      st.success(Parkinson)
if __name__ == '__main__':
     main()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

