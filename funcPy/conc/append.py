
def append7_pure(lyst):
    """
    Pure function
    """
    return lyst + [7]


def append7_np(lyst):
    """
    Function with side-effects
    """
    lyst.append(7)


l = [1]
print l
append7_pure(l)
print l
append7_np(l)
print l


'''
Side effects are sometimes necessary (Interactions, Displays, Network communication ..)
Not always.
'''