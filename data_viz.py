import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')


def boxplot(data_lists, label_list, title, x_label, y_label, out_file_name):
    """
    This function creates multiple box plot displaying the data /
    contained lists. It also saves the figure to a file.

    Parameters:
    - data_list(list): A list of list of numbers
    - label_list(list): A list of labels for the x-axis
    - title(str):
    - x_label(str):
    - y_label(str):
    - out_file_name(str): The name of the file we want to create

    Returns:
    - None, however, a file is saved.

    """
    fig = plt.figure(figsize = (15,5))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_lists)
    ax.set_xticklabels(label_list, rotation = "vertical")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(out_file_name, bbox_inches='tight')
