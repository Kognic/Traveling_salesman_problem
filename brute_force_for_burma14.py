#!/usr/bin/python3

import json
from itertools import permutations
from distances_for_burma14 import count_distances
from datetime import datetime



def path_distances(all_distances, path):

    path_distance = 0
    
    for num in range(0, len(path) - 1):
        start_point = path[num]
        end_point = path[num + 1]
        
        path_distance += all_distances[start_point][end_point]

    return path_distance


start = datetime.now()


with open("/home/kognic/tsp/burma14.json", "r") as json_file:
    cities_location = json.load(json_file)

    all_distances = count_distances(cities_location)
    start_point = "1"

    all_cities = [town for town in cities_location if town != start_point]

    list_of_pathes = list(map(lambda pathes: (start_point,) + pathes + (start_point,), list(permutations(all_cities))))
    minimal = min(list_of_pathes, key=lambda path: path_distances(all_distances, path))

    print(f"{minimal} -> {path_distances(all_distances, minimal)}")


end = datetime.now()
print(end - start)
