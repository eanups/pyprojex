import numpy as np

DELTA = .00001


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
        tmp += (float(p_vector[k]) - float(q_vector[k])) ** 2
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


def get_centroid(points, dim):
    total = [0.0, 0.0, 0.0, 0.0]
    for p in points:
        fp = np.array(p[:dim], dtype=float)
        total += fp

    return total / len(points)


def cluster_sse(centroid, points, dim):
    total = 0
    for point in points:
        total += dist(centroid, point, dim) ** 2
    return total


def overall_sse(clusters, dim):
    total = 0
    for cluster in clusters:
        centroid = get_centroid(cluster, dim)
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


def get_k_list(dists, k):
    """
    Return the first k nearest neighbor list
    :param dists: distances list
    :param k: number of neighbors
    :return:
    """
    sorted_dists = sorted(dists.items(), key=lambda x: x[1])
    return sorted_dists[:k]