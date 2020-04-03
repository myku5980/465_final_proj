#importing required libaries 
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#load iris dataset
iris = datasets.load_iris()
data = iris.data
print(data[:30])

n = 10


def SSQ(data, clusters):
    total = 0
    for x in data:
        temp = []
        for c in clusters:
            dist = 0
            for ind in range(len(x)):
                dist += abs(x[ind] - c[ind]) ** 2
            temp.append(dist)
        total += min(temp)
    return total


SSQList = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for k in range(1, n + 1):
    kmeans = KMeans(n_clusters = k).fit(data)
    clusters = kmeans.cluster_centers_
    SSQList.append(SSQ(data, clusters))

plt.plot(numbers, SSQList)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('SSQ')
plt.show()
