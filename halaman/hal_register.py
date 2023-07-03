import streamlit as st
from atribut.authentifikasi.register import register as register

def register_page():

    st.set_page_config(page_title="Register", page_icon='📈')
    st.title("Register")

    with st.form('Form Register'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        register_button = st.form_submit_button('Register')

    # Tombol Login
    cols1, cols2 = st.columns([1, 4])  
    
    with cols1:
        st.write('')
        st.write("Sudah daftar akun?")

    with cols2:
        st.write('')
        tombol_login = st.button('Login')

        if tombol_login:
            st.session_state.current_page = "page_one"

       
    # Tombol daftar 
    if register_button:
        
        if username == '':
            st.write('')
            st.warning('Silahkan masukkan username anda')

        elif len(username) < 5:
            st.write('')
            st.warning('Username terlalu pendek, silahkan membuat username dengan 5 karakter atau lebih')

        elif password == '':
            st.write('')
            st.warning('Silahkan masukkan password anda')

        elif len(password) < 5:
            st.write('')
            st.warning('Password terlalu pendek, disarankan untuk membuat password dengan 5 karakter atau lebih')


        else:
            register(username, password)