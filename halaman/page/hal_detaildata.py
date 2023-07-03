import streamlit as st
from atribut.expander import expander as expander

def detaildata_page(df):

    st.title('Detail Data📈')
    st.markdown('---')
                
    expander(df)