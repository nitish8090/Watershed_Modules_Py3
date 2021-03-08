import matplotlib.pyplot as plt
import os
import pandas as pd


def main():
    excel_folder = r'F:\Watershed_Works\2102 Feb 2021\CG_Longitudinal_Section\CG_OutputExcel_LongitudinalSection'
    output_folder = r"F:\Watershed_Works\2102 Feb 2021\CG_Longitudinal_Section\ImagesLongSec"

    for excel in os.listdir(excel_folder):
        stream_id = excel.split("_")[2]
        print(stream_id)
        if str(stream_id)[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            continue

        print(excel)
        excel_path = os.path.join(excel_folder, excel)

        df = pd.read_excel(excel_path)
        # print(df)
        title = "Longitudinal Section (Stream ID: {})".format(stream_id)
        df_line = df.plot.line(x='cum_dist', y='Elevation', title=title, legend=False, xlabel='Distance (m)',
                               ylabel='Elevation (m)', figsize=(5.95, 2.8))
        otuput_image_name = "Stream_{}_LongitudinalSection.png".format(stream_id)
        save_path = os.path.join(output_folder, otuput_image_name)
        # df_line.figure(figsize=(20, 10))
        plt.tight_layout()
        df_line.grid(b=None, which='major', axis='y')
        # plt.show()
        plt.savefig(save_path, dpi=180)
        # break


main()
