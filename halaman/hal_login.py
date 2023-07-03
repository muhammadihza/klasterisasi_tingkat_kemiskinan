import streamlit as st
from atribut.authentifikasi.login import login as login

def login_page():
    st.set_page_config(page_title="Login", page_icon='📈')
    st.title("Login")

    # Form Login
    with st.form('Form Login'):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submit_button = st.form_submit_button('Login')


    # Tombol jika ingin daftar
    cols1, cols2 = st.columns([1, 2.2])  
    
    with cols1:
        st.write('')
        st.write("Belum mendaftar sebuah akun?")

    with cols2:
        # st.write("[Klik di sini untuk mendaftar](https://example.com)")
        st.write('')
        tombol_daftar = st.button('Daftar')

        if tombol_daftar:
            st.session_state.current_page = "page_two"

       
     # Tombol submit login
    if submit_button:
        result = login(username, password)
        if result:
            
            if 'user_name' not in st.session_state:
                st.session_state.user_name = ''

            st.session_state.user_name = result[1]
            st.success("**Berhasil Login!**")
            st.session_state.current_page = "page_three"

        else:
            st.error("Invalid username or password")