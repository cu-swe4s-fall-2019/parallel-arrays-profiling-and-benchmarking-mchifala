from math_lib import list_mean
from math_lib import list_stdev
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


def boxplot(data_list, out_file_name):
    """
    This function creates a box plot displaying the data contained in the \
    list of values and displays the mean and standard deviation of the \
    data as the figure's title. It also saves the figure to a file.

    Parameters:
    - data_list(list): A list of numbers
    - out_file_name(str): The name of the file we want to create

    Returns:
    - None, however, a file is saved.

    """
    mean = list_mean(data_list)
    std = list_stdev(data_list)
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    plt.boxplot(data_list)
    plt.title("Mean: " + str(mean) + " Standard Deviation: " + str(std))
    plt.xlabel("Array #1")
    plt.ylabel("Value")
    plt.savefig(out_file_name, bbox_inches='tight')


def histogram(L, out_file_name):
    """
    This function creates a histogram displaying the data contained in the \
    list of values and displays the mean and standard deviation of the \
    data as the figure's title. It also saves the figure to a file.

    Parameters:
    - data_list(list): A list of numbers
    - out_file_name(str): The name of the file we want to create

    Returns:
    - None, however, a file is saved.

    """
    mean = list_mean(data_list)
    std = list_stdev(data_list)
    width = 3
    height = 3
    fig = plt.figure(figsize=(width, height), dpi=300)
    plt.hist(data_list)
    plt.title("Mean: " + str(mean) + " Standard Deviation: " + str(std))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.savefig(out_file_name, bbox_inches='tight')


def combo(L, out_file_name):
    """
    This function creates both a histogram and box plot displaying the data \
    contained in the list of values and displays the mean and standard \
    deviation of the data as the figure's title. It also saves \
    the figure to a file.

    Parameters:
    - data_list(list): A list of numbers
    - out_file_name(str): The name of the file we want to create

    Returns:
    - None, however, a file is saved.

    """
    width = 3
    height = 3
    mean = list_mean(data_list)
    std = list_stdev(data_list)
    fig, axes = plt.subplots(2, 1)
    axes[0].hist(data_list)
    axes[0].set_xlabel("Value")
    axes[0].set_ylabel("Frequency")
    axes[0].set_title("Mean: " + str(mean) + "Standard Deviation: " + str(std),
                      loc="right")
    axes[1].boxplot(L)
    axes[1].set_xlabel("Array #1")
    axes[1].set_ylabel("Value")
    axes[1].set_title("Mean: " + str(mean) + "Standard Deviation: " + str(std),
                      loc="right")
    plt.tight_layout()
    plt.savefig(out_file_name)