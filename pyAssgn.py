class Solution:        
    def callBFS(self, i, j, rows, cols, board, searchArray):
        for val in searchArray:
            for comb in [(-1,0),(1,0),(0,1),(0,-1)]:
                if val[0] + comb[0] >= 0 and val[0] + comb[0] < rows and val[1] + comb[1] >= 0 and val[1] + comb[1] < cols and board[val[0]+comb[0]][val[1]+comb[1]] == 'O':
                    board[val[0]+comb[0]][val[1]+comb[1]] = 'P'
                    searchArray.append((val[0]+comb[0],val[1]+comb[1]))

    def solve(self, board):
        rows = len(board)
        cols = len(board[0])
        searchArray = []

        for val in range(cols):
            if board[0][val] == 'O':
                board[0][val] = 'P'
                searchArray.append((0,val))
                self.callBFS(0, val, rows, cols, board, searchArray)
            if board[rows-1][val] == 'O':
                board[rows-1][val] = 'P'
                searchArray.append((rows-1,val))
                self.callBFS(rows-1, val, rows, cols, board, searchArray)
        
        for val in range(rows):
            if board[val][0] == 'O':
                board[val][0] = 'P'
                searchArray.append((val,0))
                self.callBFS(val, 0, rows, cols, board, searchArray)
            if board[val][cols-1] == 'O':
                board[val][cols-1] = 'P'
                searchArray.append((val, cols-1))
                self.callBFS(val, cols-1, rows, cols, board, searchArray)

        for row in range(0,rows):
            for col in range(0,cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'P':
                    board[row][col] = 'O'

arr = []
for row in iter(input, ""):
    arr.append(row.split())

obj = Solution()
obj.solve(arr)

for row in arr:
    for val in row:
        print(val, end = " ")
    print()