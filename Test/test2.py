import openpyxl

wb  = openpyxl.open(r"F:\Watershed_Works\2103 Mar 2021\1_PiExcel\Excels\CMIP5RCPP45.xlsx")
print(wb)

names = wb.sheetnames
print(names)
