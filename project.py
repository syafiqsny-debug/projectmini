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
DF = DF.rename(columns={'model': 'Model','year' : 'Year', 'price':'Price', 'transmission':'Transmission', 'mileage':'Mileage', 'mpg':'MilesperGallon'})
DF = DF[DF['fuelType']== 'Petrol']




st.subheader("Histogram")

fig, ax = plt.subplots(figsize=(10, 6))

DF['MilesperGallon'].plot(kind='hist', 
                    ax=ax)

plt.title('Histogram Plot')

plt.xlabel('MilesperGallon')
plt.ylabel('Frequency')
st.pyplot(fig)


st.subheader("Scatter Chart")
fig, ax = plt.subplots(figsize = (8, 6))

# scatter plot
DF.plot(kind='scatter',
        x='Model',
        y='Price',
        color = 'blue',
        ax=ax)
 
# set the title
plt.title('ScatterPlot')

ax.set_xticklabels(DF['Model'], rotation=45) 

st.pyplot(fig)
