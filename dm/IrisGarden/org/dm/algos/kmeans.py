import numpy as np
import matplotlib.pyplot as plt
import matplotlib

import sys

from org.dm.ingest.reader import norm_garden, class_arr
from org.dm.algos.iris_math import least_dist_centroid, get_centroid, equal_centroids, overall_sse


# setosa, versicolor, virginica = range(0, 3)

seed_list = [0, 75, 140]

o = 0
for i in norm_garden:
    if o in seed_list:
        print "{} : {} : {}".format(o, i, class_arr[o])
    o += 1


print "-" * 100


def k_means(seeds):
    """
    Calculate the k-means given the initial seed.
    :param seeds: intial seed values for k-centroids
    :return:
    """
    k_centroids = np.array([norm_garden[item] for item in seeds])
    temp_garden = norm_garden.copy()

    print "Kay Centroids\n", k_centroids

    kay = len(seeds)

    cl_list = []
    for k in range(kay):
        cl_list.append([])

    print cl_list

    count = 1
    while True:
        for m in range(kay):
            cl_list[m][:] = []

        # for item in norm_garden:
        #
        #     c = least_dist_centroid(k_centroids, item)
        #     cl_list[c].append(np.array(item))

        garden_len = len(temp_garden)
        for it in range(garden_len):
            item = temp_garden[it]
            c = least_dist_centroid(k_centroids, item)
            temp_garden[it, 4] = c
            cl_list[c].append(np.array(item))

        cl_len = len(cl_list)

        c_centroids = np.array([get_centroid(cl_list[e], dim=4) for e in range(cl_len)])

        csse = overall_sse(cl_list, 4)
        print "Iteration: {} , SSE: {}".format(count, csse)

        print k_centroids
        print c_centroids

        if equal_centroids(c_centroids, k_centroids, 3, 4) or count == 25:
        # if not significant_change_in_centroid(k_centroids, c_centroids, 3, 4):
            break
        k_centroids = c_centroids

        print "-" * 80
        count += 1

    sse = overall_sse(cl_list, 4)

    print "*" * 100
    print "Iterations: {}".format(count)
    for n in range(kay):
        print "Cluster {} : {} items".format(n, len(cl_list[n]))
    print "SSE: {} \n\tfor selected initial seeds: {}".format(sse, seeds)
    print "*" * 100

    # Data plotting
    colors = ['green', 'blue', 'purple', 'pink', 'orange', 'black', 'red', 'gray', 'brown', 'yellow']
    plt.scatter(temp_garden[:, 0], temp_garden[:, 2], c=temp_garden[:, 4], marker='^',
                cmap=matplotlib.colors.ListedColormap(colors[:kay]))
    plt.xlabel('Sepal Length')
    plt.ylabel('Petal Width')
    plt.title('Iris Data: K Means Classification')
    plt.show()


# k_means(init_seeds)
k_means(seed_list)
