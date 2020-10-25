#!/usr/bin/python3

def row_cost(distances_matrix):

    row_min_cost_sum = 0

    distance_matrix = distances_matrix[:]
    row_reduced_matrix = []

    for town_dist in distance_matrix:

        if all(v is None for v in town_dist) == False:
            min_row_dist = min([val for val in town_dist if val is not None])
            row_reduced_matrix.append([dist if dist is None else (dist - min_row_dist) for dist in town_dist])
            row_min_cost_sum += min_row_dist

        else:
            row_reduced_matrix.append([None for dist in town_dist])

    return row_reduced_matrix, row_min_cost_sum



def col_cost(rows_reduced_matrix):

    row_reduced_matrix = rows_reduced_matrix[:]
    col_min_cost_sum = 0
    col_reduced_matrix = []

    reduced_matrix = list(map(list, zip(*row_reduced_matrix)))
    c_reduced_matrix = row_cost(reduced_matrix)
    col_reduced_matrix = list(map(list, zip(*c_reduced_matrix[0])))
    col_min_cost_sum = c_reduced_matrix[1]

    return col_reduced_matrix, col_min_cost_sum





def path_constuctor(reduced_matrix, path_num, start_num):

    path_matrix = reduced_matrix.copy()

    zip_path_matrix = list(map(list, zip(*path_matrix)))

    for n in range(len(zip_path_matrix[path_num])): 
        zip_path_matrix[path_num][n] = None

    path_matrix = list(map(list, zip(*zip_path_matrix)))
    path_matrix[path_num][start_num] = None

    for n in range(len(zip_path_matrix[start_num])): 
        path_matrix[start_num][n] = None

    return path_matrix



def path_cost(reduced_matrix, path_num, start_num, start_cost):

    col_reduced_matrix = reduced_matrix.copy()
    path_value = col_reduced_matrix[start_num][path_num]

    path_matrix = path_constuctor(col_reduced_matrix, path_num, start_num)

    row_reduced_path_matrix = row_cost(path_matrix)
    
    col_reduces_path_matrix = col_cost(row_reduced_path_matrix[0])
    total_path_cost = row_reduced_path_matrix[1] + col_reduces_path_matrix[1] + start_cost + path_value

    return col_reduces_path_matrix[0], total_path_cost
