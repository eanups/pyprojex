from collections import Counter

from org.dm.algos.iris_math import dist, get_k_list
from org.dm.app.display import display_accuracy
from org.dm.ingest.reader import te_size, norm_test_garden, tr_size, norm_train_garden, DIM, train_class_arr, \
    test_class_arr

K = 2


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


kNN()
