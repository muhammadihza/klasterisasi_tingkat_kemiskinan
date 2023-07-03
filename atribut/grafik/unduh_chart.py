import streamlit as st
from streamlit import components
import pandas as pd  # pip install pandas
import numpy as np
import plotly.express as px  # pip install plotly-express
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module

def download_bar_chart(courses, values, label, n):

    if n == 1:
        fig = plt.figure(figsize = (15, 10))
            
        # Creating the bar plot
        plt.bar(courses, values, color ='maroon',
            width = 0.4)
            
        plt.title(label)

        fn = 'scatter.png'
        plt.savefig(fn)
        with open(fn, "rb") as img:
            btn = st.download_button(
                label="Download Bar Chart",
                data=img,
                file_name=fn,
                mime="image/png"
            )