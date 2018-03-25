import csv

import numpy as np

from org.dm.algos.iris_math import get_norm2_arr

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


DIM = 4
K = 5


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
    i_class_arr = tr_garden[4]

    garden_list = [sepal_len_arr, sepal_wid_arr, petal_len_arr, petal_wid_arr, i_class_arr]
    return np.array(garden_list).transpose()


train_garden = read_data("data/train.csv")
test_garden = read_data("data/test.csv")

tr_train_garden = np.transpose(train_garden)
tr_test_garden = np.transpose(test_garden)

train_class_arr = tr_train_garden[4]
test_class_arr = tr_test_garden[4]

norm_train_garden = get_norm_garden(tr_train_garden)
norm_test_garden = get_norm_garden(tr_test_garden)

norm_garden = np.concatenate((norm_train_garden, norm_test_garden), axis=0)
class_arr = np.concatenate((train_class_arr, test_class_arr), axis=0)

tr_size = train_garden.shape[0]
te_size = test_garden.shape[0]
