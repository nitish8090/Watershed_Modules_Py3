"""
To take a longitudinal section shapefile and convert it to pdfs usign matplot lib
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from scipy.interpolate import interp1d
import scipy

start = time.time()


class PointTable:
    def __init__(self, excel_path):
        self.excel_path = excel_path

        self.df = None

    def read_excel(self):
        self.df = pd.read_excel(self.excel_path, index_col=None, usecols="A, C, F")

    def read_csv(self):
        fields = ['ARCID', 'cum_dist', 'Elevation']
        self.df = pd.read_csv(self.excel_path, usecols=fields)

    def get_max_streams(self):
        return int(self.df.iloc[self.df.shape[0] - 1]['ARCID'])


def main():
    points = PointTable(
        excel_path=r"D:\Nitish\2102_Feb\17_CG_LongitudinalSectionPDF\PointsExcel\CG_Points_Elv_Shrunk.csv")
    points.read_csv()

    for i in range(1, points.get_max_streams() + 1):
        print(i)
        df2 = points.df.loc[points.df['ARCID'] == i]
        print(df2)
        # ploty = df2.plot.line(x='cum_dist', y='Elevation', figsize=(10, 5))
        # plt.show()

        # f1 = interp1d(df2.index, df2['cum_dist'], kind='cubic')
        # f2 = interp1d(df2.index, df2['Elevation'], kind='cubic')

        a_BSpline = scipy.interpolate.interp1d(x=df2['cum_dist'], y=df2['Elevation'], kind='slinear')

        df3 = pd.DataFrame()
        new_index = np.linspace(df2['cum_dist'].min(), df2['cum_dist'].max(), num=200)
        # new_index = np.arange(df2['cum_dist'].min(), df2['cum_dist'].max(), step=0.5)
        df3['cum_dist'] = new_index
        df3['Elevation'] = a_BSpline(new_index)
        df3.index = new_index

        print(df3)

        ax2 = df3.plot.line(x='cum_dist', y='Elevation', figsize=(10, 5))

        # plt.plot(df2['cum_dist'], df2['Elevation'], '--', df3['cum_dist'], df3['Elevation'], '-')
        plt.plot(df3['cum_dist'], df3['Elevation'], '-')
        plt.show()

        # print(f1(df2.index))
        # print(df2)
        # ploty = df3.plot.line(x='cum_dist', y='Elevation', figsize=(10, 5))
        # ploty.figure(figsize=(20,10))
        # plt.show()
        # break


main()
end = time.time()
print("This took : {}".format(end - start))
