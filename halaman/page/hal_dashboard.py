import streamlit as st
from streamlit import components
import pandas as pd  # pip install pandas
import numpy as np
import plotly.express as px  # pip install plotly-express
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import base64  # Standard Python Module
import io
from io import StringIO, BytesIO  # Standard Python Module
import xlsxwriter

# Import fungsi
from atribut.mark import simple_mark as mk
from atribut.grafik.unduh_chart import download_bar_chart as unduh

def dashboard_page():

    st.title("Dashboard 📉" )
    st.markdown('---')
    st.write('Hasil dari pengklasteran data menggunakan K-Means ditampilkan pada tabel dan grafik dibawah ini: ')

    # -------------- Inisialisasi Data -------------------- #
    data = st.session_state.data

    data_akhir = data.copy()

    # Menyeleksi Kategori
    string_kolom1 = data_akhir.select_dtypes(include=['int','float'])
    string_kolom2 = data_akhir.select_dtypes(include='object')

    nama_kolom = string_kolom2.columns.tolist()
    nama_kolom2 = string_kolom1.columns.tolist()
    
    kategori1 = st.selectbox(
        'Lihat Kelompok Data Berdasarkan Kategori 1: ',
        (nama_kolom)
    )
    kategori2 = st.selectbox(
        'Lihat Kelompok Data Berdasarkan Kategori 2: ',
        (nama_kolom2)
    )

    mk()

    st.subheader('(*) Tabel')
    klaster1 = st.multiselect(
                "Pilih untuk : " + kategori1,
                options=data_akhir[kategori1].unique(),
                default=data_akhir[kategori1].unique()
            )
    
    klaster2 = st.multiselect(
                "Pilih untuk : " + kategori2,
                options=data_akhir[kategori2].unique(),
                default=data_akhir[kategori2].unique()
            )


    if kategori1 and kategori2:
        data_seleksi = data_akhir.query("`{}` == @klaster1 and `{}` == @klaster2".format(kategori1, kategori2))

    # Tampilan Tabel
    with st.expander('Lihat Tabel', expanded=True):
        st.write(data_seleksi)


    # Menampilkan Grafik Bentuk Pie
    mk()
    st.subheader('(*) Grafik')

    pie_chart = px.pie(data_seleksi,
        title='Presentase Tingkat Kemiskinan Berdasarkan : ' + kategori2,
        values=kategori2,
        names='Cluster')
    
    st.plotly_chart(pie_chart)
    st.info('Grafik diatas, kelompok ditampilkan berdasarkan pilihan **kategori2**')


    
    # Menampilkan Grafik Bentuk Bar
    nama_kolom3 = data_akhir.columns.tolist()
    mk()
    kategori3 = st.selectbox(
        'Lihat Data : ',
        (nama_kolom3)
    )

    st.write('')
    st.write('')

    col1, col2 = st.columns([2, 1.2])

    with col1:
        # Menghitung jumlah masing-masing atribut unik
        count = data_seleksi[kategori3].value_counts()

        # Membuat bar chart menggunakan Streamlit
        st.bar_chart(count)


    with col2:

        tipe_int = data_seleksi.select_dtypes(include=['int', 'float'])

        if kategori3 in tipe_int.columns:

            # Mencari nilai tertinggi, rata-rata, terendah
            nilai_tertinggi = data_seleksi[kategori3].max()
            nilai_rata_rata = data_seleksi[kategori3].mean()
            nilai_terendah = data_seleksi[kategori3].min()

            with st.expander('Lihat Detail'):

                st.info('**Nilai rata-rata pada**   ' + kategori3 + ' : ' + str(nilai_rata_rata))
                st.info('**Nilai tertinggi**   ' + kategori3 + ' : ' + str(nilai_tertinggi))
                st.info('**Nilai terendah**   ' + kategori3 + ' : ' + str(nilai_terendah))
        
        else:
            # Melihat label paling banyak muncul
            labMax = data_seleksi[kategori3].value_counts().idxmax()

            # Melihat label paling sedikit muncul
            labMin = data_seleksi[kategori3].value_counts().idxmin()


            with st.expander('Lihat Detail', expanded=True):

                st.write('Terbanyak muncul : ', labMax)
                st.write('Paling sedikit muncul : ', labMin)


    st.subheader('Donwload :')

    option = st.selectbox(
        'Pilih format data',
        ('1. Bar Chart', '2. Tabel(csv)'))
    
    if option == '1. Bar Chart':

        courses = list(set(data_seleksi[kategori3]))
        values = [data_seleksi[kategori3].value_counts()[course] for course in courses]
        n = 1

        unduh(courses, values, kategori3, n)

    if option == '2. Tabel(csv)':

        df = pd.DataFrame(data_seleksi)

        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="Data.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)