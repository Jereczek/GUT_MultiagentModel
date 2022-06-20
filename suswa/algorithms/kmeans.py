from sklearn.cluster import KMeans

class TwoMeans():

    def __init__(self, init: str = 'random', n_init: int = 10, max_iter: int = 100, n_clusters: int = 2):
        self.kmeans = KMeans(init=init, n_clusters=n_clusters, n_init=n_init, max_iter=max_iter)

    def fit(self, array):
        return self.kmeans.fit(array)

