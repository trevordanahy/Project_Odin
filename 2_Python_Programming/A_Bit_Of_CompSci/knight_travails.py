# Traveling Knight Problem
# Odin Project Challenge, https://www.theodinproject.com/courses/ruby-programming/lessons/data-structures-and-algorithms

#Create a list of algebraic notation on chess board
rows = [r for r in range(8, 0 ,-1)]
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
algebraic_board = [str(r)+c for r in rows for c in columns]

'''#A chess board is 8x8 grid, but to prevent off board movemnts by 
the knight use a 12x12 grid.  For ease of movement and 
evaluation create a list with each gridsquare numbered
starting in the top left, 1-144'''

#Using 12x12 grid(1-144)create a list of the valid 8x8 chess board postions
valid_postions = [num for num in range(27,119) if num %12 > 2 and num %12 < 11]

#Map our Algebraic board to our position board.
board_map = {valid_postions[i] : algebraic_board[i] for i in range(len(valid_postions))}

#Possible moves for Knight
knight_moves = (-25, -23, -14, -10, 10, 14, 23,25)



def valid_move(move):
	if move in valid_postions:
		return True
	else:
		return False

def move_knight(position):
	possible_moves = []
	for move in knight_moves:
		new_pos = position + move
		if valid_move(new_pos):
			possible_moves.append(new_pos)
	return possible_moves


def find_path(start, end):
	if start == end:
		print("You are already there, stop wasting my time.")
		return
	else:
		num_moves = {start:0}
		previous_move  = {start: None}
		move_count = 1
		starts = [start]
		squares_visited = set()

		
		while end not in squares_visited:
			next_moves = []
			for start in starts:
				new_moves = move_knight(start)
				for move in new_moves:
					if move not in squares_visited:
						num_moves[move] = move_count
						previous_move[move] = start
						next_moves.append(move)
						squares_visited.add(move)
			starts = next_moves
			move_count += 1

	return num_moves[end]


def convert_pos2_algebraic(position):
	return board_map[position]

def convert_algebraic2_pos(position):
	idx = algebraic_board.index(position)
	return valid_postions[idx]



print("I can tell you how many moves it takes to move a knight from 1 postion on a chess board to another.")

start = input("Give me a starting postion in algebraic notation ")
while start not in algebraic_board:
	print('That is not algebraic notation, an example would be 8a.')
	start = input('Try again ')

end = input("Where do you want to end?, again in algebraic notation ")
while end not in algebraic_board:
	print('That is not algebraic notation, an example would be 8a')
	end = input('Try again ')


start_pos = convert_algebraic2_pos(start)
end_pos = convert_algebraic2_pos(end)


print(find_path(start_pos,end_pos))










































'''
def valid_move(moved_position, movement_list,new_starts={}):
	if moved_position in valid_postions:
		movement_list.append(moved_position)
		new_starts.add(moved_position)
	else:
		return

def move_tree(start_positions, end):
	visited = set()
	next_start = set()

	for num in start_positions:
		movements = []
		for move in knight_moves:
			valid_move(num+move, movements, next_start)
		for pos in movements:
			visited.add(pos)
		if end in visited:
			possible_moves.update({num: movements})
			
	if end in visited:
		print(possible_moves)
	else:
		start_positions.clear()
		print('move')
		for pos in next_start:
			start_positions.append(pos)
		next_start.clear()
		move_tree(start_positions, end)


move_tree(start_positions, 67)



'''
