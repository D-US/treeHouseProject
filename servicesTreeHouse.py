#####
#This class is where we defined all our functions

#Count the number of tree for the top or bottom row
def count_top_row(map_list, index_top, index_next):
    top_row = map_list[index_top]
    bottom_row = map_list[index_next]
    highest_trees_list = [-1]* len(top_row)
    count_trees = 0
    for i in range(len(top_row)):
        if top_row[i] > bottom_row[i]:
            count_trees +=1
            highest_trees_list[i] = top_row[i]
    return {
                "count" :count_trees,
                "list_item": highest_trees_list
             }

#Count the number of tree for the top or bottom column
def count_top_column(map_list, index_top, index_next):
    tempo_top = map_list[:,index_top]
    top_col = tempo_top[1:len(tempo_top)-1]

    tempo_bot = map_list[:,index_next]
    bottom_col = tempo_bot[1:len(tempo_top)-1]
    highest_trees_list = [-1]* len(top_col)
    count_trees = 0
    for i in range(len(top_col)):
        if top_col[i] > bottom_col[i]:
            count_trees +=1
            highest_trees_list[i] = top_col[i]

    return {
                "count" :count_trees,
                "list_item": highest_trees_list
             }

def count_inner_tree_value(map_list):
    list_shape = map_list.shape
    count_val = 0
    temp = []
    for i in range(1, list_shape[0]-1):

        templist = [-1]* (list_shape[0]-2)
        for j in range(1,list_shape[1]-1 ):
           if  (is_tree_visible_row(map_list, i, j) ) or is_tree_visible_col(map_list, i, j):
                count_val +=1
                index = (j-1)
                templist[index] = map_list[i,j]
        temp.append(templist)

    return {
                "count" :count_val,
                "list_item": temp
             }




def is_tree_visible_row(map_list, row_val, col_value):
    if (map_list[row_val, col_value] > map_list[(row_val), (col_value-1)]) and \
            (map_list[row_val, col_value] > map_list[(row_val), (col_value +1)]):
        return True
    return False

def is_tree_visible_col(map_list, row_val, col_value):
    if (map_list[row_val, col_value] > map_list[(row_val-1), (col_value)]) and \
            (map_list[row_val, col_value] > map_list[(row_val +1), (col_value)]):
        return True
    return False