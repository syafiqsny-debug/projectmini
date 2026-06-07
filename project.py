import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("""Welcome to my Dashboard
This is my first time using streamlit.""")

DF = pd.read_csv('bmw (1).csv')
st.subheader("Raw Data")
st.write(DF)

DF.isnull().sum()
DF.dropna(inplace = True)
DF.duplicated().sum()
DF.drop_duplicates(inplace = True)
DF = DF[DF['year'] >= 2019]
DF = DF.rename(columns={'model': 'Model','year' : 'Year', 'price':'Price', 'transmission':'Transmission', 'mileage':'Mileage'})
DF = DF[DF['fuelType']== 'Petrol']


st.subheader("Histogram")
column = st.selectbox("Choose a column",DF.columns)
fig, ax = plt.subplots(figsize = (10,6))
DF[column].plot(kind = 'hist', ax =ax)
st.pyplot(fig)
fig = px.histogram(DF, x=column)
fig.update_traces( marker = {"color":"purple", "line":{"color":"black","width":2}})
st.plotly_chart(fig)

st.subheader("Scatter Chart")
x_column = st.selectbox("Choose x-axis column",DF.columns)
y_column = st.selectbox("Choose y-axis column",DF.columns)
fig, ax = plt.subplots(figsize = (10,6))
DF.plot(kind = 'scatter', x=x_column, y=y_column, ax =ax)
st.pyplot(fig)