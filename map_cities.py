"""
 Map cities from .csv file to Map of US based on finding provided list in existing list of US cities with their lat
 and long.

 After connecting the provided cities to those in the US Database list, map the cities with their Rankings,
 City Name, on the correct Latitude and Longitude.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_city_list():
    us_cities = pd.read_csv('uscities.csv')
    us_cities.head()
    bounding_box = ((us_cities.lng.min(), us_cities.lng.max(),
                     us_cities.lat.min(), us_cities.lat.max()))
    us_map = plt.imread('US_map.png')
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.scatter(us_cities.lng, us_cities.lat, zorder=1, alpha=0.2, c='b', s=10)
    ax.set_title('US Cities')
    ax.set_xlim(bounding_box[0], bounding_box[1])
    ax.set_ylim(bounding_box[2], bounding_box[3])
    ax.imshow(us_map, zorder=0, extent=bounding_box, aspect='equal')
    plt.show()


if __name__ == "__main__":
    read_city_list()
