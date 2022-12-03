
with open('day03_rucksack.txt') as infile:
    lines = infile.readlines()
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    total = 0
    count = 0

    rucksack1 = ' '
    rucksack2 = ' '
    rucksack3 = ' '

    # read all the file ...
    for line in lines:

        count += 1

        #batches of 3.  When count = 4 it's first of next batch
        if count == 4:
            count = 1
            rucksack1 = ' '
            rucksack2 = ' '
            rucksack3 = ' '

        contents = line.strip()

        #batches of 3 ... get contents of each rucksack in the batch
        if count == 1:
            rucksack1 = contents
        elif count == 2:
            rucksack2 = contents
        elif count == 3:
            rucksack3 = contents

        #once rucksack3 has a value we can check for common letter in each rucksack
        if rucksack3 > ' ':

            #cycle through each letter for rucksack1
            for letter in rucksack1:

                # ...and check if it exists in other rucksacks
                if letter in rucksack2 and letter in rucksack3:

                    #success ... lookup the value in the array and add it to the total
                    value = letters.index(letter) + 1  #array starts at 0!  Remember to add one
                    total += value
                    break

    #showtime
    print(total)
