import matplotlib.pyplot as plt
import os
import pandas as pd


class Excels:
    def __init__(self, folder):
        self.folder = folder
        self.list = []

    def read_list(self):
        self.list = os.listdir(self.folder)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.list):
            print("Progress: [{}/{}] {:.2f}%".format(self.n + 1, len(self.list), ((self.n + 1) / len(self.list)) * 100),
                  end='')
            excel_path = os.path.join(self.folder, self.list[self.n])
            self.n += 1
            return Excel(path=excel_path)
        else:
            raise StopIteration


class Excel:
    def __init__(self, path):
        self.path = path
        self.name = os.path.split(self.path)[1]
        self.stream_id = self.name.split("_")[2]

    def plot_graph(self):
        print(" ||| Currently Working: {}".format(self.stream_id))
        df = pd.read_excel(self.path)
        # print(df)
        title = "Longitudinal Section (Stream ID: {})".format(self.stream_id)
        df_line = df.plot.line(x='cum_dist', y='Elevation', title=title, legend=False, xlabel='Distance (m)',
                               ylabel='Elevation (m)', figsize=(5.95, 2.8))
        plt.tight_layout()
        df_line.grid(b=None, which='major', axis='y')

    def save_graph(self, save_path):
        plt.savefig(save_path, dpi=180)

    def clear_graph(self):
        plt.cla()
        plt.clf()
        plt.close()


def main():
    excels = Excels(folder=r'D:\Nitish\26_States\2_MP\MP_LongitudinalSection\IndividualExcels')
    output_folder = r"D:\Nitish\26_States\2_MP\MP_LongitudinalSection\IndividualCharts2"

    excels.read_list()
    for excel in excels:
        excel.plot_graph()

        output_image_name = "Stream_{}_LongitudinalSection.png".format(excel.stream_id)
        save_path = os.path.join(output_folder, output_image_name)
        excel.save_graph(save_path=save_path)

        excel.clear_graph()



main()
