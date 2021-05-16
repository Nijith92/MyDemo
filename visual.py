#import libraries
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import time
#matplotlib.use('Agg')
import seaborn as sns
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
# SIDE Bar
st.sidebar.header("STREAMLIT APP")
st.sidebar.subheader("Select your option")

option = st.sidebar.selectbox( '',('Intro','Table', 'Pairplot', 'Heap','Lineplot'))

# import dataset
df = pd.read_csv('titanic.csv')
# First ten rows
tips = df.head(10)

st.title("Welcome to the Demo Streamlit App")

# SIDE Bar
my_bar = st.progress(0)

if (my_bar.progress == 0):
    st.write("wait..")
else:
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
    st.write("completed loading..")

#Disaplay Intro
if ( option == 'Intro'):

    st.markdown('In this app a data sheet is integrated')
    st.markdown('** 3 charts ** have been drawn based on the same')
    st.markdown('The data sheets is of  the passengers  travelled in ** Titanic **')
    st.markdown('You can select the option from the side bar')

#Display the table
elif (option == 'Table' ):
    with st.beta_container():
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.title("Tips_Dataset")
        st.table(tips)


#pairplot
elif (option == 'Pairplot' ):

    with st.beta_container():
        st.subheader("Pairplot")
        sns.pairplot(tips,hue='Sex',palette='rainbow')
        st.pyplot()

#Correation
elif (option == 'Heap'):

    with st.beta_container():
        st.subheader("Heatmap")
        sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
        st.pyplot()

#lineplot
elif (option == "Lineplot"):

    with st.beta_container():
        st.subheader("lineplot")
        sns.set_theme(style="darkgrid")
        sns.lineplot(x="Survived", y="Age", hue="Sex", data=df)
        st.pyplot()