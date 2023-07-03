import streamlit as st

def simple_mark():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('---')

    with col2:
        st.markdown('---')

    with col3:
        st.markdown('---')

