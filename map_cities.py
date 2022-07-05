"""
 Map cities from .csv file to Map of US based on finding provided list in existing list of US cities with their lat
 and long.

 After connecting the provided cities to those in the US Database list, map the cities with their Rankings,
 City Name, on the correct Latitude and Longitude.
"""


def read_city_list():
    with open('uscities.csv', mode='r', encoding='utf-8') as file:
        us_cities = file.read()

        # add code here to match provided cities to us_cities
        
        file.close()
