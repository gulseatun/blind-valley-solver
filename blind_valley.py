import sys

#Checking if placing a high tile at the given position is valid
def check_high(layout, constraints, column, row, row_number, column_number):

    #Getting high constraints
    row_high = int(constraints[0][row])
    column_high = int(constraints[2][column])

    #Checking if no high tiles are required in the row or column
    if row_high == 0 or column_high == 0:
        return False
    
    #Checking if there are no high tile constraints in both row and column
    if row_high+column_high == -2:
        return True

    #Checking high constraints in both row and column
    if row_high != -1 and column_high != -1: 
        high_number_row = 0
        for i in range(column_number):
            if layout[row][i] == 'H':
                high_number_row += 1

        high_number_column = 0
        for i in range(row_number):
            if layout[i][column] == 'H':
                high_number_column += 1

        #Checking if the number of high tiles matches the constraints
        if column_high != high_number_column and row_high != high_number_row:

            #Checking specific conditions based on the type of the tile
            if layout[row][column] == "L":
                if column_number-column-2 >= (row_high-high_number_row-1)*2 - 1 and \
                   row_number-row -1 >= (column_high- high_number_column-1)*2: 
                    return True
                
            if layout[row][column] == "R":
                if column_number-column-1 >= (row_high - high_number_row-1)*2 and \
                   row_number-row -1 >= (column_high - high_number_column-1)*2: 
                    return True
                
            if layout[row][column] == "U":
                if column_number-column-1 >= (row_high - high_number_row-1)*2 and \
                   row_number-row-2 >= (column_high-high_number_column-1)*2-1:
                    return True

            if layout[row][column] == "D":
                left_tile_number = 0
                for i in layout[row][:column]:
                    if i == "L" :
                        left_tile_number += 1
                        
                if column_number-column-1 >= (row_high - high_number_row-1-left_tile_number)*2 and \
                   row_number-row-1 >= (column_high-high_number_column-1)*2:
                    return True
        else:
            return False
        
    #Checking if only the column requires high tiles
    if row_high == -1:
        high_number_column = 0
        for i in range(row_number):
            if layout[i][column] == 'H':
                high_number_column += 1

        #Checking if the number of high tiles in the column matches the constraint
        if column_high != high_number_column:

            #Checking specific conditions based on the type of the tile
            if layout[row][column] == "L":
                if row_number-row -1 >= (column_high- high_number_column-1)*2:
                    return True
                
            if layout[row][column] == "R":
                if row_number-row -1 >= (column_high - high_number_column-1)*2: 
                    return True
                
            if layout[row][column] == "U":
                if row_number-row-2 >= (column_high-high_number_column-1)*2-1:                  
                    return True

            if layout[row][column] == "D":
                if row_number-row-1 >= (column_high-high_number_column-1)*2:                   
                    return True
        else:
            return False

    #Checking if only the row requires high tiles
    if column_high == -1:      
        high_number_row = 0
        for i in range(column_number):
            if layout[row][i] == 'H':
                high_number_row += 1

        #Checking if the number of high tiles in the row matches the constraint
        if row_high != high_number_row:

            #Checking specific conditions based on the type of the tile
            if layout[row][column] == "L":
                if column_number-column-2 >= (row_high-high_number_row-1)*2 - 1:
                    return True
                
            if layout[row][column] == "R":
                if column_number-column-1 >= (row_high - high_number_row-1)*2: 
                    return True
                
            if layout[row][column] == "U":
                if column_number-column-1 >= (row_high - high_number_row-1)*2:
                    return True

            if layout[row][column] == "D":
                left_tile_number = 0
                for i in layout[row][:column]:
                    if i == "L" :
                        left_tile_number += 1
                if column_number-column-1 >= (row_high - high_number_row-1 - left_tile_number)*2:
                    return True
        else:
            return False

            
    return False

#Checking if placing a base tile at the given position is valid
def check_base(layout, constraints, column, row, row_number, column_number):

    #Getting base constraints
    row_base = int(constraints[1][row])
    column_base = int(constraints[3][column])

    #Checking if no base tiles are required in the row or column
    if row_base == 0 or column_base == 0:
        return False
    
    #Checking if there are no base tile constraints in both row and column
    if row_base+column_base == -2:
        return True

    #Checking high constraints in both row and column
    if row_base != -1 and column_base != -1: 
        base_number_row = 0
        for i in range(column_number):
            if layout[row][i] == 'B':
                base_number_row += 1

        base_number_column = 0
        for i in range(row_number):
            if layout[i][column] == 'B':
                base_number_column += 1

        #Checking if the number of base tiles matches the constraints
        if column_base != base_number_column and row_base != base_number_row:

            #Checking specific conditions based on the type of the tile
            if layout[row][column] == "L":
                if column_number-column-2 >= (row_base-base_number_row-1)*2 - 1 and \
                   row_number-row -1 >= (column_base- base_number_column-1)*2: 
                    return True
                
            if layout[row][column] == "R":
                if column_number-column-1 >= (row_base - base_number_row-1)*2 and \
                   row_number-row -1 >= (column_base - base_number_column-1)*2: 
                    return True
                
            if layout[row][column] == "U":
                if column_number-column-1 >= (row_base - base_number_row-1)*2 and \
                   row_number-row-2 >= (column_base-base_number_column-1)*2-1:
                    return True

            if layout[row][column] == "D":
                left_tile_number = 0
                for i in layout[row][:column]:
                    if i == "L" :
                        left_tile_number += 1
                if column_number-column-1 >= (row_base - base_number_row-1- left_tile_number)*2 and \
                   row_number-row-1 >= (column_base-base_number_column-1)*2:
                    return True
        else:
            return False
        
    #Checking if only the column requires base tiles
    if row_base == -1:
        base_number_column = 0
        for i in range(row_number):
            if layout[i][column] == 'B':
                base_number_column += 1

        #Checking if the number of base tiles in the column matches the constraint
        if column_base != base_number_column:

            #Checking specific conditions based on the type of the tile
            if layout[row][column] == "L":
                if row_number-row -1 >= (column_base- base_number_column-1)*2:
                    return True
                
            if layout[row][column] == "R":
                if row_number-row -1 >= (column_base - base_number_column-1)*2: 
                    return True
                
            if layout[row][column] == "U":
                if row_number-row-2 >= (column_base-base_number_column-1)*2-1:                  
                    return True

            if layout[row][column] == "D":
                if row_number-row-1 >= (column_base-base_number_column-1)*2:                   
                    return True
        else:
            return False

    #Checking if only the row requires base tiles
    if column_base == -1:     
        base_number_row = 0 
        for i in range(column_number):
            if layout[row][i] == 'B':
                base_number_row += 1

        #Checking if the number of base tiles in the row matches the constraint
        if row_base != base_number_row:

            #Checking specific conditions based on the type of the tile
            if layout[row][column] == "L":
                if column_number-column-2 >= (row_base-base_number_row-1)*2 - 1:
                    return True
                
            if layout[row][column] == "R":
                if column_number-column-1 >= (row_base - base_number_row-1)*2: 
                    return True
                
            if layout[row][column] == "U":
                if column_number-column-1 >= (row_base - base_number_row-1)*2:
                    return True

            if layout[row][column] == "D":
                left_tile_number = 0
                for i in layout[row][:column]:
                    if i == "L" :
                        left_tile_number += 1
                if column_number-column-1 >= (row_base - base_number_row-1- left_tile_number)*2:
                    return True
        else:
            return False
            
    return False


#Checking if placing a tile of a given type at a specific location is valid based on neighboring tiles.
def check_neighbours(layout, column, row, row_number, column_number, tile_type):

    #Checking if the tile is in the top-left corner
    if column == 0 and row == 0:
            return True
        
    #Checking for tiles in the middle of the board
    if 0<column<column_number-1 and 0<row<row_number-1:
        if not tile_type in (layout[row][column+1], layout[row][column-1], layout[row-1][column]):
            return True
    
    #Checking for tiles on the top edge of the board
    if row == 0 and column != column_number-1:
        if not tile_type in (layout[row][column+1], layout[row][column-1]):
            return True       

    #Checking for tiles on the left edge of the board
    if column == 0 and row != row_number-1:
        if not tile_type in (layout[row][column+1], layout[row-1][column]):
            return True
        
    #Checking for tiles in the middle of the last row
    if row == row_number -1 and column != 0 and column != column_number-1:
        if not tile_type in (layout[row-1][column], layout[row][column-1], layout[row][column+1]):
            return True

    #Checking for tiles on the right edge of the board
    if column == column_number-1 and row != 0:
        if not tile_type in (layout[row-1][column], layout[row][column-1]):
            return True
        
    #Checking for tiles on the top edge of the board
    if row == 0:
        if layout[row][column-1] != tile_type:
            return True
        
    #Checking for tiles on the left edge of the board
    if column == 0:
        if not tile_type in (layout[row][column+1], layout[row-1][column]):
            return True
    
    #Checking for tiles in the bottom edge of the board
    if row == row_number-1:
        if not tile_type in (layout[row][column-1], layout[row-1][column]):
            return True
 
    return False

#Checking if placing a neutral tile at the given position is valid
def check_for_n(layout, constraints, column, row, row_number, column_number, cells_element):

    #Getting constraints for the current cell's row and column
    row_base =int(constraints[1][row])
    column_base = int(constraints[3][column])
    row_high = int(constraints[0][row])
    column_high = int(constraints[2][column])

    #Checking if the current cell type is vertical
    if cells_element[2] == "U":

        #Getting constraint values for the cell below the current cell
        row_high_below = int(constraints[0][row+1])
        row_base_below = int(constraints[1][row+1])

        #Initializing counts for high and base numbers in different positions
        high_number_below_row = 0
        base_number_below_row = 0
        high_number_row = 0
        base_number_row = 0

        #Counting high and base numbers in the current cell's row and the row below
        for i in range(column_number):
            if layout[row][i] == 'H':
                high_number_row += 1

            if layout[row+1][i] == "H":
                high_number_below_row += 1

            if layout[row+1][i] == "B":
                base_number_below_row += 1

            if layout[row][i] == 'B':
                base_number_row += 1

        #Initializing counts for high and base numbers in different positions
        high_number_column = 0
        base_number_column = 0

        #Counting high and base numbers in the current cell's column
        for i in range(row_number):
            if layout[i][column] == 'H':
                high_number_column += 1
                
            if layout[i][column] == 'B':
                base_number_column += 1

        #Counting empty horizontal left tiles  
        left_tile_number = 0
        for i in layout[row+1][:column]:
            if i == "L" :
                left_tile_number += 1

        #Counting base and high numbers on the right side of the cell
        right_tile_base_number = 0
        right_tile_high_number = 0
        for i in layout[row][column:]:
            if i == "B" :
                right_tile_base_number += 1
            if i == "H":
                right_tile_high_number += 1

        #Counting base and high numbers on the right side of the below cell
        right_tile_base_number_below = 0
        right_tile_high_number_below = 0
        for i in layout[row+1][column:]:
            if i == "B" :
                right_tile_base_number_below += 1
            if i == "H":
                right_tile_high_number_below += 1

        #Checking if the constraints are satisfied for placing neutral tile in the given position
        if column_number - column-1 -(right_tile_base_number)*2>= (row_base - base_number_row)*2 -1 and \
            column_number - column-1 -(right_tile_base_number_below)*2>= (row_base_below - base_number_below_row- left_tile_number)*2-1 and \
            column_number - column-1 -(right_tile_high_number)*2>= (row_high - high_number_row)*2-1 and \
            column_number - column-1 -(right_tile_high_number_below)*2>= (row_high_below - high_number_below_row-left_tile_number)*2-1 and \
            row_number - row - 2 >= (column_high - high_number_column)*2-1 and \
            row_number- row - 2 >= (column_base- base_number_column)*2-1:
            return True
        
    #Checking if the current cell type is horizontal
    if cells_element[2] == "L":

         #Getting constraint values for the cell right to the current cell
        column_base_right = int(constraints[3][column+1])
        column_high_right = int(constraints[2][column+1])

        #Initializing counts for high and base numbers in different positions
        high_number_right_column = 0
        base_number_right_column = 0

        high_number_row = 0
        base_number_row = 0

        #Counting high and base numbers in the current cell's row
        for i in range(column_number):
            if layout[row][i] == 'H':
                high_number_row += 1
            if layout[row][i] == 'B':
                base_number_row += 1

        #Initializing counts for high and base numbers in different positions
        high_number_column = 0
        base_number_column = 0

        #Counting high and base numbers in the current cell's column and the right column
        for i in range(row_number):
            if layout[i][column] == 'H':
                high_number_column += 1

            if layout[i][column+1] == "H":
                high_number_right_column += 1

            if layout[i][column+1] == "B":
                base_number_right_column += 1

            if layout[i][column] == 'B':
                base_number_column += 1

        #Counting base and high numbers on the right side of the cell
        right_tile_base_number = 0
        right_tile_high_number = 0
        for i in layout[row][column:]:
            if i == "B" :
                right_tile_base_number += 1
            if i == "H":
                right_tile_high_number += 1
    
        #Checking if the constraints are satisfied for placing neutral tile in the given position
        if  row_number - row-1 >= (column_base - base_number_column)*2-1 and \
            row_number - row-1 >= (column_base_right - base_number_right_column)*2-1 and \
            row_number - row-1 >= (column_high - high_number_column)*2-1 and \
            row_number - row-1 >= (column_high_right - high_number_right_column)*2-1  and \
            column_number - column - 2 -(right_tile_high_number)*2>= (row_high - high_number_row)*2-1  and \
            column_number- column - 2-(right_tile_base_number)*2>= (row_base- base_number_row)*2-1 :
            return True


#Getting positions and types of tiles in the layout
def getting_cells(layout):
    
    cells = []
    for i in range(len(layout)):
        for j in range(len(layout[0])):
            if layout[i][j] == "L" or layout[i][j] == "U":
                cells.append([i ,j, layout[i][j]])

    return cells


#Places the tiles on the given layout based on the constraints
def place(layout, constraints, row_number, column_number, cells, tiles_left):

    #Base case: If all tiles are placed, return True
    if tiles_left == 0:
        return True

    #Getting information about the current cell to be filled
    cells_element = cells[-tiles_left]
    row = cells_element[0]
    column = cells_element[1]
    cell_type = cells_element[2]
    
    #For filling vertical type cells
    if cell_type == "U":

        #Checking if tile is empty
        if layout[row][column] == "U":

            #Checking constraints and neighbors for high tile
            if check_high(layout, constraints, column, row, row_number, column_number) and \
                check_neighbours(layout, column, row, row_number, column_number, "H"):
                #Checking constraints and neighbors for base tile
                if check_base(layout, constraints, column, row+1, row_number, column_number) and \
                    check_neighbours(layout, column, row+1, row_number, column_number, "B"):

                    #Place "HB" tile
                    layout[row][column] = "H"
                    layout[row+1][column] = "B"
                    tiles_left -= 1 #Moving to the next tile
                    if tiles_left == 0:
                        return True
                    
                    #Recursive call for the next tile
                    if place(layout, constraints, row_number, column_number, cells, tiles_left):
                        return True
                    
                    else: #Backtracking if placement fails
                        tiles_left += 1
                        return place(layout, constraints, row_number, column_number, cells, tiles_left)
        
        #Checking if tile is empty or filled with "HB" type tile
        if layout[row][column] == "U" or layout[row][column] == "H":   

            #Empty tile for the case it is filled
            layout[row][column] = "U"
            layout[row+1][column] = "D"  

            #Checking constraints and neighbors for base tile
            if check_base(layout, constraints, column, row, row_number, column_number) and \
                check_neighbours(layout, column, row, row_number, column_number, "B"):
                #Checking constraints and neighbors for high tile
                if check_high(layout, constraints, column, row+1, row_number, column_number) and \
                    check_neighbours(layout, column, row+1, row_number, column_number, "H"):

                    #Place "BH" tile
                    layout[row][column] = "B"
                    layout[row+1][column] = "H"
                    tiles_left -= 1 #Moving to the next tile
                    if tiles_left == 0:
                        return True
                    
                    #Recursive call for the next tile
                    if place(layout, constraints, row_number, column_number, cells, tiles_left):
                        return True
                    
                    else: #Backtracking if placement fails
                        tiles_left += 1
                        return place(layout, constraints, row_number, column_number, cells, tiles_left)
                    
        #Checking if tile is empty or filled with "HB" or "BH" type tile 
        if layout[row][column] == "U" or layout[row][column] == "H" or layout[row][column] == "B":   

            #Empty tile for the case it is filled
            layout[row][column] = "U"
            layout[row+1][column] = "D"     

            #Checking if "NN" type tile placement is valid
            if check_for_n(layout, constraints, column, row,row_number,column_number,cells_element):
                    
                    #Place "NN" tile
                    layout[row][column] = "N"
                    layout[row+1][column] = "N"
                    tiles_left -= 1 #Moving to the next tile
                    if tiles_left == 0:
                        return True
                    
                    #Recursive call for the next tile
                    if place(layout, constraints, row_number, column_number, cells, tiles_left):
                        return True
                    
                    else: #Backtracking if placement fails
                        tiles_left += 1
                        #Empty previously placed "NN" type tiles
                        while tiles_left != len(cells) and layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] == "N":
                            if cells[-(tiles_left+1)][2] == "L":
                                layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] = "L"
                                layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]+1] = "R"
                            elif cells[-(tiles_left+1)][2] == "U":
                                layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] = "U"
                                layout[cells[-(tiles_left+1)][0]+1][cells[-(tiles_left+1)][1]] = "D"
                            tiles_left += 1

                        tiles_left += 1

                        #Empty current tile
                        layout[row][column] = "U"
                        layout[row+1][column] = "D"
                        if tiles_left>len(cells):
                            return False
                        return place(layout, constraints, row_number, column_number, cells, tiles_left)

            else: #Backtracking if placement fails
                #Empty previously placed "NN" type tiles
                while tiles_left != len(cells) and layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] == "N":
                    if cells[-(tiles_left+1)][2] == "L":
                        layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] = "L"
                        layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]+1] = "R"
                    elif cells[-(tiles_left+1)][2] == "U":
                        layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] = "U"
                        layout[cells[-(tiles_left+1)][0]+1][cells[-(tiles_left+1)][1]] = "D"
                    tiles_left += 1

                tiles_left += 1
                #Empty current tile
                layout[row][column] = "U"
                layout[row+1][column] = "D"
                if tiles_left>len(cells):
                    return False
                return place(layout, constraints, row_number, column_number, cells, tiles_left)


    #For filling horizontal type cells
    elif cell_type == "L":
        
        #Checking if tile is empty 
        if layout[row][column] == "L":

            #Checking constraints and neighbors for high tile
            if check_high(layout, constraints, column, row, row_number, column_number) and \
                check_neighbours(layout, column, row, row_number, column_number, "H"):
                #Checking constraints and neighbors for base tile
                if check_base(layout, constraints, column+1, row, row_number, column_number) and \
                    check_neighbours(layout, column+1, row, row_number, column_number, "B"):

                    #Place "HB" tile
                    layout[row][column] = "H"
                    layout[row][column+1] = "B"
                    tiles_left -= 1 #Moving to the next tile
                    if tiles_left == 0:
                        return True
                    
                    #Recursive call for the next tile
                    if place(layout, constraints, row_number, column_number, cells, tiles_left):
                        return True
                    
                    else: #Backtracking if placement fails
                        tiles_left += 1
                        return place(layout, constraints, row_number, column_number, cells, tiles_left)
                        
        #Checking if tile is empty or filled with "HB" type tile
        if layout[row][column] == "L" or layout[row][column] == "H":  

            #Empty tile for the case it is filled
            layout[row][column] = "L"
            layout[row][column+1] = "R"

            #Checking constraints and neighbors for base tile
            if check_base(layout, constraints, column, row, row_number, column_number) and \
                check_neighbours(layout, column, row, row_number, column_number, "B"):
                #Checking constraints and neighbors for high tile
                if check_high(layout, constraints, column+1, row, row_number, column_number) and \
                    check_neighbours(layout, column+1, row, row_number, column_number, "H"):

                    #Place "BH" tile
                    layout[row][column] = "B"
                    layout[row][column+1] = "H"
                    tiles_left -= 1 #Moving to the next tile
                    if tiles_left == 0:
                        return True

                    #Recursive call for the next tile
                    if place(layout, constraints, row_number, column_number, cells, tiles_left):
                        return True

                    else: #Backtracking if placement fails
                        tiles_left += 1
                        return place(layout, constraints, row_number, column_number, cells, tiles_left)
                        
        #Checking if tile is empty or filled with "HB" or "BH" type tile
        if layout[row][column] == "L" or layout[row][column] == "H" or layout[row][column] == "B":   

            #Empty tile for the case it is filled
            layout[row][column] = "L"
            layout[row][column+1] = "R"
            if check_for_n(layout, constraints, column, row,row_number,column_number,cells_element):
                    
                    #Place "NN" tile
                    layout[row][column] = "N"
                    layout[row][column+1] = "N"
                    tiles_left -= 1 #Moving to the next tile
                    if tiles_left == 0:
                        return True
                    
                    #Recursive call for the next tile
                    if place(layout, constraints, row_number, column_number, cells, tiles_left):
                        return True
                    
                    else: #Backtracking if placement fails
                        tiles_left += 1
                        #Empty previously placed "NN" type tiles
                        while tiles_left != len(cells) and layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] == "N":
                            if cells[-(tiles_left+1)][2] == "L":
                                layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] = "L"
                                layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]+1] = "R"
                            elif cells[-(tiles_left+1)][2] == "U":
                                layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] = "U"
                                layout[cells[-(tiles_left+1)][0]+1][cells[-(tiles_left+1)][1]] = "D"
                            tiles_left += 1
                                
                        tiles_left += 1
                        #Empty current tile
                        layout[row][column] = "L"
                        layout[row][column+1] = "R" 
                        if tiles_left>len(cells):
                            return False
                        return place(layout, constraints, row_number, column_number, cells, tiles_left)                       
        
            else: #Backtracking if placement fails
                #Empty previously placed "NN" type tiles
                while tiles_left != len(cells) and layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] == "N":
                    if cells[-(tiles_left+1)][2] == "L":
                        layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] = "L"
                        layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]+1] = "R"
                    elif cells[-(tiles_left+1)][2] == "U":
                        layout[cells[-(tiles_left+1)][0]][cells[-(tiles_left+1)][1]] = "U"
                        layout[cells[-(tiles_left+1)][0]+1][cells[-(tiles_left+1)][1]] = "D"
                    
                    tiles_left += 1

                tiles_left += 1
                if tiles_left>len(cells): 
                    return False
                #Empty current tile
                layout[row][column] = "L"
                layout[row][column+1] = "R"
                return place(layout, constraints, row_number, column_number, cells, tiles_left)

    return False

##Printing layout with removing brackets
def printing_board(board):
    for i in board:
        print(" ".join(i))

def main():

    game_in = sys.argv[1]  #Getting the input game file from the command line arguments
    game = (open(game_in, "r")).read() #Reading the game configuration from the file
    board = game.split("\n")  ##Splitting the input line by line
    #Splitting the input into constraints and layout
    constraints = board[:4]
    for i in range(len(constraints)):
        constraints[i] = constraints[i].split(" ")
    layout = board[4:]
    for i in range(len(layout)): 
        layout[i] = layout[i].split(" ")

    #Getting the dimensions of the board
    column_number = len(layout[0])
    row_number = len(layout)

    #Geting the positions and types of tiles in the layout
    cells = getting_cells(layout)
    #Getting the number of tiles to be placed
    tiles_left = len(cells)

    try:
        #Attempting to place the tiles on the board
        place(layout, constraints, row_number, column_number, cells, tiles_left)
        printing_board(layout) #Printing the resulting layout
    except:
        print("No solution!") #Print a message if no solution is found

if __name__ == "__main__":

    main() #Executing the main function when the script is run

   
         

 
