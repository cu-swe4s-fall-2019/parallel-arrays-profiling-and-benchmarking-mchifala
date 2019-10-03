import matplotlib.pyplot as plt
import numpy as np
import os
import unittest
from data_viz import boxplot
import matplotlib
matplotlib.use('Agg')


class TestPlots(unittest.TestCase):
    """
    This class is used to test the boxplot methods from the data_viz module.

    """
    def test_boxplot_exist(self):
        self.data_lists = []
        for i in range(4):
            self.data_lists.append(np.random.randint(0, 100, size=100))
        self.file = "boxplot_test"
        self.label_list = ['Sample1', 'Sample2', 'Sample3', 'Sample4']
        self.title = "ACTA2"
        self.x_label = "SMTS"
        self.y_label = "Gene read counts"
        boxplot(self.data_lists, self.label_list, self.title, self.x_label,
                self.y_label, self.file)
        self.assertEqual(True, os.path.exists(self.file+".png"))

    def test_boxplot_empty(self):
        self.data_lists = []
        self.file = "boxplot_empty"
        self.label_list = []
        self.title = "ACTA2"
        self.x_label = "SMTS"
        self.y_label = "Gene read counts"
        boxplot(self.data_lists, self.label_list, self.title, self.x_label,
                self.y_label, self.file)
        self.assertEqual(True, os.path.exists(self.file+".png"))

    def test_boxplot_not_exist(self):
        self.data_lists = []
        for i in range(4):
            self.data_lists.append(np.random.randint(0, 100, size=100))
        self.file = "boxplot_test2"
        self.label_list = ['Sample1', 'Sample2', 'Sample3', 'Sample4']
        self.title = "ACTA2"
        self.x_label = "SMTS"
        self.y_label = "Gene read counts"
        boxplot(self.data_lists, self.label_list, self.title, self.x_label,
                self.y_label, "bad_histogram")
        self.assertEqual(False, os.path.exists(self.file+".png"))


if __name__ == '__main__':
    unittest.main()
