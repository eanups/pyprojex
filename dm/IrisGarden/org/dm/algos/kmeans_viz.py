import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib

from org.dm.ingest.reader import read_data, get_norm_garden
from org.dm.algos.iris_math import least_dist_centroid, get_centroid, equal_centroids, overall_sse

DIM = 4
setosa, versicolor, virginica = range(0, 3)

iris_garden = read_data("data/iris.data")
iris_norm_garden = get_norm_garden(np.transpose(iris_garden))

# Initial Seeds
p = 10
q = 25
r = 125
init_seeds = np.array([iris_norm_garden[p], iris_norm_garden[q], iris_norm_garden[r]])

o = 0
for i in iris_norm_garden:
    if o == p or o == q or o == r:
        print "{} : {}".format(o, i)
    o += 1


print "-" * 100


def k_means(seeds):
    """
    Calculate the k-means given the initial seed.
    :param seeds: intial seed values for k-centroids
    :return:
    """
    print setosa
    k_centroids = seeds
    temp_garden = iris_norm_garden.copy()

    c0 = []  # setosa
    c1 = []  # versicolor
    c2 = []  # virginica

    count = 1
    while True:
        c0[:] = []
        c1[:] = []
        c2[:] = []
        garden_len = len(temp_garden)
        for it in range(garden_len):

            c = least_dist_centroid(k_centroids, temp_garden[it])
            temp_garden[it, 4] = c
            # print temp_garden[it]

            if c == setosa:
                c0.append(temp_garden[it])
            elif c == versicolor:
                c1.append(temp_garden[it])
            elif c == virginica:
                c2.append(temp_garden[it])
            else:
                print "Error. Invalid item"

        c_centroids = np.zeros((3, DIM))
        c_centroids[0] = np.array(get_centroid(c0, DIM))
        c_centroids[1] = np.array(get_centroid(c1, DIM))
        c_centroids[2] = np.array(get_centroid(c2, DIM))

        csse = overall_sse([c0, c1, c2], DIM)
        print "Iteration: {} , SSE: {}".format(count, csse)

        if equal_centroids(c_centroids, k_centroids, 3, DIM):
        # if not significant_change_in_centroid(k_centroids, c_centroids, 3, 4):
            break
        k_centroids = c_centroids.copy()

        print "-" * 80
        count += 1

    sse = overall_sse([c0, c1, c2], DIM)

    # Data plotting
    colors = ['green', 'blue', 'purple', 'pink', 'orange', 'black', 'red', 'gray', 'brown', 'yellow']
    plt.scatter(temp_garden[:, 0], temp_garden[:, 2], c=temp_garden[:, 4], marker='*',
                cmap=matplotlib.colors.ListedColormap(colors[:3]))
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Width')
    plt.title('Iris Data: K Means Classification')
    plt.show()
    # plt.pause(0.5)

    print "*" * 100
    print "Iterations: {}".format(count)
    print "{} : {} : {}".format(len(c0), len(c1), len(c2))
    print "SSE: {} \n\tfor selected initial seeds: {}".format(sse, [p, q, r])
    print "*" * 100


k_means(init_seeds)
