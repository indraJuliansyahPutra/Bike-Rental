import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the data
bike_data = pd.read_csv('data\hour.csv')
bike_data = bike_data.rename(columns= {'dteday':'date', 'yr':'year', 'mnth':'month', 'hr': 'hour', 'weathersit': 'weather', 'hum':'humidity', 'casual': 'casual_user', 'registered': 'registered_user', 'cnt':'count'})

del bike_data['instant']

bike_data['date'] = pd.to_datetime(bike_data['date'])

bike_data = bike_data.set_index('date')

bike_data["day_of_month"] = bike_data.index.day
bike_data["day_of_week"]  = bike_data.index.dayofweek
bike_data["month"] = bike_data.index.month

# Set the title
st.title("Dashboard Analisis Data Peminjaman Sepeda")

# Create a sidebar
st.sidebar.header("Pilihan Filter")

# Create a select box for month
month = st.sidebar.selectbox("Bulan", bike_data["month"].unique())

# Create a select box for day of week
day_of_week = st.sidebar.selectbox("Hari", bike_data["day_of_week"].unique())

# Create a select box for workingday
workingday = st.sidebar.selectbox("Hari Kerja", bike_data["workingday"].unique())

# Create a select box for season
season = st.sidebar.selectbox("Musim", bike_data["season"].unique())

# Create a button to update the plots
st.sidebar.button("Perbarui")

# Plot the data
if month is not None:
    bike_data_filtered = bike_data[bike_data["month"] == month]
    fig = px.line(bike_data_filtered, x="hour", y="count", title="Jumlah Peminjaman Sepeda per Jam")
    fig.update_xaxes(tickvals=np.arange(0, 25), ticktext=[str(i) for i in range(0, 25)])
    st.plotly_chart(fig)

if day_of_week is not None:
    bike_data_filtered = bike_data[bike_data["day_of_week"] == day_of_week]
    fig = px.bar(bike_data_filtered, x="hour", y="count", title="Jumlah Peminjaman Sepeda per Jam")
    fig.update_xaxes(tickvals=np.arange(0, 25), ticktext=[str(i) for i in range(0, 25)])
    st.plotly_chart(fig)

if workingday is not None:
    bike_data_filtered = bike_data[bike_data["workingday"] == workingday]
    fig = px.bar(bike_data_filtered, x="hour", y="count", title="Jumlah Peminjaman Sepeda per Jam")
    fig.update_xaxes(tickvals=np.arange(0, 25), ticktext=[str(i) for i in range(0, 25)])
    st.plotly_chart(fig)

if season is not None:
    bike_data_filtered = bike_data[bike_data["season"] == season]
    fig = px.box(bike_data_filtered, x="hour", y="count", color="season", title="Persebaran Jumlah Peminjam di setiap musimnya")
    st.plotly_chart(fig)
