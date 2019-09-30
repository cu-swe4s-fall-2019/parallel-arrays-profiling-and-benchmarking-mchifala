import sys
import math
import numpy as np


def list_mean(data_list):
    """
    This function calculates the mean of a list of numbers. It is \
    capable of handling errors when the list is empty or contains \
    the wrong data types.

    Parameters:
    - data_list(list): A list of numbers

    Returns:
    - mean(float): The mean of the list

    """
    try:
        return sum(data_list)/len(data_list)

    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)

    except TypeError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)


def list_stdev(data_list):
    """
    This function calculates the standard of a list of numbers. It is \
    capable of handling errors when the list is empty or contains \
    the wrong data types.

    Parameters:
    - data_list(list): A list of numbers

    Returns:
    - mean(float): The mean of the list

    """
    try:
        return math.sqrt(sum([(np.mean(data_list)-x)**2 for x in data_list]) / len(data_list))

    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)

    except TypeError as inst:
        print("Run-Time Error:", type(inst))
        sys.exit(1)