with open('2022_day10_input.txt') as infile:
	lines = infile.readlines()

	# x is register.  Starts at 1

	x = 1
	cycle = 1
	qty = 0
	strength = 0

	for line in lines:

		inst = str(line.split()[0])

		if inst == 'addx':
			qty  = int(line.split()[1])
			cycle += 1


			if cycle in (20, 60, 100, 140, 180, 220):
				print("cycle:", cycle, "x:", x, "strength:", cycle*x)
				strength += (cycle * x)

			cycle +=1
			x += qty

		else:
			cycle += 1


		if cycle in (20, 60, 100, 140, 180, 220):
			print("cycle:", cycle, "x:", x, "strength:", cycle*x)
			strength += (cycle * x)

	print("signal strength:", strength)




				





			
