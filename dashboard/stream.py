import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load bike_data (dummy data, Anda harus mengganti ini dengan data sebenarnya)
# bike_data = pd.read_csv('nama_file.csv')
bike_data = pd.read_csv('dashboard/clean.csv')  # Ganti nama file sesuai kebutuhan
bike_data['date'] = pd.to_datetime(bike_data['date'])
bike_data = bike_data.set_index('date')
bike_data["day_of_month"] = bike_data.index.day
bike_data["day_of_week"]  = bike_data.index.dayofweek
bike_data["month"] = bike_data.index.month

df_by_month = bike_data.resample("M")["count"].sum()
day_of_week_counts = bike_data.groupby("day_of_week")["count"].mean()
day_of_week_labels = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
day_of_month_counts = bike_data.groupby("day_of_month")["count"].mean()
day_of_hour_counts = bike_data.groupby("hour")["count"].mean()
grouped_hour = bike_data.groupby(['workingday', 'hour'])['count'].mean().reset_index(name='counts')

# Visual 1
st.header('Visual 1: Jumlah Pengguna Rental Sepeda per Bulan selama 2011 - 2012')
fig1, ax1 = plt.subplots(figsize=(24, 6))
ax1.plot(df_by_month.index, df_by_month, label='Jumlah Pengguna Rental Sepeda')
ax1.annotate('Test', (df_by_month.index[0], df_by_month.iloc[0]), textcoords="offset points", xytext=(0, 5), ha='center')
ax1.legend()
st.pyplot(fig1)

# Visual 2
st.header('Visual 2: Rata-rata Pengguna Rental Sepeda per Hari dalam Seminggu')
fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(day_of_week_counts.index, day_of_week_counts)
ax2.set_xticks(day_of_week_counts.index)
ax2.set_xticklabels(day_of_week_labels)
st.pyplot(fig2)

# Visual 3
st.header('Visual 3: Jumlah Pengguna Rental Sepeda per Hari dalam Sebulan')
fig3, ax3 = plt.subplots(figsize=(24, 6))
ax3.bar(day_of_month_counts.index, day_of_month_counts)
ax3.set_xticks(np.arange(1, 32))
ax3.set_xticklabels([str(i) for i in range(1, 32)])
st.pyplot(fig3)

# Visual 4
st.header('Visual 4: Rata-rata Pengguna Rental Sepeda per Jam dalam Sehari')
fig4, ax4 = plt.subplots(figsize=(24, 6))
ax4.plot(day_of_hour_counts.index, day_of_hour_counts, label='Rata-rata Pengguna Rental Sepeda')
ax4.annotate('Test', (day_of_hour_counts.index[0], day_of_hour_counts.iloc[0]), textcoords="offset points", xytext=(0, 5), ha='center')
ax4.set_xticks(np.arange(0, 25))
ax4.set_xticklabels([str(i) for i in range(0, 25)])
ax4.legend()
st.pyplot(fig4)

# Visual 5
st.header('Visual 5: Jumlah Pengguna Rental Sepeda per Jam')
fig5, ax5 = plt.subplots(figsize=(24, 6))
for workingday, group in grouped_hour.groupby('workingday'):
    ax5.plot(group['hour'], group['counts'], label=f'Workingday: {workingday}')
ax5.set_xlabel('Hour')
ax5.set_ylabel('Jumlah Pengguna')
ax5.set_title('Jumlah Pengguna Rental Sepeda per Jam')
ax5.set_xticks(np.arange(0, 25))
ax5.legend()
st.pyplot(fig5)
