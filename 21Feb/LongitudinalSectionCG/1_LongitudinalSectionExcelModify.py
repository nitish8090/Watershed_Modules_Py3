import xlsxwriter
import pandas as pd
import os


class PointTable:
    def __init__(self, excel_path):
        self.excel_path = excel_path

        self.df = None
        self.column_heads = ['ARCID', 'cum_dist', 'Elevation']

    def read_excel(self):
        self.df = pd.read_excel(self.excel_path, index_col=None, usecols="A, C, F")

    def read_csv(self):
        self.df = pd.read_csv(self.excel_path, usecols=self.column_heads)

    def get_max_streams(self):
        return int(self.df.iloc[self.df.shape[0] - 1]['ARCID'])



class OutputExcel:
    def __init__(self, path):
        self.path = path
        self.workbook = None
        self.worksheet = None

    def create_sheet(self):
        self.workbook = xlsxwriter.Workbook(self.path)
        self.worksheet = self.workbook.add_worksheet('Sheet1')

    def write_heading(self, heading):
        for i, column in enumerate(heading):
            self.worksheet.write(0, i, column)

    def write_data(self, dataframe):
        row_num = 0  # Because iterrows returns index
        for index, row in dataframe.iterrows():
            a_row = list(row)
            print(a_row)
            for col_num, cell_value in enumerate(a_row):
                print("RowNo: {}, ColNo:{}, Value:{}".format(row_num + 1, col_num, cell_value))
                self.worksheet.write(row_num + 1, col_num, cell_value)  # +1 for Headings
            row_num += 1

    def add_chart(self, col_length):
        # Create a new chart object.
        chart = self.workbook.add_chart({'type': 'line'})

        # Add a series to the chart.
        chart.add_series({'categories': '=Sheet1!$B$2:$B${}'.format(col_length + 1),
                          'values': '=Sheet1!$C$2:$C${}'.format(col_length + 1),
                          'smooth': 'TRUE'})

        # Insert the chart into the worksheet.
        self.worksheet.insert_chart('C1', chart)

    def save(self):
        self.workbook.close()


def main():
    points = PointTable(
        excel_path=r"D:\Nitish\26_States\2_MP\MP_LongitudinalSection\CSV\MP_LongSec_Point_WithElevation.csv")
    output_folder = r"D:\Nitish\26_States\2_MP\MP_LongitudinalSection\IndividualExcels"

    points.read_csv()

    for i in range(1, points.get_max_streams() + 1):
        print("Working for stream: {}".format(i))
        df2 = points.df.loc[points.df['ARCID'] == i].copy()
        print(df2)
        col_length = len(df2.index)

        output_path = os.path.join(output_folder, "MP_StreamID_{}_LongitudinalSec.xlsx".format(i))
        print("\tSaving at: {}".format(output_path))

        output_excel = OutputExcel(path=output_path)
        output_excel.create_sheet()
        output_excel.write_heading(points.column_heads)
        output_excel.write_data(dataframe=df2)
        output_excel.add_chart(col_length=col_length)
        output_excel.save()


main()
