import streamlit as st
import numpy as np

def change_data(data, bobot):

    df = data.drop(['Nama', 'Kecamatan'], axis=1)

    if bobot == 0:
        
        with st.form("Tingkat_Pendidikan"):
            st.subheader('**Nilai Bobot Tingkat Pendidikan**')
            st.write('')

            tp_1= st.number_input('Tidak Sekolah')
            tp_2 = st.number_input('SD')
            tp_3 = st.number_input('SMP')
            tp_4 = st.number_input('SMA')
            tp_5 = st.number_input('S1')
            tp_6 = st.number_input('S2')
            tp_7 = st.number_input('S3')

            st.markdown('---')
            st.subheader('**Nilai Bobot Dinding Rumah**')
            st.write('')

            dr_1 = st.number_input('Tembok')
            dr_2 = st.number_input('Kayu')
            dr_3 = st.number_input('Bambu')


            st.markdown('---')
            st.subheader('**Nilai Bobot Lantai Rumah**')
            st.write('')

            lr_1 = st.number_input('Lantai Semen')
            lr_2 = st.number_input('Lantai Keramik')
            lr_3 = st.number_input('Lantai Kayu')
            lr_4 = st.number_input('Lantai Tanah')


            st.markdown('---')
            st.subheader('**Nilai Bobot Atap Rumah**')
            st.write('')

            ar_1 = st.number_input('Rumbia')
            ar_2 = st.number_input('Seng')
            ar_3 = st.number_input('Asbes')
            ar_4 = st.number_input('Genteng')


            st.markdown('---')
            st.subheader('**Nilai Bobot Luas Lantai Rumah**')
            st.write('')

            llr_1 = st.number_input('Lebih kecil dari 8m/orang')
            llr_2 = st.number_input('Lebih besar daru 8m/orang')


            st.markdown('---')
            st.subheader('**Nilai Bobot Sumber Mata Air**')
            st.write('')

            ma_1 = st.number_input('Sumber Resapan')
            ma_2 = st.number_input('Sumber Galian')
            ma_3 = st.number_input('Sumber Pompa')
            ma_4 = st.number_input('Sumber Bor')

            st.markdown('---')
            st.subheader('**Nilai Bobot Pengeluaran Kebutuhan Pangan**')
            st.write('')

            kp_1 = st.number_input('Sebagian Kecil')
            kp_2 = st.number_input('Sebagian Besar')


            st.markdown('---')
            st.subheader('**Nilai Bobot Pengobatan Tenaga Medis**')
            st.write('')

            tm_1 = st.number_input('Kesulitan Berobat')
            tm_2 = st.number_input('Tidak Kesulitan Berobat')

            st.markdown('---')
            st.subheader('**Nilai Bobot Pembelian Pakaian**')
            st.write('')

            pp_1 = st.number_input('Kesulitan Membeli Pakaian')
            pp_2 = st.number_input('Tidak Kesulitan Membeli Pakaian')

            # Every form must have a submit button.
            st.write('')
            st.write('')
            st.form_submit_button("Submit")




        # Menetapkan Label 
            
        conditions1 = [

            (df['Tingkat Pendidikan']=='Tidak Sekolah'),
            (df['Tingkat Pendidikan']=='SD'),
            (df['Tingkat Pendidikan']=='SMP'),
            (df['Tingkat Pendidikan']=='SMA'),
            (df['Tingkat Pendidikan']=='S1'),
            (df['Tingkat Pendidikan']=='S2'),
            (df['Tingkat Pendidikan']=='S3')]
        
        choices1 = [tp_1, tp_2, tp_3, tp_4, tp_5, tp_6, tp_7]
        df['Tingkat Pendidikan'] = np.select(conditions1, choices1)
        

        conditions2 = [
            
            (df['Dinding Rumah']=='Tembok'),
            (df['Dinding Rumah']=='Kayu'),
            (df['Dinding Rumah']=='Bambu')]
        
        choices2 = [dr_1, dr_2, dr_3]
        df['Dinding Rumah'] = np.select(conditions2, choices2)


        conditions3 = [
            
            (df['Lantai Rumah']=='Semen'),
            (df['Lantai Rumah']=='Keramik'),
            (df['Lantai Rumah']=='Kayu'),
            (df['Lantai Rumah']=='Tanah')]
        
        choices3 = [lr_1, lr_2, lr_3, lr_4]
        df['Lantai Rumah'] = np.select(conditions3, choices3)


        conditions4 = [
            
            (df['Atap Rumah']=='Rumbia'),
            (df['Atap Rumah']=='Seng'),
            (df['Atap Rumah']=='Asbes'),
            (df['Atap Rumah']=='Genteng')]
        
        choices4 = [ar_1, ar_2, ar_3, ar_4]
        df['Atap Rumah'] = np.select(conditions4, choices4)


        conditions5 = [
            
            (df['Luas Lantai Rumah(m2)']=='< 8m'),
            (df['Luas Lantai Rumah(m2)']=='> 8m')]
        
        choices5 = [llr_1, llr_2]
        df['Luas Lantai Rumah(m2)'] = np.select(conditions5, choices5)

        conditions6 = [
            
            (df['Sumber Mata Air']=='Sumur Resapan'),
            (df['Sumber Mata Air']=='Sumur Galian'),
            (df['Sumber Mata Air']=='Sumur Pompa'),
            (df['Sumber Mata Air']=='Sumur Bor')]
        
        choices6 = [ma_1, ma_2, ma_3, ma_4]
        df['Sumber Mata Air'] = np.select(conditions6, choices6)


        conditions7 = [
            
            (df['Pengeluaran Kebutuhan Pangan']=='Sebagian Kecil'),
            (df['Pengeluaran Kebutuhan Pangan']=='Sebagian Besar')]
        
        choices7 = [kp_1, kp_2]
        df['Pengeluaran Kebutuhan Pangan'] = np.select(conditions7, choices7)


        conditions8 = [
            
            (df['Pengobatan Tenaga Medis']=='Tidak Mampu'),
            (df['Pengobatan Tenaga Medis']=='Mampu')]
        
        choices8 = [tm_1, tm_2]
        df['Pengobatan Tenaga Medis'] = np.select(conditions8, choices8)


        conditions9 = [
            
            (df['Pembelian Pakaian(/tahun)']=='Tidak Mampu'),
            (df['Pembelian Pakaian(/tahun)']=='Mampu')]
        
        choices9 = [pp_1, pp_2]
        df['Pembelian Pakaian(/tahun)'] = np.select(conditions9, choices9)

        return df
    




    
    elif bobot == 1:
            
        conditions1 = [

            (df['Tingkat Pendidikan']=='Tidak Sekolah'),
            (df['Tingkat Pendidikan']=='SD'),
            (df['Tingkat Pendidikan']=='SMP'),
            (df['Tingkat Pendidikan']=='SMA'),
            (df['Tingkat Pendidikan']=='S1'),
            (df['Tingkat Pendidikan']=='S2'),
            (df['Tingkat Pendidikan']=='S3')]
        
        choices1 = [1, 1.5, 2, 3, 4, 5, 6]
        df['Tingkat Pendidikan'] = np.select(conditions1, choices1)
        

        conditions2 = [
            
            (df['Dinding Rumah']=='Tembok'),
            (df['Dinding Rumah']=='Kayu'),
            (df['Dinding Rumah']=='Bambu')]
        
        choices2 = [3, 2, 1]
        df['Dinding Rumah'] = np.select(conditions2, choices2)


        conditions3 = [
            
            (df['Lantai Rumah']=='Semen'),
            (df['Lantai Rumah']=='Keramik'),
            (df['Lantai Rumah']=='Kayu'),
            (df['Lantai Rumah']=='Tanah')]
        
        choices3 = [4, 3, 2, 1]
        df['Lantai Rumah'] = np.select(conditions3, choices3)


        conditions4 = [
            
            (df['Atap Rumah']=='Rumbia'),
            (df['Atap Rumah']=='Seng'),
            (df['Atap Rumah']=='Asbes'),
            (df['Atap Rumah']=='Genteng')]
        
        choices4 = [1, 2, 3, 4]
        df['Atap Rumah'] = np.select(conditions4, choices4)


        conditions5 = [
            
            (df['Luas Lantai Rumah(m2)']=='< 8m'),
            (df['Luas Lantai Rumah(m2)']=='> 8m')]
        
        choices5 = [1, 2]
        df['Luas Lantai Rumah(m2)'] = np.select(conditions5, choices5)

        conditions6 = [
            
            (df['Sumber Mata Air']=='Sumur Resapan'),
            (df['Sumber Mata Air']=='Sumur Galian'),
            (df['Sumber Mata Air']=='Sumur Pompa'),
            (df['Sumber Mata Air']=='Sumur Bor')]
        
        choices6 = [1, 2, 3, 4]
        df['Sumber Mata Air'] = np.select(conditions6, choices6)


        conditions7 = [
            
            (df['Pengeluaran Kebutuhan Pangan']=='Sebagian Kecil'),
            (df['Pengeluaran Kebutuhan Pangan']=='Sebagian Besar')]
        
        choices7 = [2, 1]
        df['Pengeluaran Kebutuhan Pangan'] = np.select(conditions7, choices7)


        conditions8 = [
            
            (df['Pengobatan Tenaga Medis']=='Tidak Mampu'),
            (df['Pengobatan Tenaga Medis']=='Mampu')]
        
        choices8 = [1, 2]
        df['Pengobatan Tenaga Medis'] = np.select(conditions8, choices8)


        conditions9 = [
            
            (df['Pembelian Pakaian(/tahun)']=='Tidak Mampu'),
            (df['Pembelian Pakaian(/tahun)']=='Mampu')]
        
        choices9 = [1, 2]
        df['Pembelian Pakaian(/tahun)'] = np.select(conditions9, choices9)

        return df