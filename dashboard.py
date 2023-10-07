import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

st.title('Dashboard Bike Sharing')
df = pd.read_csv('all_data.csv')

df['dteday'] = pd.to_datetime(df['dteday'])
df2011 = df[df["dteday"].dt.year == 2011]

df['dteday'] = pd.to_datetime(df['dteday'])
df2012 = df[df["dteday"].dt.year == 2012]

option = st.sidebar.selectbox(
    'Jumlah pengguna Sepeda:',
    ('Pada Tahun 2011-2012','Registered(terdaftar)','Casual(tidak terdaftar)')
)

if option == 'Pada Tahun 2011-2012' or option == '':
    st.header(""" Jumlah Pengguna Sepeda Pada Tahun 2011 - 2012""") 
    df['dteday'] = pd.to_datetime(df['dteday'])
    df['yr'] = df['dteday'].dt.year
    yearly_counts = df.groupby('yr')['cnt'].sum()
    plt.figure(figsize=(10, 6))
    yearly_counts.plot(kind='bar', color='blue')
    plt.title('Tren Penggunaan Sepeda (Bike Sharing) per Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Jumlah Sepeda Disewakan')
    st.pyplot(plt)

elif option == 'Registered(terdaftar)':
    st.subheader(""" Pengguna sepeda yang terdaftar(Registered)""") 
    sum_2011 = df2011['registered'].sum()
    sum_2012 = df2012['registered'].sum()

    # Membuat barchart
    fig, ax = plt.subplots()
    ax.bar(['2011', '2012'], [sum_2011, sum_2012])
    ax.set_title('Perbandingan Pengguna Registred Tahun 2011 dan 2012')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Rata-Rata Pengguna Terdaftar')
    st.pyplot(fig)  
   
    fig, axs = plt.subplots(1, 2, figsize=(10, 7))

# Data dan plot untuk tahun 2011

    group = df2011[['casual', 'registered']].mean()
    axs[0].pie(group, labels = group.index, autopct='%1.1f%%')
    axs[0].set_title('(2011)')
#Data untuk tahun 2012
    grouped = df2012[['casual', 'registered']].mean()
    axs[1].pie(grouped, labels = grouped.index, autopct='%1.1f%%')
    axs[1].set_title('(2012)')
    st.pyplot(fig)

elif option == 'Casual(tidak terdaftar)':
    st.subheader("Pengguna Sepeda yang tidak terdaftar(Casual)") 
    sum_casual_2011 = df2011['casual'].sum()
    sum_casual_2012 = df2012['casual'].sum()

    fig, ax = plt.subplots()
    ax.bar(['2011', '2012'], [sum_casual_2011, sum_casual_2012])
    ax.set_title('Perbandingan Pengguna Casual Tahun 2011 dan 2012')
    ax.set_xlabel('Tahun')
    ax.set_ylabel('Jumlah Pengguna tidak Terdaftar')
    st.pyplot(fig) 

    fig, axs = plt.subplots(1, 2, figsize=(10, 7))

# Data dan plot untuk tahun 2011

    group = df2011[['casual', 'registered']].mean()
    axs[0].pie(group, labels = group.index, autopct='%1.1f%%')
    axs[0].set_title('(2011)')
#Data untuk tahun 2012
    grouped = df2012[['casual', 'registered']].mean()
    axs[1].pie(grouped, labels = grouped.index, autopct='%1.1f%%')
    axs[1].set_title('(2012)')
    st.pyplot(fig)
