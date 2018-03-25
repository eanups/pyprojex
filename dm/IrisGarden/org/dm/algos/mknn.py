from org.dm.algos.iris_math import dist, get_k_list
from org.dm.app.display import display_accuracy
from org.dm.ingest.reader import te_size, norm_test_garden, tr_size, norm_train_garden, DIM, K, train_class_arr, \
    test_class_arr

K = 5


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


m_kNN()
