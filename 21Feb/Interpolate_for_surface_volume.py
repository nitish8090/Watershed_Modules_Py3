from scipy import interpolate
import pandas as pd
import matplotlib.pyplot as plt


def main():
    known_points = r"F:\Watershed_Works\2102 Feb 2021\5_SurfaceVolume\Interpolate\known_points.csv"
    unknown_points = r"F:\Watershed_Works\2102 Feb 2021\5_SurfaceVolume\Interpolate\unknow_points.csv"

    known_points_df = pd.read_csv(known_points, delimiter='\t')
    known_points_df.sort_values(by=['Area'], inplace=True)
    print(known_points_df)

    unknown_points_df = pd.read_csv(unknown_points, delimiter='\t')
    unknown_points_df.sort_values(by=['Area'], inplace=True)
    unknown_points_df.drop([99], inplace=True)
    print(unknown_points_df)

    f = interpolate.interp1d(x=known_points_df.Area, y=known_points_df.Volume)
    unknown_points_df['Volume'] = f(unknown_points_df.Area)
    print(unknown_points_df)

    plt.plot(known_points_df.Area, known_points_df.Volume, 'o', unknown_points_df.Area, unknown_points_df.Volume, '-')
    plt.show()

    unknown_points_df.to_csv(r"F:\Watershed_Works\2102 Feb 2021\5_SurfaceVolume\Interpolate\interpolated_points.csv")

main()
