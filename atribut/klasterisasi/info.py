import streamlit as st
from atribut.mark import simple_mark as sm


def info(item, k, df):

    if item == 1:

        with st.expander("**⬇️ DETAIL DATA**"):
                sm()
                st.write('Jumlah Klaster : ', k)
                st.write('*Karena menggunakan index, maka penamaan kelompok dimulai dari nilai' 
                         '0, 1, 2... dan seterusnya*')
                if k == 2:
                        st.write('( 1 = *Tinggi* )')
                        st.write('( 0 = *Rendah* )')
                        
                elif k == 3:
                        st.write('( 0 = *Tinggi* )')
                        st.write('( 1 = *Sedang* )')
                        st.write('( 2 = *Rendah* )')

                elif k == 4:
                        st.write('( 1 = *Sangat Tinggi* )')
                        st.write('( 2 = *Tinggi* )')
                        st.write('( 3 = *Sedang* )')
                        st.write('( 0 = *Rendah* )')
  
                elif k == 5:
                        st.write('( 4 = *Sangat Tinggi* )')
                        st.write('( 0 = *Tinggi* )')
                        st.write('( 1 = *Sedang* )')
                        st.write('( 2 = *Rendah* )')
                        st.write('( 3 = *Sangat Rendah* )')  
                sm()


                col1, col2= st.columns(2)
                with col1:
                    st.write('Jumlah Baris')
                    a = df.shape[0]
                    st.info(a)

                with col2:
                    st.write('Jumlah Kolom')
                    b = df.shape[1]
                    st.info(b)
        st.write(df)


    if item == 2:

        kol2_1, kol2_2 = st.columns(2)
        with kol2_1:
            st.write(df)

        with kol2_2:
            with st.expander("**⬇️ DETAIL DATA**"):
                sm()
                st.write('**Jumlah Klaster**')
                st.info(k)
                st.write('*Karena menggunakan index, maka penamaan kelompok dimulai dari nilai 0, 1, 2... dan seterusnya*')

                if k == 2:
                    st.write('( 1 = *Besar* )')
                    st.write('( 0 = *Kecil* )')
                        
                elif k == 3:
                    st.write('( 1 = *Besar* )')
                    st.write('( 2 = *Sedang* )')
                    st.write('( 0 = *Kecil* )')

                elif k == 4:
                    st.write('( 0 = *Sangat Besar* )')
                    st.write('( 2 = *Besar* )')
                    st.write('( 3 = *Sedang* )')
                    st.write('( 1 = *Kecil* )')
                       

                elif k == 5:
                    st.write('( 4 = *Sangat Besar* )')
                    st.write('( 1 = *Besar* )')
                    st.write('( 2 = *Sedang* )')
                    st.write('( 3 = *Kecil* )')
                    st.write('( 0 = *Sangat Kecil* )')
                        
                sm()

                st.write('**Jumlah Baris**')
                a = df.shape[0]
                st.info(a)

                st.write('**Jumlah Kolom**')
                b = df.shape[1]
                st.info(b)