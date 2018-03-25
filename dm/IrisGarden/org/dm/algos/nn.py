from org.dm.app.display import display_accuracy
from org.dm.algos.iris_math import dist
from org.dm.ingest.reader import te_size, norm_test_garden, tr_size, norm_train_garden, DIM, train_class_arr, \
    test_class_arr


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


nearest_neighbor()
