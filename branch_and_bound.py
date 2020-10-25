#!/usr/bin/python3

import json
from datetime import datetime
from distances_2_for_burma14 import count_distances
from create_reduced_matrix import row_cost, col_cost, path_constuctor, path_cost

start = datetime.now()


def cities_num(cities_and_location):

    cities_matrix = {}

    for num, city in enumerate(cities_and_location):
        cities_matrix[num] = city
         
    return cities_matrix



with open("/home/kognic/tsp/burma14.json", "r") as json_file:
    cities_location = json.load(json_file)

    all_distances = count_distances(cities_location)

    cities = cities_num(cities_location)

    row_reduced_matrix = row_cost(all_distances)[0]
    r_cost = row_cost(all_distances)[1]
    col_reduced_matrix = col_cost(row_reduced_matrix)[0]
    column_cost = col_cost(row_reduced_matrix)[1]

    start_cost = r_cost + column_cost

    path_and_cost = {}
    path_and_matrix = {}
    path_and_remained_pathes = {}
    path_way = {}

    start_num = 0

    for path_num in range(1, len(col_reduced_matrix)):
        total_path_cost = path_cost(col_reduced_matrix, path_num, start_num, start_cost)
        path_and_cost[f"{cities[start_num]}:{cities[path_num]}"] = total_path_cost[1]

        path_and_matrix[f"{cities[start_num]}:{cities[path_num]}"] = total_path_cost[0]
        path_and_remained_pathes[f"{cities[start_num]}:{cities[path_num]}"] = [n for n in range(1, len(all_distances)) if n != path_num]
        path_way[f"{cities[start_num]}:{cities[path_num]}"] = (path_num, )




    limit = len(path_and_cost) // 2
    while limit != 0:
        del path_and_cost[max(path_and_cost, key=path_and_cost.get)]
        limit -=1

    while True:
        start_num = min(path_and_cost, key=path_and_cost.get)

        if path_and_cost[start_num]:
            
            new_pathes = {}
            for path_num in path_and_remained_pathes[start_num]:

                total_path_cost = path_cost(path_and_matrix[start_num], path_num, path_way[start_num][-1], path_and_cost[start_num])

                path_and_cost[f"{start_num}:{cities[path_num]}"] = total_path_cost[1]

                path_and_matrix[f"{start_num}:{cities[path_num]}"] = total_path_cost[0]
                path_and_remained_pathes[f"{start_num}:{cities[path_num]}"] = [var for var in path_and_remained_pathes[start_num] if var != path_num]
                path_way[f"{start_num}:{cities[path_num]}"] = (path_num, )

                new_pathes[f"{start_num}:{cities[path_num]}"] = total_path_cost[1]


            if len(start_num.split(":")) != len(cities):

                limit = len(new_pathes) // 2
                while limit != 0:
                    max_num = max(new_pathes, key=new_pathes.get)
                    del path_and_cost[max_num]
                    del new_pathes[max_num]
                    limit -=1
                    del path_and_remained_pathes[max_num]
                    del path_and_matrix[max_num]
                    del path_way[max_num]


                del path_and_cost[start_num]
                del path_and_remained_pathes[start_num]
                del path_and_matrix[start_num]
                del path_way[start_num]



        if len(start_num.split(":")) == len(cities):
            print(f"{start_num}:{cities[0]}, {path_and_cost[start_num]}")
            break



end = datetime.now()
print(end - start)
