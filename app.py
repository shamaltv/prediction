import streamlit as st 
import pandas as pd
import numpy as np
import pickle


st.title('Predicting the Species Based on Measurements')
model= pickle.load(open('iris.pkl','rb'))

#user input

sepal_length=st.number_input('sepal length (cm)')
sepal_width=st.number_input('sepal width (cm)')
petal_length=st.number_input('petal length (cm)')
petal_width=st.number_input('petal width (cm)')

user_data = pd.DataFrame({'sepal length (cm)':sepal_length,
                         'sepal width (cm)':sepal_width,
                         'petal length (cm)':petal_length,
                         'petal width (cm)':petal_width},index=[0])


prediction=model.predict(user_data)
if st.button('Predict'):
    st.write(f'The predicted Iris Species is {prediction}')