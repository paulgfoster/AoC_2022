#Day 8

#get number of rows (thanks Stackoverflow)
rows = sum(1 for line in open('2022_day08_input.txt'))
columns = 0
outside = 0

trees  = []
matrix = []
    

with open('2022_day08_input.txt') as infile:
    lines = infile.readlines()

    for line in lines:
    	row = str(line.split()[0])
    	if columns == 0:
    		columns = len(row)

    	#build a matrix of each value	
    	for i in range(0, columns):
    		trees.append(row[i])

	    
    	matrix.append(trees)
    	trees = []


matrix_size = len(matrix)
row_size = len(row)

#total of trees on outside of square
outside = (columns * 2) + ((rows - 2) * 2)

count = 0
topscore = 0


#get the inner trees by row
for i in range(1, matrix_size):
	row = matrix[i]

	current_row = i

	#get each inner tree in row
	for j in range(1, columns-1):

		current_tree   = int(matrix[i][j])
		current_column = j

		left = 0
		x = int(current_column - 1)
		while x >= 0:
			if int(matrix[current_row][x]) >= current_tree:
				left = current_column - x
				break
			else:
				x -= 1
				left += 1
		
		right = 0
		x = int(current_column + 1)
		while x <= (row_size-1):
			if int(matrix[current_row][x]) >= current_tree:
				right = x - current_column
				break
			else:
				x += 1
				right += 1


		top = 0
		x = int(current_row - 1)
		while x >= 0:
			if int((matrix[x][current_column])) >= current_tree:
				top = current_row - x 
				break
			else:
				top += 1
				x -= 1

		bottom = 0
		x = int(current_row + 1)
		while x <= matrix_size-1:
			if int((matrix[x][current_column])) >= current_tree:
				bottom = x - current_row
				break
			else:
				bottom += 1
				x += 1

		score = left * right * top * bottom


		if score > topscore:
			topscore  = score 
			topleft   = left 
			topright  = right 
			toptop    = top 
			topbottom = bottom 


print("highest scenic score:", topscore)
print("left:", topleft, "right:", topright, "top:", toptop, "bottom:", topbottom)


