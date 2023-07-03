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


# Fungsi untuk melakukan login
def login(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    select_query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(select_query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result