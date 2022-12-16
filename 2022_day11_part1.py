
index = 0

#lists for each variable
monkey_items   = []
monkey_action  = []
monkey_value   = []
monkey_divisor = []
monkey_true    = []
monkey_false   = []
monkey_inspected = []

alltime = []

for i in range(0, 8):
	monkey_inspected.append(0)

print(monkey_inspected)


#setup lists for each variable

with open('2022_day11_input.txt') as infile:
	lines = infile.readlines()

	count = 0
	for line in lines:

		#set up monkey data

		#each monkey has 6 lines plus a blank line
		count += 1 

		#remove colons
		line = line.replace(':', '')
		
		#Get monkey number
		if count == 1:
			monkey = int(line.split()[1])

		#get items and add to list.  Then append to monkey list
		if count == 2:

			#start from numbers: "Starting items: 79, 98"
			i = 2

			valid = True
			###

			items = []

			while valid == True:
				try:
					item = int(line.split()[i].replace(',', ''))
					items.append(item)
				except:
					valid = False
					break
				i += 1
			
			monkey_items.append(items)

		#operation.  Need split 4 and 5 "Operation: new = old * 19"
		if count == 3:
			action = line.split()[4]
			monkey_action.append(action)
			value  = line.split()[5]
			monkey_value.append(value)

		#Test: find number divisible by in element 3
		if count == 4:
			divisor = int(line.split()[3])
			monkey_divisor.append(divisor)
			

		#monkey to throw to if true: "If true: throw to monkey 2"
		if count == 5:
			true_monkey = int(line.split()[5])
			monkey_true.append(true_monkey)

		#monkey to throw to if false: If false: throw to monkey 3
		if count == 6:
			false_monkey = int(line.split()[5])	
			monkey_false.append(false_monkey)


		#next monkey
		if count == 7:
			count = 0

	index += 1

	#process items according to rules

	# i is current monkey

	round = 0
	while round <= 19:

		round += 1

		for i in range(0, len(monkey_items)): 

			action  = monkey_action[i]
			value   = monkey_value[i]
			divisor = int(monkey_divisor[i])
			true    = int(monkey_true[i])
			false   = int(monkey_false[i])


			#get current items in list for this monkey
			item_length = len(monkey_items[i])
			for j in range(0, len(monkey_items[i])):

				worry = int(monkey_items[i][j])

				#action
				if value == 'old':
					factor = int(worry)
				else:
					factor = int(value)

				if action == '*':
					worry *= factor

				if action == '+':
					worry += factor


				#divisor: determine true or false
				temp = worry
				worry = int(temp/3)

				if worry % divisor == 0:
					receiver = true
				else:
					receiver = false 

				#add 1 to throwing monkey
				monkey_inspected[i] += 1

				#add new worry level to receiving monkey:
				monkey_items[receiver].append(worry)

			#remove original items from original monkey (all been thrown)
			for j in range(0, len(monkey_items[i])):
				del monkey_items[i][0]

			#print(i, monkey_items)



print(monkey_inspected)
sorted_monkeys = sorted(monkey_inspected)
print(sorted_monkeys[-1] * sorted_monkeys[-2])


