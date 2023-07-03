import streamlit as st
import pymysql

def create_connection():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='user'
    )
    return connection

# Fungsi untuk melakukan registrasi
def register(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    # insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    # cursor.execute(insert_query, (username, password))
    # connection.commit()
    # cursor.close()
    # connection.close()
    
    select_query = f"SELECT * FROM users WHERE username='{username}'"
    cursor.execute(select_query)
    result = cursor.fetchone()

    if result:
        st.error('Username sudah ada, **Registrasi Gagal!**')
    
    else:
        # Tambahkan data pengguna baru ke tabel pengguna
        insert_query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
        cursor.execute(insert_query)
        connection.commit()
        cursor.close()
        connection.close()

        st.success("**Registrasi Berhasil!** Klik tombol register kembali untuk pindah ke halaman login")
        st.session_state.current_page = "page_one"
        