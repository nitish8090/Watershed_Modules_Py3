import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import os


class CIMPList:
    def __init__(self, path):
        self.path = path
        self.list = []

        self.set_cimps()

    def set_cimps(self):
        for name in os.listdir(self.path):
            self.list.append(CIMP(self.path, name))


class CIMP:
    def __init__(self, folder, name):
        self.name = name
        self.path = os.path.join(folder, name)
        self.sheet_list = []

    def read_sheet_list(self):
        xls = openpyxl.open(self.path)
        self.sheet_list = xls.sheetnames


class ResRel:
    def __init__(self, excel_path, sheet_name):
        self.path = excel_path
        self.sheet = sheet_name
        self.df = None

    def read_dataframe(self):
        self.df = pd.read_excel(self.path, self.sheet)
        self.df = self.df.iloc[9:14, 9:15]
        self.df = self.df.reset_index(drop=True)
        self.df.set_index(self.df.columns[0], inplace=True)
        self.df.columns = ["(1981-2019)",
                           "(2020-2040)",
                           "(2041-2060)",
                           "(2061-2080)",
                           "(2081-2100)"]
        print(self.df)
        # labels = self.df['Reliability.1'][9:14]
        # axes = self.df.S1[9:14]

    def check(self):
        """Was used to check the consistency of the dataframes"""
        ref_list = ['Healthy', 'Satisfactory', 'Innocuous', 'Unsatisfactory', 'Unhealthy']
        check_list = list(self.df.iloc[:, 0])
        # print("Checking: {}".format(self.sheet))
        if check_list.sort() == ref_list.sort():
            pass
            # print("Passed test {}".format(check_list))
        else:
            print("This Failed the test: \n{}\\{}".format(self.path, self.sheet))


# class PieChart:
#     def __init__(self, df):
#         self.df = df
#
#     def create(self):
#         plot = self.df.df.plot.pie(xlabel=self.df.df.iloc[:, 0], y='B1', figsize=(5, 5), title='B1', legend=False)
#         plt.axis('off')
#         # plt.pie(self.axes, labels=self.labels, autopct='%1.1f%%')
#         # plt.xticks(rotation=45)
#
#         # plt.legend(axes, labels, bbox_to_anchor=(-0.1, 1.))
#
#     def show(self):
#         plt.show()


def main():
    cimp_list = CIMPList(r"D:\Nitish\2103_Mar\3_PiCharts\Round2\piExcel")
    pi_folder_path = r"D:\Nitish\2103_Mar\3_PiCharts\Round2\piCharts"

    for cimp in cimp_list.list:
        print("Inside: {}".format(cimp.name))
        cimp_out_folder = os.path.join(pi_folder_path, os.path.splitext(cimp.name)[0])
        print("Creating folder: {}".format(cimp_out_folder))
        if run_for_real:
            os.mkdir(cimp_out_folder)  # Create cimp folder

        cimp.read_sheet_list()
        for sheet in cimp.sheet_list:
            print("\tSheet: {}".format(sheet))
            # sheet_folder_path = os.path.join(cimp_out_folder, sheet)
            # print("\tCreating folder: {}".format(sheet_folder_path))
            # if run_for_real:
            #     os.mkdir(sheet_folder_path)  # Create sheet folder

            res_rel = ResRel(excel_path=cimp.path, sheet_name=sheet)
            res_rel.read_dataframe()
            # res_rel.check()  # Was used to check the consistency of the dataframe

            print("\t\t{}".format(res_rel.sheet))
            # print(res_rel.df)

            # for col in res_rel.df.columns:
            #     print("\t\t\t{}".format(col))
            #     plt.close()
            #     plot = res_rel.df.plot.pie(labels=None, y=col, figsize=(5, 5), title=title_dict[col],
            #                                )
            #     plt.tight_layout()
            #     plt.axis('off')
            #     plt.show()
            #
            #     plt_save_path = os.path.join(sheet_folder_path, sheet + col + ".png")
            #     print("\t\t\tSaving at: {}".format(plt_save_path))
            #     if run_for_real:
            #         # plt.savefig(plt_save_path)
            #         pass

            sheet_image_path = os.path.join(cimp_out_folder, sheet + ".png")
            print("Saving at {}".format(sheet_image_path))
            plt.close()
            plt.rcParams.update({'font.size': 60})
            plot = res_rel.df.plot.pie(labels=None, subplots=True, figsize=(60, 12), legend=None)
            # plt.text(-10, -0.1, "(b)", snap= True, fontsize=60, rotation=90)
            # plt.title(rotation='vertical', x=-5.2, y=0.5)

            plt.tight_layout()
            # plt.show()
            if run_for_real:
                plt.savefig(sheet_image_path)
            else:
                plt.savefig(os.path.join(pi_folder_path, "lol.png"))
                break

            # pi_chart = PieChart(df=res_rel.df)
            # pi_chart.create()

        if not run_for_real:
            break


run_for_real = True
main()
