import csv
import numpy as np

DIM = 4


def read_data(csv_file):
    recs = []

    with open(csv_file, 'rb') as csv_handle:
        reader = csv.reader(csv_handle, delimiter=',')
        for row in reader:
            recs.append(row)

    return np.array(recs)


def dist(p_vector, q_vector, dimension):
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

# print norm_train_garden

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

print "=" * 100

print corr_class
print 'Accuracy of Nearest Neighbor Algo:  {}'.format(float(corr_class)/te_size * 100)

print "=" * 100
