import numpy as np
from sklearn.cluster import KMeans


def kmeans_1(df_scaled,n_klaster):

    kmeans = KMeans(n_clusters=n_klaster)
    y_predicted = kmeans.fit_predict(df_scaled)
   
    return y_predicted