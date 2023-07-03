import streamlit as st

def logout_page():

    st.session_state["halaman"] = 0
    st.session_state.halaman2 = 0

    st.session_state.current_page = "page_one"

   