import pandas as pd
import os


def main():
    excel_folder = r"D:\Nitish\2101_Jan\7_IWMP_Progress_Dump_Download\13_14"
    output_path = r"D:\Nitish\2101_Jan\7_IWMP_Progress_Dump_Download"
    output_excel = "13_14_All_District.xlsx"
    excels = os.listdir(excel_folder)

    for i, excel in enumerate(excels):

        print("Working: " + excel)
        excel_path = os.path.join(excel_folder, excel)
        if i == 0:
            df = pd.read_excel(excel_path)
        else:
            new_df = pd.read_excel(excel_path)
            df = pd.concat([df, new_df])
        print(df)

    df.to_excel(os.path.join(output_path, output_excel))
        # break


main()
