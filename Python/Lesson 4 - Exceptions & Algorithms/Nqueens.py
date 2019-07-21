# demo code for placing queens on a chess board
# uses backtracking

def canPlace(row):
	if (row==N):
		return True
	for i in range(N):
		#inDanger checks previous columns and diagonals
		if not inDanger(row,i):
			#This seems good - put the queen in place
			board[row][i] = 'Q'
			if not canPlace(row+1):
				#Not a good place after all, take her out
				board[row][i] = '.'
			else:
				#A solution was found - quit
				return True
	# None of those worked
	return False

def inDanger(r,c):
	#Check the columns
	for i in range(1,r+1):
		if board[r-i][c] == 'Q':
			return True
	#Check leading diagonal
	for i in range(1,min(r,c)+1):
		if board[r-i][c-i] == 'Q':
			return True
	#Check trailing diagonal
	for i in range(1,min(r,N-c-1)+1):
		if board[r-i][c+i] == 'Q':
			return True
	return False

def printBoard(board):
  for i in range(len(board)):
      print(''.join(board[i]))

# testing
N = 4
board = [['.' for i in range(N)] for i in range(N)]
if canPlace(0):
	printBoard(board)