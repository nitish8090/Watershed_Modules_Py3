from netCDF4 import Dataset
import numpy as np
import os

main_dir = r"C:\Users\lenovo1\Downloads\BNU_output\BNU_output"


def get_files(path):
    files = os.listdir(path)
    return_files = []
    for file in files:
        if file.endswith(".nc"):
            return_files.append(file)
    return return_files


# nc_file = r"C:\Users\lenovo1\Downloads\BNU_output\BNU_output\bias_corrected_TMAX_BNUESM_rcp45_2006_2100_setaxis_fldmean.nc"
# fh = Dataset(nc_file, mode='r')

# for var in fh.variables:
#     print(var)
#     print("__________")

# time = fh.variables['time'][:]
# time_bnds = fh.variables['time_bnds'][:]
# lon = fh.variables['lon'][:]
# lat = fh.variables['lat'][:]
# TMAX = fh.variables['TMAX'][:]

# print(fh.variables['time'])

for nc_file in get_files(main_dir):
    print("FILE: " + nc_file)
    fh = Dataset(os.path.join(main_dir, nc_file), mode='r')
    # for variable in fh.variables:
    #     print(variable)
    #     if True:
    #         var = fh.variables[variable][:]
    #         print(var)
    #     # print("------")
    for variable in fh.variables:
        print(variable)

    # print(fh['TMAX'])
    # exit()
    print("###########################")
