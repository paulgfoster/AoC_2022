with open('2022_day10_input.txt') as infile:
	lines = infile.readlines()

	# x is register.  Starts at 1
	x = 1
	cycle = 0
	qty = 0
	pos = 0

	crt_row = 0

	crt  = ''
	crt1 = ''
	crt2 = ''
	crt3 = ''
	crt4 = ''
	crt5 = ''
	crt6 = ''


	# write each char here. if within "x" write #, otherwise a space
	# (space makes it easier to read)
	#---------------------------------------------------------
	def write_line(crt):
		global pos, x

		if (pos == x) or (pos == x-1) or (pos == x+1):
			crt += '#'
		else:
			crt += ' '
		return crt

	# each CRT row is crt1, crt2 etc. Start next row here
	#----------------------------------------------------------
	def update_crt(): 

		global cycle, crt, crt1, crt2, crt3, crt4, crt5, crt6, crt_row

		crt_row += 1

		if crt_row == 1:
			crt1 = crt
		if crt_row == 2:
			crt2 = crt
		if crt_row == 3:
			crt3 = crt
		if crt_row == 4:
			crt4 = crt
		if crt_row == 5:
			crt5 = crt
		if crt_row == 6:
			crt6 = crt

		crt = ''

		cycle = 1
		return	

	#---------------------------------------------------------


	for line in lines:

		inst = str(line.split()[0])

		if inst == 'addx':
			qty  = int(line.split()[1])

			#start addx
			cycle += 1

			#40 chars per row.  So 41 starts on next row
			if cycle == 41:
				update_crt()

			pos = cycle-1
			crt = write_line(crt)

			#end addx
			cycle += 1

			#40 chars per row.  So 41 starts on next row
			if cycle == 41:
				update_crt()

			pos = cycle-1 #because count starts at zero
			crt = write_line(crt)
			x += qty
			
		else:
			cycle += 1

			#40 chars per row.  So 41 starts on next row
			if cycle == 41:
				update_crt()

			pos = cycle-1 #because count starts at zero
			crt = write_line(crt)
	

crt6 = crt

print()
			
print(crt1) 
print(crt2) 
print(crt3) 
print(crt4) 
print(crt5) 
print(crt6) 

print()
