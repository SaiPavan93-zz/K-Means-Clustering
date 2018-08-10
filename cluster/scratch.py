import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from sklearn.preprocessing import  scale

def main():
    data=pd.read_csv("Iris.csv")
    X1=data["SepalLengthCm"].values
    Y1=data["SepalWidthCm"].values
    X = np.array(list(zip(X1, Y1)))
    number=range(1,10)
    d=determineK(number,X)
    plt.plot(number,d,'rx-')
    plt.xlabel('number')
    plt.ylabel('d')
    plt.show()
    model=KMeans(n_clusters=3)
    model=model.fit(scale(X))
    plt.figure('K means')

    plt.scatter(X[:,0],X[:,1],c=model.labels_)
    print(model.labels_)
    plt.xlabel('Sepallt')
    plt.ylabel('Sepalwt')
    plt.show()


def determineK(number,X):
    d=[]
    for i in number:
        kmeans=KMeans(i).fit(X)
        kmeans.fit(X)
        d.append(sum(np.min(cdist(X,kmeans.cluster_centers_,'euclidean'),axis=1))/X.shape[0])
    return d

if __name__=="__main__" :
    main()