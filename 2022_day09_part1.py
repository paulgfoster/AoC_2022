
#set up arbitrary start point (only for ease of testing)

hr = 100 #head row 
hc = 100 #head col

tr = 100 #tail row
tc = 100 #tail col

#array of where tail has been
visited = []
visited.append('100,100')



with open('2022_day09_input.txt') as infile:
	lines = infile.readlines()

	for line in lines:
		dirn = str(line.split()[0])
		qty  = int(line.split()[1])

		i = 0

		#move rope one square at a time.  
		while i < qty:
			i += 1

			if dirn == 'R':
				hc += 1 

				#only move tail if within 1 square of head
				if abs(hr - tr ) > 1 or abs(hc - tc) > 1:
					tc = hc - 1
					tr = hr
					
					square = str(hr) + ',' + str(tc)
					if square not in visited:
						visited.append(square)


			if dirn == 'L':
				hc -= 1 

				#only move tail if within 1 square of head
				if abs(hr - tr ) > 1 or abs(hc - tc) > 1:
					tc = hc + 1
					tr = hr
					
					square = str(hr) + ',' + str(tc)
					if square not in visited:
						visited.append(square)


			if dirn == 'D':
				hr += 1

				#only move tail if within 1 square of head
				if abs(hr - tr ) > 1 or abs(hc - tc) > 1:
					tr = hr - 1
					tc = hc
					
					square = str(tr) + ',' + str(hc)
					if square not in visited:
						visited.append(square)


			if dirn == 'U':
				hr -= 1

				#only move tail if within 1 square of head
				if abs(hr - tr ) > 1 or abs(hc - tc) > 1:
					tr = hr + 1
					tc = hc
					
					square = str(tr) + ',' + str(hc)
					if square not in visited:
						visited.append(square)


#showtime and pray
print(len(visited))