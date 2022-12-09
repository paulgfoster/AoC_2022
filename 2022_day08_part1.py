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

#total of trees on outside of square
outside = (columns * 2) + ((rows - 2) * 2)

count = 0


#get the inner trees by row
for i in range(1, matrix_size-1):
	row = matrix[i]

	current_row = i

	#get each inner tree in row
	for j in range(1, columns-1):

		current_tree   = int(matrix[i][j])
		current_column = j + 1


		#we have our row and column.  See if this is the biggest number of trees to left, to right, above or below 


		#current row from left
		visible = False
		this_max = 0
		for x in range(0, current_column-1):
			
			if int(row[x]) > this_max:
				this_max = int(row[x])

		if current_tree > this_max:
			visible = True
			#print("LEFT", "max:", this_max, "tree:", int(row[x]))

		#current row: from right
		if visible == False:
			this_max = 0
			for x in range(current_column, columns):

				if int(row[x]) > this_max:
					this_max = int(row[x])

			if current_tree > this_max:
				visible = True
				#print("RIGHT", "row:", current_row, "max:", this_max, "tree:", int(row[x]), "current_tree", current_tree , "current_column", current_column )

				
		#find in current column:

		# -1 because of index starting at 0
		current_column -= 1

		#current column: from top

		if visible == False:
			this_max = 0
			for x in range(0, current_row):

				if int(matrix[x][current_column]) > this_max:
					this_max = int(matrix[x][current_column])

			if current_tree > this_max:
				visible = True


		#current column: from bottom
		if visible == False:
			this_max = 0
			for x in range(current_row +1, matrix_size):

				if int(matrix[x][current_column]) > this_max:
					this_max = int(matrix[x][current_column])

			if current_tree > this_max:
				visible = True


	
		if visible == True:
			count += 1


total = outside + count
	
print()
print("outside:", outside, "inside", count, "total", total)


	



