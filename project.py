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
                           edgecolor = 'black',
                    ax=ax)

plt.title('Histogram Plot')

plt.xlabel('MilesperGallon')
plt.ylabel('Frequency')
st.pyplot(fig)

st.write("""This histogram displays a bimodal, left-skewed distribution for the MilesperGallon variable across a range of approximately 23 to 58 MPG.
The data is characterized by two distinct frequency peaks—a minor peak around 41–43 MPG and a primary, tallest peak around 48–50 MPG—separated by a noticeable drop in frequency near 45 MPG.
This bimodal behavior strongly suggests the dataset contains two distinct subgroups of vehicles, such as standard internal combustion engines versus highly efficient hybrids,
while the elongated tail to the left indicates a smaller group of lower-efficiency vehicles extending down toward 23 MPG.""")


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
st.write("This scatter plot displays vehicle Price across different vehicle Model categories (specifically BMW models), revealing a highly fragmented x-axis with repeating, overlapping labels (e.g., multiple separated columns for "2 Series" and "1 Series") that indicates the categorical data needs to be aggregated or cleaned. Looking past the labeling issue, prices generally range from a low of around $12,000 to a peak of $90,000, with high-performance models like the "M4" commanding the highest price clusters between $60,000 and $90,000. In contrast, entry-level groups like the early "1 Series" and "2 Series" columns show tight vertical distributions concentrated safely below $40,000, highlighting a clear premium tiering system across different model variants.")
