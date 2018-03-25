from org.dm.ingest.reader import te_size


def display_accuracy(corr_class, k=0):
    print "=" * 100
    print corr_class
    print 'Accuracy of K[{}] - Nearest Neighbor Algo:  {}'.format(k, float(corr_class) / te_size * 100)
    print "=" * 100