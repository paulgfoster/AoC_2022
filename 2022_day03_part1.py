
with open('day03_rucksack.txt') as infile:
    lines = infile.readlines()
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    total = 0

    # read all the file ...
    for line in lines:

        contents = line.strip()
        length = len(contents)

        #find where compartment 1 ends and 2 starts
        halfway = int(length/2)

        #split string into 2 compartments
        compartment1 = contents[0: halfway]
        compartment2 = contents[halfway:]

        #cycle through each letter in compartment 1 ...
        for letter in compartment1:

            # ...and check if it exists in compartment
            if letter in compartment2:

                #success ... lookup the value in the array and add it to the total
                value = letters.index(letter) + 1  #array starts at 0!  Remember to add one
                total += value
                break

    #showtime
    print(total)
