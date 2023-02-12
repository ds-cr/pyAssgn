import time

class Board_solver:
    
    search_value = 'O'
    flag_value = 'A'
    turn_into_value = 'X'

    def __init__(self):
        self.board = []

    # searchArray : This array consists the indexes (list of tuples) of those Os which are at the border rows or columns
    #               or are connected to Os which are on the border. Basically the Os in this list are connected to border somehow.

    # This function goes through the searchArray and does two things
    # 1) Changes that value from search_value to flag_value 
    # 2) Searches its neigbours to see if any of them also has the search_value and add it to the searchArray 
    # Inputs - total rows and columns, the board itself and the array for bfs search
    def __add_neighbour_O_to_searchArray_and_mark_them(self, rows, cols, board, searchArray):
        for val in searchArray:

            # Step1-Mark Value
            board[val[0]][val[1]] = self.flag_value

            # Step2
            # Searching through neighbours
            # comb -> combinations(left, right, bottom, top)
            for comb in [(-1,0),(1,0),(0,1),(0,-1)]:
                if val[0] + comb[0] >= 0 and val[0] + comb[0] < rows and val[1] + comb[1] >= 0 and val[1] + comb[1] < cols and \
                board[val[0]+comb[0]][val[1]+comb[1]] == self.search_value:
                    searchArray.append((val[0]+comb[0],val[1]+comb[1]))

    # This is the public function that is called to solve the board
    def convert_surrounded_O_to_X(self):
        rows = len(self.board)
        if rows == 0 :
            return
        cols = len(self.board[0])
        searchArray = []

        # Go through the columns and add any index that has value equal to search_value to searchArray
        for val in range(cols):
            if self.board[0][val] == self.search_value:
                searchArray.append((0,val))
            if self.board[rows-1][val] == self.search_value:
                searchArray.append((rows-1,val))
        
        # Go through the rows and add any index that has value equal to search_value to searchArray
        for val in range(rows):
            if self.board[val][0] == self.search_value:
                searchArray.append((val,0))
            if self.board[val][cols-1] == self.search_value:
                searchArray.append((val, cols-1))
    
        self.__add_neighbour_O_to_searchArray_and_mark_them(rows, cols, self.board, searchArray)
        
        # Finally change all the flag_values to search_values and any search_value to turn_into_value
        for row in range(rows):
            for col in range(cols):
                if self.board[row][col] == self.search_value:
                    self.board[row][col] = self.turn_into_value
                elif self.board[row][col] == self.flag_value:
                    self.board[row][col] = self.search_value

    # Taking input
    # Used iter to get input which will allow input until empty string is passed as input string (press ENTER twice)
    # Split each input string on spaces and append the value to board
    def get_input(self):
        self.board = []
        row_len = 0
        for row in iter(input, ""):
            print(row)
            char_lst = row.split()
            
            # Test to see if row is made up of only required values
            if not all(c in [self.search_value, self.turn_into_value] for c in char_lst):
                raise Exception("Unexpected value found!")
            row_len = (row_len or len(char_lst))
            
            # Test to see if row lengths are same
            if row_len != len(char_lst):
                raise Exception("Row lengths not equal")
            
            self.board.append(char_lst)
        # Test to see if column length same as row length
        if len(self.board) != row_len:
            raise Exception("Column length not same as row length")
    
    # Print the board
    def print_board(self):
        print("Solved Board")
        for row in self.board:
            for val in row:
                print(val, end = " ")
            print()

    # Getter function
    def get_board(self):
        return self.board