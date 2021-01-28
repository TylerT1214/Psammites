from sklearn.cluster import kmeans_plusplus
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from subprocess import Popen

n_samples = 4000
n_components = 4

X, y_true = make_blobs(n_samples=n_samples,
                       centers=n_components,
                       cluster_std=0.60,
                       random_state=0)
                       
X = X[:, ::-1]

centers_init, indices = kmeans_plusplus(X, n_clusters=4, random_state=0)


def my_plot():
    try:
        x = Popen(['rm', '/var/tmp/plot.png'])
    except:
        pass
        
    plt.figure(1)
    colors = ['#4EACC5', '#FF9C34', '#4E9A06', 'm']

    for k, col in enumerate(colors):
        cluster_data = y_true == k
        plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker='.', s=10)
        
    plt.scatter(centers_init[:,0], centers_init[:,1], c="b", s=50)
    plt.title("K-Means++ Initialization")
    plt.xticks([])
    plt.yticks([])
    fig = plt.gcf()
    fig.savefig("/var/tmp/plot.png")
    
    
if __name__ == "__main__":
    print(type(my_plot()))
    try:
        my_plot().show()
    except:
        pass
