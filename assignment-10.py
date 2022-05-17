# Noah Foster
# MISY262, Section 012, Assignment 10

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.set_page_config(page_title = 'NF MISY262', page_icon = ':cat:', menu_items = {'Get Help': None, 'Report a Bug': None, 'About': '![Oogie](https://cdn.discordapp.com/attachments/618611702069723136/975832091285684274/IMG_4846.JPG)'}) # Click on the link.

st.title('MISY262 Assignment 10')
st.subheader('Noah Foster')
st.write('*Selected California Housing Data from 1990*')
housing = pd.read_csv('housing.csv')

price_filter = st.slider('Median House Price: ', 0.0, housing.median_house_value.max(), 200000.0)
location_filter = st.sidebar.multiselect('Choose a location type: ', housing.ocean_proximity.unique(), housing.ocean_proximity.unique())
income_filter = st.sidebar.radio('Choose an income level: ', ('Low', 'Medium', 'High'))

housing = housing[housing.median_house_value <= price_filter]
housing = housing[housing.ocean_proximity.isin(location_filter)]
if income_filter == 'Low':
    housing = housing[housing.median_income <= 2.5]
elif income_filter == 'Medium':
    housing = housing[(housing.median_income <= 4.5) & (housing.median_income > 2.5)]
elif income_filter == 'High':
    housing = housing[housing.median_income > 4.5]

st.subheader('See more filters in the sidebar.')
st.map(housing)

st.subheader('Histogram of the Median House Value: ')
fig, ax = plt.subplots()
housing.median_house_value.plot.hist(bins = 30).set(ylabel = None)
st.pyplot(fig)