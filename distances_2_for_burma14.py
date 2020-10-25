#!/usr/bin/python3
from math import cos, sin, asin, sqrt, floor, pi, ceil

Earth_equatorial_radius_km = 6378



def count_distances(cities_and_location):

    distance_matrix = []

    # Positive latitude is assumed to be 'North', negative latitude means 'South'
    # Positive longitude means 'East', negative longitude is assumed to be 'West'

    for key, value in cities_and_location.items():
        total_x = floor(value["x"])
        min_part_x = value["x"] - total_x
        lat_x = total_x + ( 5 * min_part_x / 3)

        latitude_start = pi * lat_x / 180

        total_y = floor(value["y"])
        min_part_y = value["y"] - total_y
        lon_y = total_y + ( 5 * min_part_y / 3)

        longitude_start = pi * lon_y / 180
 
        distances = []
        for key2, value2 in cities_and_location.items():

            if key == key2:
                distance = None
       
            else:
                

                total_x_2 = floor(value2["x"])
                min_part_x_2 = value2["x"] - total_x_2
                lat_x_2 = total_x_2 + ( 5 * min_part_x_2 / 3)

                latitude_end = pi * lat_x_2 / 180

                total_y_2 = floor(value2["y"])
                min_part_y_2 = value2["y"] - total_y_2
                lon_y_2 = total_y_2 + ( 5 * min_part_y_2 / 3)

                longitude_end = pi * lon_y_2 / 180


                # Haversine formula

                dist_lon = longitude_end - longitude_start 
                dist_lat = latitude_end - latitude_start 

                hav = sin(dist_lat / 2) ** 2 + cos(latitude_start) * cos(latitude_end) * sin(dist_lon / 2) ** 2
                distance = ceil(2 * Earth_equatorial_radius_km * asin(sqrt(hav)))

           
            distances.append(distance)
        distance_matrix.append(distances)

    return distance_matrix
