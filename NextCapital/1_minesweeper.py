import re
def in_graph(curr_row, curr_col, row_size, col_size):
    if curr_row < 0 or curr_col < 0:
        return False
    if curr_row >= row_size or curr_col >= col_size:
        return False
    return True

def solve_minesweeper(puzzle_array):
    row_len = len(puzzle_array)
    col_len = len(puzzle_array[0])
    #print(row_len)
    #print(col_len)
    result = []
    for i in range(row_len):
        inner_list = []
        for j in range(col_len):
            inner_list.append(0)
        result.append(inner_list)


    for row in range(0,row_len):
        # bomb in row: rule 4
        bomb_in_row = False
        if row % 2 != 0:
            bomb_in_row = False
            for temp_col in range(0, col_len):
                if puzzle_array[row][temp_col] == 'm':
                    bomb_in_row = True
                    break
        for col in range(0,col_len):
            if puzzle_array[row][col] =='m':
                result[row][col] = -1
            elif puzzle_array[row][col] == '.':
                curr_cell_val = 0
                #check adj
                if in_graph(row-1 , col-1, row_len, col_len) and puzzle_array[row-1][col-1] == 'm':
                    curr_cell_val += 1
                if in_graph(row-1, col, row_len, col_len) and puzzle_array[row-1][col] == 'm':
                    curr_cell_val += 1
                if in_graph(row-1, col+1, row_len, col_len) and puzzle_array[row-1][col+1] == 'm':
                    curr_cell_val += 1
                if in_graph(row, col+1, row_len, col_len) and puzzle_array[row][col+1] == 'm':
                    curr_cell_val += 1
                if in_graph(row, col-1, row_len, col_len) and puzzle_array[row][col-1] == 'm':
                    curr_cell_val += 1
                if in_graph(row+1, col+1, row_len, col_len) and puzzle_array[row+1][col+1] == 'm':
                    curr_cell_val += 1
                if in_graph(row+1, col, row_len, col_len) and puzzle_array[row+1][col] == 'm':
                    curr_cell_val += 1
                if in_graph(row+1, col-1, row_len, col_len) and puzzle_array[row+1][col-1] == 'm':
                    curr_cell_val +=1
                print('for row, col ',row,col,'cur_cell after 1st rule: ',curr_cell_val)
                #check if its below a mine - double
                if in_graph(row-1, col, row_len, col_len) and puzzle_array[row-1][col] == 'm':
                    #curr_cell_val = curr_cell_val *2
                    curr_cell_val = 2
                print('for row, col ', row, col, 'cur_cell after 2nd rule: ', curr_cell_val)
                # if its right of  a bomb - set to zero
                if in_graph(row, col-1, row_len, col_len) and puzzle_array[row][col-1] == 'm':
                    curr_cell_val = 0
                print('for row, col ', row, col, 'cur_cell after 3rd rule: ', curr_cell_val)
                # row with bomb - triple
                if bomb_in_row:
                    curr_cell_val = curr_cell_val * 3
                print('for row, col ', row, col, 'cur_cell after 4th rule: ', curr_cell_val)

                # corners are doubled
                if in_graph(row - 1, col - 1, row_len, col_len) and puzzle_array[row - 1][col - 1] == 'm':
                    curr_cell_val = curr_cell_val*2
                elif in_graph(row - 1, col + 1, row_len, col_len) and puzzle_array[row - 1][col + 1] == 'm':
                    curr_cell_val = curr_cell_val*2
                elif in_graph(row + 1, col + 1, row_len, col_len) and puzzle_array[row + 1][col + 1] == 'm':
                    curr_cell_val = curr_cell_val * 2
                elif in_graph(row + 1, col - 1, row_len, col_len) and puzzle_array[row + 1][col - 1] == 'm':
                    curr_cell_val = curr_cell_val * 2
                #print('for row, col ', row, col, 'cur_cell after 5th rule: ', curr_cell_val)
                result[row][col] = curr_cell_val
                #print('for row, col ', row, col, 'result:',result)
                #print('------------------------------------------------')
    print(result)
    return result

if __name__ =="__main__":
    #puzzle_array = [['.','m','.','.'], ['.','.','.','.'], ['.','.','.','m'], ['m','.','.','.']]
    #puzzle_array = [['m', 'm', 'm', 'm'], ['m', 'm', 'm', 'm'], ['m', 'm', 'm', 'm'], ['m', 'm', 'm', 'm']]
    #puzzle_array = [['m', 'm', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['.', '.', '.', '.']]
    puzzle_array = [['.', 'm', '.', '.'], ['.', '.', 'm', '.'], ['.', '.', '.', '.'], ['m', '.', '.', '.']]
    solve_minesweeper(puzzle_array)