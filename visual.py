#import libraries
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns
#Remove Warnings
st.balloons()

# SIDE Bar
st.sidebar.header("Streamlit Assignment")
st.sidebar.subheader("Nijithkamal")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Tips_Dataset")

#import dataset
df = pd.read_csv('titanic.csv')
#First thirty rows
tips = df.head(10)
#Display the table
st.table(tips)

#pairplot
st.subheader("Pairplot")
sns.pairplot(tips,hue='Sex',palette='rainbow')
st.pyplot()

#Correation
st.subheader("Heatmap")
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
st.pyplot()

#lineplot
st.subheader("lineplot")
sns.set_theme(style="darkgrid")
sns.lineplot(x="Survived", y="Age", hue="Sex", data=df)
st.pyplot()