"""Suppose that you are given an n x n checkerboard and a checker.
You must move the checker from the bottom edge of the board to the top edge of the board
according to the following rule. At each step you may move the checker to one of three
squares:
1. the square immediately above,
2. the square that is one up and one to the left (but only if the checker is not already in the
left-most column),
3. the square that is one up and one to the right (but only if the checker is not already in
the right-most column).
Each time you move from square x to square y, you receive p(x,y) dollars. You are given
p(x,y) for all pairs (x,y) for which a move from x to y is legal. Do not assume that p(x,y) is
positive.
Give an algorithm that figures out the set of moves that will move the checker from
somewhere along the bottom edge to somewhere along the top edge while gathering as
many dollars as possible. Your algorithm is free to pick any square along the bottom edge as
a starting point and any square along the top edge as a destination in order to maximize the
number of dollars gathered along the way. What is the running time of your algorithm?"""

from random import randint

def generate_board(n_rows=8, n_cols=0, value_range=(-100, 100)):
	if not n_cols: n_cols = n_rows
	return [[randint(*value_range) for _ in range(n_cols)] for _ in range(n_rows)]


def print_board(board):
	line = len(board)*7*'-'
	matrix = [[' '] + list(range(len(board)))] + [[i]+row for i, row in enumerate(board)]
	print('\n'+f'\n{line}\n'.join([''.join(['|{:4} '.format(cell) for cell in row]) for row in matrix]))


def checker_max_path(board):
	if not board:
		return None

	n_rows = len(board)
	n_cols = len(board[0])
	b = [[float("-inf")]*(n_cols+2) for _ in range(n_rows+1)]
	b[1][1:-1] = board[0]

	for i in range(1, n_rows):
		for j in range(n_cols):
			b[i+1][j+1] = board[i][j] + max(b[i][j], b[i][j+1], b[i][j+2])

	return max(b[-1]), _get_max_path(b, n_cols)

def _get_max_path(table, n_cols):
	path = []
	left, right = 1, n_cols+2
	for i in range(len(table)-1, 0, -1):
		row = table[i]
		max_value = max(row[left:right])
		max_index = row.index(max_value)
		path.append((i-1, max_index-1))
		left = max_index-1
		right = max_index+2
	return path[::-1]



# Tests
game = generate_board()
print_board(game)
max_sum, path = checker_max_path(game)
print(f"\nThe max possible result for this board is: ${max_sum}")
print(f"The optimal (most lucrative) path is: {path}")
