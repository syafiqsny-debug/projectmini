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

numeric_columns = DF.select_dtypes(include=['int64', 'float64']).columns.tolist()
column = st.selectbox("Choose a numeric column for the histogram", numeric_columns, key="hist_column_select")

fig_plotly = px.histogram(DF, x=column, title=f"Plotly Distribution of {column}")
fig_plotly.update_traces(marker={"color": "purple", "line": {"color": "black", "width": 2}})

# Fix the x-axis range based on the minimum and maximum values of the selected column
fig_plotly.update_layout(
    xaxis_range=[DF[column].min(), DF[column].max()]
)

st.plotly_chart(fig_plotly)

st.subheader("Scatter Chart")
x_column = st.selectbox("Choose x-axis column",DF.columns)
y_column = st.selectbox("Choose y-axis column",DF.columns)
fig, ax = plt.subplots(figsize = (10,6))
DF.plot(kind = 'scatter', x=x_column, y=y_column, ax =ax)
ax.tick_params(axis='x', labelrotation=45)
st.pyplot(fig)
