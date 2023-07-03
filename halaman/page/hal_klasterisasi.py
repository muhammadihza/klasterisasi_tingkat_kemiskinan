import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler 

from atribut.mark import simple_mark as sm

from atribut.klasterisasi.info import info as info
from atribut.klasterisasi.normalisasi_data import change_data as change
from atribut.klasterisasi.kmeans_1 import kmeans_1 as kmeans_1
from atribut.klasterisasi.kmeans_2 import kmeans_2 as kmeans_2
from atribut.labeling_hasil import labeling_result as lr


def klaster_page():
    
    data_awal = st.session_state.upload_file.copy()

    st.title("Klasterisasi 📈" )
    st.write('')
    st.write('')


    if 'data_baru' not in st.session_state:
        st.session_state.data_baru = ''

    jenis_data = st.session_state.jenisData

    if jenis_data == 'DataKemiskinan':

        st.subheader('(*) Pemberian Nilai Bobot Data')

        pembobotan = st.radio(
            # "👇 Melakukan pembobotan nilai atribut secara : ",
            "Pembobotan nilai atribut secara : ",
            ["Manual", "Otomatis"],
            horizontal=True
        )

        if pembobotan == "Manual":

            bobot = 0
            df = change(data_awal.copy(), bobot)

            scaler = StandardScaler()
            df_scaled = scaler.fit_transform(df)
            df_scaled = pd.DataFrame(df_scaled, columns=df.columns)  
            st.session_state.data_baru = df_scaled

            
        else:

            bobot = 1
            df = change(data_awal.copy(), bobot)
            st.write(df)

            scaler = StandardScaler()
            df_scaled = scaler.fit_transform(df)
            df_scaled = pd.DataFrame(df_scaled, columns=df.columns)  
            st.session_state.data_baru = df_scaled

    else:

        seleksikolum = data_awal.copy()
        string_columns = seleksikolum.select_dtypes(include='object').columns
        
        # Menghapus kolom-kolom dengan tipe data string
        df = seleksikolum.drop(columns=string_columns)
        df = pd.DataFrame(df)
        st.session_state.data_baru = df


    data = st.session_state.data_baru

    sm()


    # ---------------------------- Opsi Klasterisasi --------------------------
    st.subheader('(*) Tentukan Jumlah Klaster')

    n_klaster = st.slider('Tentukan jumlah klaster', min_value=2, max_value=6, value=3)

    sm()

    # ---------------------------- Mendefiniskan centroid ---------------------
    st.subheader('(*) Tentukan nilai centroid untuk masing masing klaster')
    centroid_indices = []
    for i in range(n_klaster):
        index = st.number_input(f"Indeks nilai Centroid {i+1}", value=i+1, step=1)
        centroid_indices.append(index)


    # Mendefiniskan centroid secara manual
    centroids = data.values[centroid_indices]

    # Perform K-Means clustering
    labels, final_centroids = kmeans_2(data.values, centroids)
        
    # Create a DataFrame with the cluster labels
    data_with_labels = data_awal.copy()
    data_with_labels['Cluster'] = labels
    
    sm()

    # ---------------------------- Labeling Klaster --------------------------
    st.subheader('(*) Tentukan Nama Label Klaster')
    df_klaster = lr(n_klaster, data_with_labels)


    sm()
    
    proses =  st.button('Lihat Hasil')

    if proses:

        st.session_state.halaman2 = 1
        # ------------------------ Hasil K-Means ---------------------- #

        st.write(df_klaster)

        if 'data' not in st.session_state:
            st.session_state.data = ''   
        st.session_state.data = df_klaster

        st.success('Berhasil memproses!! Silahkan ke halaman dashboard untuk melihat hasil.', icon="✅")
