import csv

with open('2022_day04_sections.csv') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')

    #function to get part1...
    def get_duplicate(hyphen_position, min_first_elf, max_first_elf, min_second_elf, max_second_elf):

        found = 0
        count = 0

        #if 1st range is within 2nd range...
        if min_first_elf >= min_second_elf and max_first_elf <= max_second_elf:
            count += 1

            #if equal we could duplicate in next section.  Set found flag on
            found = 1


        #if 2nd range is within 1st range (and not already found in first pass above)...
        if found == 0:
            if min_second_elf >= min_first_elf and max_second_elf <= max_first_elf:
                count += 1

        return count

    #function to get part2...
    def get_overlap(hyphen_position, min_first_elf, max_first_elf, min_second_elf, max_second_elf):

        found = 0
        count = 0

        #if 1st range overlaps with 2nd range...
        if max_first_elf >= min_second_elf and max_first_elf <= max_second_elf:
            count += 1

            #if equal we could duplicate in next section.  Set found flag on
            found = 1


        #if 2nd range overlaps 1st range...
        if found == 0:
           if max_second_elf >= min_first_elf and max_second_elf <= max_first_elf:
                count += 1

        return count


    #
    # End of functions.  Start the engines ...
    #

    count_duplicate = 0
    count_overlap   = 0

    #read each line annd get max/min for each pair ....
    for row in lines:

        first_elf = row[0]
        second_elf = row[1]

        #find max and min values for 1st elf: either side of "-"
        hyphen_position = first_elf.index('-')
        min_first_elf   = int(first_elf[0:hyphen_position])
        max_first_elf   = int(first_elf[hyphen_position+1:])

        #find max and min values for 2nd elf: either side of "-"
        hyphen_position = second_elf.index('-')
        min_second_elf  = int(second_elf[0:hyphen_position])
        max_second_elf  = int(second_elf[hyphen_position+1:])


        count_duplicate += get_duplicate(hyphen_position, min_first_elf, max_first_elf, min_second_elf, max_second_elf)
        count_overlap   += get_overlap(hyphen_position, min_first_elf, max_first_elf, min_second_elf, max_second_elf)

    print("fully duplicated: ", count_duplicate)
    print("overlapping: ", count_overlap)
