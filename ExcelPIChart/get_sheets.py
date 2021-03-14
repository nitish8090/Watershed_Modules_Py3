import openpyxl
import os


def main():
    excel_folder = r"F:\Watershed_Works\2103 Mar 2021\1_PiExcel\Excels"

    excels = os.listdir(excel_folder)

    for excel in excels:
        if excel.startswith("~"):
            continue
        print(excel)
        excel_path = os.path.join(excel_folder, excel)

        workbook = openpyxl.open(excel_path)
        sheets = workbook.sheetnames

        print(sheets)


main()
"""
book3CIMP5 RCP 4(AutoRecovered).xlsx
['Rel_P_DROUGHT', 'Res_P_DROUGHT', 'Vul_P_DROUGHT', 'RRV_P_DROUGHT', 'Rel_PET', 'Res_PET', 'Vul_PET', 'RRV_PET', 'Rel_PERC_GW', 'Res_PERC_GW', 'Vul_PERC_GW', 'RRV_PERC_GW', 'Rel_SURQ_HIGH', 'Res_SURQ_HIGH', 'Vul_SURQ_HIGH', 'RRV_SURQ_HIGH', 'Rel_SYLD', 'Res_SYLD', 'Vul_SYLD', 'RRV_SYLD', 'VUL_WHI_NEW', 'Rel_WHI', 'Res_WHI', 'Vul_WHI', 'Sheet1', 'WHI', 'WHI_NEW', 'WHI_C']
book3CIMP5 RCP 4.5.xlsx
['Rel_P_DROUGHT', 'Res_P_DROUGHT', 'Vul_P_DROUGHT', 'RRV_P_DROUGHT', 'Rel_PET', 'Res_PET', 'Vul_PET', 'RRV_PET', 'Rel_PERC_GW', 'Res_PERC_GW', 'Vul_PERC_GW', 'RRV_PERC_GW', 'Rel_SURQ_HIGH', 'Res_SURQ_HIGH', 'Vul_SURQ_HIGH', 'RRV_SURQ_HIGH', 'Rel_SYLD', 'Res_SYLD', 'Vul_SYLD', 'RRV_SYLD', 'Rel_WHI', 'Res_WHI', 'Vul_WHI', 'WHI', 'WHI_C']
book3CIMP5 RCP 8.5.xlsx
['Rel_P_DROUGHT', 'Res_P_DROUGHT', 'Vul_P_DROUGHT', 'RRV_P_DROUGHT', 'Rel_PET', 'Res_PET', 'Vul_PET', 'RRV_PET', 'Rel_PERC_GW', 'Res_PERC_GW', 'Vul_PERC_GW', 'RRV_PERC_GW', 'Rel_SURQ_HIGH', 'Res_SURQ_HIGH', 'Vul_SURQ_HIGH', 'RRV_SURQ_HIGH', 'Rel_SYLD', 'Res_SYLD', 'Vul_SYLD', 'RRV_SYLD', 'Rel_WHI', 'Res_WHI', 'Vul_WHI', 'WHI', 'WHI_C']
book3CIMP6 RCP 4.5-1.xlsx
['Rel_P_DROUGHT', 'Res_P_DROUGHT', 'Vul_P_DROUGHT', 'RRV_P_DROUGHT', 'Rel_PET', 'Res_PET', 'Vul_PET', 'RRV_PET', 'Rel_PERC_GW', 'Res_PERC_GW', 'Vul_PERC_GW', 'RRV_PERC_GW', 'Rel_SURQ_HIGH', 'Res_SURQ_HIGH', 'Vul_SURQ_HIGH', 'RRV_SURQ_HIGH', 'Rel_SYLD', 'Res_SYLD', 'Vul_SYLD', 'RRV_SYLD', 'Rel_WHI', 'Res_WHI', 'Vul_WHI', 'WHI', 'WHI_C', 'Sheet1']
book3CIMP6 RCP 8.5-1 (1).xlsx
['Rel_P_DROUGHT', 'Res_P_DROUGHT', 'Vul_P_DROUGHT', 'RRV_P_DROUGHT', 'Rel_PET', 'Res_PET', 'Vul_PET', 'RRV_PET', 'Rel_PERC_GW', 'Res_PERC_GW', 'Vul_PERC_GW', 'RRV_PERC_GW', 'Rel_SURQ_HIGH', 'Res_SURQ_HIGH', 'Vul_SURQ_HIGH', 'RRV_SURQ_HIGH', 'Rel_SYLD', 'Res_SYLD', 'Vul_SYLD', 'RRV_SYLD', 'Rel_WHI', 'Res_WHI', 'Vul_WHI', 'WHI', 'WHI_C']
"""
