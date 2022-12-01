import csv

#save values into calories.csv and read by row ...
with open('calories.csv') as csvfile:
    readings = csv.reader(csvfile)

    #initialise variables
    elf = 0                     #current elf
    max = 0                     #current max calories
    current_calories = 0        #current row value
    array = []                  #set up array for part 2

    for row in readings:
        if len(row) == 0:       #empty row
            array.append(elf)   #append current elf value to array
            if elf > max:       #is current elf calories > max calories?
                max = elf       #if so this elf is the new max
            elf = 0             #reset count for next elf
        else:
            current_calories = int(row[0])  #get value from row.  Cast to int
            elf += current_calories         #add to current elf

    ##### Part 1:

    #is last elf the max?
    if elf > max:
        max = elf
    #showtime
    print("Max elf calories is: ", max)

    ##### Part 2
    array.sort()            #sort array in ascending order
    index = len(array)      #get array length

    #get last 3 values (1st element is zero, so last index is len-1)
    total = array[index-1] + array[index-2] + array[index-3]

    #showtime
    print("Combined top 3 elves: ", total)
