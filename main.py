import servicesTreeHouse as sth
import numpy as np

#url to the problem: https://adventofcode.com/2022/day/8
#the map given in the exercise
quadcopter_map = [
    [3,0,3,7,3],
    [2,5,5,1,2],
    [6,5,3,3,2],
    [3,3,5,4,9],
    [3,5,3,9,0]
]
def tree_visibility_nb(quadcopter_map):
    nb_trees = 0
    my_map = np.array(quadcopter_map)
    map_shape = my_map.shape
    #if shape is (m,0)
    # if shape is (0,n)

    #shape is (m,n) where m and n are >0
    if (map_shape[0]) > 0 and (map_shape[1] >0):

        #count the top row of the map
        row_top = sth.count_top_row(my_map, 0, 1)
        nb_trees += row_top['count']
        print("top row")
        print(row_top['list_item'])

        # count the top column of the map. Here we should exclude the value already count on the row above
        col_top = sth.count_top_column(my_map, 0, 1)
        nb_trees += col_top['count']
        print("top column")
        print(col_top['list_item'])

        #count the bottom row of the map
        row_bottom = sth.count_top_row(my_map, map_shape[0]-1, map_shape[0]-2 )
        nb_trees += row_bottom['count']
        print("bottom row")
        print(row_bottom['list_item'])

        # count the top column of the map. Here we should exclude the value already count on the row above
        col_bottom = sth.count_top_column(my_map, map_shape[1]-1, map_shape[1]-2)
        nb_trees += col_top['count']
        print("bottom column")
        print(col_bottom['list_item'])

        #Work with data inside the map.
        inner_count = sth.count_inner_tree_value(my_map)
        nb_trees += inner_count['count']
        print("inner work")
        [print(i) for i in inner_count['list_item']]


    print("For the map below, the number of trees which are visible is: \033[1m ",nb_trees )
    [print(i) for i in quadcopter_map]

    return nb_trees



if __name__ == '__main__':
    tree_visibility_nb(quadcopter_map)
