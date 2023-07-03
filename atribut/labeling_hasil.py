import streamlit as st
import numpy as np

def labeling_result(n, df):
    
    labels = []

    for i in range(n):
        label = st.text_input(f"Masukkan label untuk klaster {i+1}:")
        labels.append(label)

    conditions = [(df['Cluster'] == i) for i in range(n)]
    choices = labels[:n]
    
    df['Cluster'] = np.select(conditions, choices)

    return df