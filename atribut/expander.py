import streamlit as st

def expander(df):

    st.subheader('Dataset')
    st.write('Data set yang telah diinputkan dapat dilihat pada dataframe dibawah ini :')
    st.dataframe(df)
    
    with st.expander("**⬇️ LIHAT DETAIL DATA**"):

        st.markdown('---')

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write('Tipe Data Kolom')
            st.dataframe(df.dtypes)

        with col2:
            st.write('Jumlah Baris')
            a = df.shape[0]
            st.info(a)

        with col3:
            st.write('Jumlah Kolom')
            b = df.shape[1]
            st.info(b)