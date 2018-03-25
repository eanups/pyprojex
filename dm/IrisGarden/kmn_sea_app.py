import csv
import numpy as np
from collections import Counter
import sys


DIM = 4
K = 5
DELTA = .00001
setosa, versicolor, virginica = range(0, 3)


def read_data(csv_file):
    """
    Reads data from a CSV file into a 2D Array List / Matrix
    :param csv_file:
    :return:
    """
    recs = []

    with open(csv_file, 'rb') as csv_handle:
        reader = csv.reader(csv_handle, delimiter=',')
        for row in reader:
            recs.append(row)

    return np.array(recs)


def dist(p_vector, q_vector, dimension):
    """
    Finds the Euclidean distance
    :param p_vector: data point 1
    :param q_vector: data point 2
    :param dimension: number of dimensions
    :return:
    """
    tmp = 0
    for k in range(dimension):
        tmp += (p_vector[k] - q_vector[k]) ** 2
    return abs(tmp) ** 0.5


def get_norm_arr(arr):
    """
    Returns a normalized array
    :param arr:
    :return:
    """
    f_arr = np.asfarray(arr)
    max_f_arr = max(f_arr)
    return f_arr / max_f_arr


def get_norm2_arr(arr):
    """
    Returns a normalized array
    :param arr:
    :return:
    """
    f_arr = np.asfarray(arr)
    max_f_arr = max(f_arr)
    min_f_arr = min(f_arr)
    return (f_arr - min_f_arr) / (max_f_arr - min_f_arr)


def get_norm_garden(tr_garden):
    """
    Returns a normalized garden
    :param tr_garden:
    :return:
    """
    sepal_len_arr = get_norm2_arr(tr_garden[0])
    sepal_wid_arr = get_norm2_arr(tr_garden[1])
    petal_len_arr = get_norm2_arr(tr_garden[2])
    petal_wid_arr = get_norm2_arr(tr_garden[3])

    garden_list = [sepal_len_arr, sepal_wid_arr, petal_len_arr, petal_wid_arr]
    return np.array(garden_list).transpose()


def get_k_list(dists, k):
    """
    Return the first k nearest neighbor list
    :param dists: distances list
    :param k: number of neighbors
    :return:
    """
    sorted_dists = sorted(dists.items(), key=lambda x: x[1])
    return sorted_dists[:k]


train_garden = read_data("data/train.csv")
test_garden = read_data("data/test.csv")

print "-" * 100

# Read training and test data.
tr_train_garden = np.transpose(train_garden)
tr_test_garden = np.transpose(test_garden)

train_class_arr = tr_train_garden[4]
test_class_arr = tr_test_garden[4]

norm_train_garden = get_norm_garden(tr_train_garden)
norm_test_garden = get_norm_garden(tr_test_garden)

# For K-means use aggregated train and test data.
norm_garden = np.concatenate((norm_train_garden, norm_test_garden), axis=0)

class_arr = np.concatenate((train_class_arr, test_class_arr), axis=0)

# Initial Seeds
p = 0
q = 1
r = 2
init_seeds = np.array([norm_garden[p], norm_garden[q], norm_garden[r]])
print init_seeds

o = 0
for i in norm_garden:
    if o == p or o == q or o == r:
        print "{} : {} : {}".format(o, i, class_arr[o])
    o += 1


print "-" * 100

# Test
# print dist([0, 2, 0], [0, 4, 1], 3)


# Steps
'''
For each of the test data point
  Compare with every training data point
    To check the minimum distance to it.
    Assign the minimum distance point class to a computed class point.
    Compare computed class with actual test class and count the number of correct points.
    
Divide the correct points against the actual test points to know the accuracy
'''

tr_size = train_garden.shape[0]
te_size = test_garden.shape[0]


def kNN():
    corr_class = 0

    for i in range(te_size):
        k_dists = {}
        p = norm_test_garden[i]
        for j in range(tr_size):
            q = norm_train_garden[j]
            comp_dist = dist(p, q, DIM)
            k_dists[j] = comp_dist

        print "For Test Point {}".format(i)
        # Get first 5 smallest distances
        k_list = get_k_list(k_dists, K)
        c_list = []
        for (key, value) in k_list:
            t_class = train_class_arr[key]
            print "\tTraining Point {} is at a distance of {} having the class {}".format(key, value,
                                                                                          train_class_arr[key])
            c_list.append(t_class)
        c = Counter(c_list)
        c_class = c.most_common()[0][0]

        if c_class == test_class_arr[i].strip():
            corr_class += 1
        else:
            print "Unmatched test data index: {}".format(i)

    display_accuracy(corr_class, K)


def display_accuracy(corr_class, k=0):
    print "=" * 100
    print corr_class
    print 'Accuracy of K[{}] - Nearest Neighbor Algo:  {}'.format(k, float(corr_class) / te_size * 100)
    print "=" * 100


def get_weight(d1, dk, dj):
    weight = 1
    if dk != d1:
        weight = (dk - dj)/(dk - d1)
    return weight


def m_kNN():
    corr_class = 0

    for i in range(te_size):
        k_dists = {}
        p = norm_test_garden[i]
        for j in range(tr_size):
            q = norm_train_garden[j]
            comp_dist = dist(p, q, DIM)
            k_dists[j] = comp_dist

        print "For Test Point {}".format(i)
        # Get first 5 smallest distances
        k_list = get_k_list(k_dists, K)

        # Determine the weights.
        weights = {}
        for (key, value) in k_list:
            cl = train_class_arr[key]
            if weights.get(cl) is not None:
                weights[cl] += value
            else:
                weights.update({cl: value})
        print weights
        c_class = max(weights, key=weights.get)

        if c_class == test_class_arr[i].strip():
            corr_class += 1
        else:
            print "Unmatched test data index: {}".format(i)

    display_accuracy(corr_class, K)


def nearest_neighbor():
    corr_class = 0
    for i in range(te_size):
        min_dist = 1000
        p = norm_test_garden[i]
        min_j = 0
        for j in range(tr_size):
            q = norm_train_garden[j]
            comp_dist = dist(p, q, DIM)

            if comp_dist < min_dist:
                min_dist = comp_dist
                min_j = j

        if train_class_arr[min_j].strip() == test_class_arr[i].strip():
            corr_class += 1
        else:
            print "Unmatched test data index: {}".format(i)

    display_accuracy(corr_class)


def get_centroid(points):
    total = np.array([0.0, 0.0, 0.0, 0.0])
    for p in points:
        total += p

    return total / len(points)


def cluster_sse(centroid, points, dim):
    total = 0
    for point in points:
        total += dist(centroid, point, dim) ** 2
    return total


def overall_sse(clusters, dim):
    total = 0
    for cluster in clusters:
        centroid = get_centroid(cluster)
        total += cluster_sse(centroid, cluster, dim)
    return total


def significant_change_in_centroid(xc, cc, k, dim):
    sum_of_dist = 0.0
    for f in range(k):
        sum_of_dist = dist(xc[f], cc[f], dim)

    if sum_of_dist > DELTA:
        return True
    else:
        return False


def equal_centroids(xc, cc, k, dim):
    for cen in range(k):
        for f in range(dim):
            if xc[cen][f] != cc[cen][f]:
                return False

    return True


def least_dist_centroid(centroids, point):
    dists = []
    for c in centroids:
        dists.append(dist(c, point, 4))
    return dists.index(min(dists))


def k_means(seeds):
    """
    Calculate the k-means given the initial seed.
    :param seeds: intial seed values for k-centroids
    :return:
    """
    print setosa
    k_centroids = seeds

    print "Kay Centroids\n", k_centroids

    c0 = []  # setosa
    c1 = []  # versicolor
    c2 = []  # virginica

    count = 1
    while True:
        c0[:] = []
        c1[:] = []
        c2[:] = []
        for item in norm_garden:

            c = least_dist_centroid(k_centroids, item)
            if c == setosa:
                c0.append(item)
            elif c == versicolor:
                c1.append(item)
            elif c == virginica:
                c2.append(item)
            else:
                print "Error. Invalid item"

        c_centroids = np.zeros((3, 4))
        c_centroids[0] = np.array(get_centroid(c0))
        c_centroids[1] = np.array(get_centroid(c1))
        c_centroids[2] = np.array(get_centroid(c2))

        csse = overall_sse([c0, c1, c2], 4)
        print "Iteration: {} , SSE: {}".format(count, csse)

        if equal_centroids(c_centroids, k_centroids, 3, 4):
        # if not significant_change_in_centroid(k_centroids, c_centroids, 3, 4):
            break
        k_centroids = c_centroids.copy()

        print "-" * 80
        count += 1

    sse = overall_sse([c0, c1, c2], 4)

    print "*" * 100
    print "Iterations: {}".format(count)
    print "{} : {} : {}".format(len(c0), len(c1), len(c2))
    print "SSE: {} \n\tfor selected initial seeds: {}".format(sse, [p, q, r])
    print "*" * 100


# Algorithms :

kNN()
# m_kNN()
# nearest_neighbor()

# k_means(init_seeds)
