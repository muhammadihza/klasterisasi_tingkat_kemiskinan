import numpy as np


def kmeans_2(X, centroids, max_iterations=30):
    num_clusters = centroids.shape[0]
    num_samples = X.shape[0]
    labels = np.zeros(num_samples, dtype=int)
    X = np.array(X)
    for _ in range(max_iterations):
        # Assign each data point to the nearest centroid
        for i in range(num_samples):
            distances = np.linalg.norm(X[i] - centroids, axis=1)
            labels[i] = np.argmin(distances)

        # Update the centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(num_clusters)])

        # Check for convergence
        if np.all(centroids == new_centroids):
            break

        centroids = new_centroids

    return labels, centroids