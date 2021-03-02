"""
To take a longitudinal section shapefile and convert it to pdfs usign matplot lib
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class PointTable:
    def __init__(self, excel_path):
        self.excel_path = excel_path

        self.df = None

    def read_excel(self):
        self.df = pd.read_excel(self.excel_path, index_col=None, usecols="B, L")

    def get_max_streams(self):
        return int(self.df.iloc[self.df.shape[0]-1]['ARCID'])


def main():
    points = PointTable(excel_path=r"Excel/CG_Points.xlsx")
    points.read_excel()

    for i in range(1, points.get_max_streams()+1):
        print(i)
        df2 = points.df.loc[points.df['ARCID'] == 1]


main()
