import os
import csv
import pandas as pd
import numpy as np
from collections import namedtuple


class WeatherDataFiles:
    WeatherDataFile = namedtuple('WeatherDataFile', ['name', 'path', 'code'])

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = []

    def set_list_of_files(self):
        for csv_file in os.listdir(self.folder_path):
            if csv_file.startswith("weatherdata") and csv_file.endswith(".csv"):
                code = os.path.splitext(csv_file)[0].split("-")[1]
                w1 = self.WeatherDataFile(name=csv_file, path=os.path.join(self.folder_path, csv_file), code='p' + code)
                self.files.append(w1)
                # "weatherdata-236728.csv"


class RandomPoints:
    def __init__(self, path):
        self.path = path
        self.df = None
        self.lat_header = ''
        self.long_header = ''

    def read_dataframe(self):
        self.df = pd.read_csv(self.path)

    def set_lat_long_header(self, lat, long):
        self.lat_header = lat
        self.long_header = long


class DataPoints:
    def __init__(self, path):
        self.path = path
        self.df = None

    def read_dataframe(self):
        self.df = pd.read_csv(self.path)


class StationCSV:
    def __init__(self, path):
        self.path = path
        self.df = None
        self.lat = None
        self.long = None

    def read_dataframes(self):
        self.df = pd.read_csv(self.path, index_col=False)
        self.lat = self.df.Latitude[0]
        self.long = self.df.Longitude[0]


class IndividualRandomPoint:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long
        self.nearDF = None
        self.mainDF = None

    def set_known_point_dataframes(self, known_points_dataframe):
        """Make a copy of dataframe and calculate distance"""
        self.nearDF = known_points_dataframe.copy()
        self.nearDF['Distance'] = np.nan

    def calculate_distance(self):
        self.nearDF['Distance'] = ((self.nearDF.LAT - self.lat) ** 2 + (self.nearDF.LONG - self.long) ** 2) ** 0.5

    def create_main_dataframe(self, weather_data_file):
        station_csv = StationCSV(weather_data_file.path)
        station_csv.read_dataframes()

        self.mainDF = pd.DataFrame({'Date': station_csv.df.Date})

        self.mainDF['Longitude'] = self.long
        self.mainDF['Latitude'] = self.lat

    def calculate_pixel_values(self):
        pass


def main():
    input_data_path = r"C:\Users\lenovo1\PycharmProjects\ShellDrop\NProcessing\InputData\38166_2021-02-13-08-18-25\38166_2021-02-13-08-18-25"
    data_points = DataPoints(os.path.join(input_data_path, "pcp.txt"))
    random_points = RandomPoints(r"C:\Users\lenovo1\PycharmProjects\ShellDrop\NProcessing\InputData\RandomPoints.csv")
    random_points.set_lat_long_header(lat='Lat', long='Long')

    weather_data_files = WeatherDataFiles(folder_path=os.path.join(input_data_path))
    weather_data_files.set_list_of_files()

    # for weather_data_file in weather_data_files.files:
    #     print(weather_data_file)
    #
    #     station_csv = StationCSV(weather_data_file.path)
    #     station_csv.read_dataframes()
    #     print(station_csv.df)

    data_points.read_dataframe()
    print(data_points.df)

    random_points.read_dataframe()
    print(random_points.df)

    for row in random_points.df.itertuples():
        lat, long = (getattr(row, random_points.lat_header), getattr(row, random_points.long_header))
        indivial_random_point = IndividualRandomPoint(lat, long)
        indivial_random_point.set_known_point_dataframes(data_points.df)
        indivial_random_point.calculate_distance()

        print("______________________")
        print(indivial_random_point.lat, indivial_random_point.long)
        print(indivial_random_point.nearDF)

        print("_______________________________________________")
        indivial_random_point.create_main_dataframe(weather_data_file=weather_data_files.files[1])
        indivial_random_point.calculate_pixel_values()
        print(indivial_random_point.mainDF)


# def calculate_distance():


main()
