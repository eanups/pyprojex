# Wrapper

import time


def time_func(some_func):
    """
    Wraps a function by timing the execution
    :param some_func: function to be timed
    :return: wrapped function
    """
    def wrap_func(*args):
        t_start = time.time()
        some_func(args[0], args[1])
        t_end = time.time()
        print("Time taken: " + str(t_end - t_start))
    return wrap_func


def sum_of_n(num, power):
    """
    Calculate sum of numbers
    :param num:
    :param power:
    :return:
    """
    total = 0
    for i in range(num):
        total = total + i ** power
    print("Sum of first " + str(num) + " numbers:" + str(total))

timed_sum_of_n = time_func(sum_of_n)
timed_sum_of_n(10, 2)

print("-" * 50)


# Decorator

@time_func
def prod_of_n(num, power):
    total = 1
    for i in range(1, num+1):
        total = total * i ** power
    print("Prod of first " + str(num) + " numbers:" + str(total))

prod_of_n(3, 2)

print("-" * 50)
