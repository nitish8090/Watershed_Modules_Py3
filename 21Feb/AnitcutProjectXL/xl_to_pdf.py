import os
import win32com.client
import sys

def main():
    excel_folder = r"F:\Watershed_Works\2102 Feb 2021\4_Anicut_Report\Round2\Output"
    output_pdf_folder = r"F:\Watershed_Works\2102 Feb 2021\4_Anicut_Report\Round2\Output\PDFs"

    o = win32com.client.gencache.EnsureDispatch("Excel.Application")
    print(sys.modules[o.__module__].__file__)
    # o.Visible = False

    excels = os.listdir(excel_folder)

    for excel in excels:
        print(excel)
        excel_path = os.path.join(excel_folder, excel)
        print(excel_path)

        # continue

        output_pdf_path = os.path.join(output_pdf_folder, os.path.splitext(excel)[0] + ".pdf")
        wb = o.Workbooks.Open(excel_path)

        ws_index_list = [i for i in range(1, 8)]  # say you want to print these sheets
        wb.WorkSheets(ws_index_list).Select()
        wb.ActiveSheet.ExportAsFixedFormat(0, output_pdf_path)

        # break


main()
