import geopandas as gpd
import matplotlib.pyplot as plt


def get_file():
    shape = gpd.read_file(r'D:\Nitish\1020_Oct\web\up_pop\up_dist_utm3.shp')
    shape.rename(columns={'ISO': 'Country Code', 'NAME_0': 'Country', 'yolo': 'golo'}, inplace=True)
    shape.plot()
    plt.grid(False)
    plt.axis('off')
    path_to_image = "static/larsen.png"
    plt.savefig(path_to_image)

    return path_to_image, shape


def get_stats():
    dataframe = gpd.read_file(r'D:\Nitish\1020_Oct\web\up_pop\up_dist_utm3.shp')

    # Total population
    total_population = dataframe['Population'].sum(axis=0)
    num_list = list(str(total_population))
    num_list.reverse()
    total_population = ""
    for i, num in enumerate(num_list):
        if i == 3:
            total_population = "," + total_population
        elif i % 2 != 0 and i > 3:
            total_population = "," + total_population
        total_population = num + total_population

    # No of districts
    no_of_districts = len(dataframe.index)

    # Maximum Density
    max_density = dataframe['Density'].max()

    return total_population, no_of_districts, max_density



print(get_stats())
