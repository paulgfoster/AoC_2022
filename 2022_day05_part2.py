import csv

num_lines = sum(1 for line in open('2022_day05_crates.txt'))


with open('2022_day05_crates.txt') as infile:
    lines = infile.readlines()

    stack1 = []
    stack2 = []
    stack3 = []
    stack4 = []
    stack5 = []
    stack6 = []
    stack7 = []
    stack8 = []
    stack9 = []

    linecount = num_lines


    # iterate through each line ...
    for line in reversed(lines):

        #not last line, this is stack numbers
        if linecount != num_lines:

            contents = line.strip('\n')
            length = len(line)

            charcount  = int(0)
            cratecount = int(0)

            i = 0
            start = 1 #starts in col 2
            end   = 3
            pos   = 0
            index = 0

            while True:
     
                if pos > length:
                    break

                if i != 0:
                    start = start + 4
                    end   = end + 4
                    index += 1

                value = contents[start-1: end]  

                if value > '     ':

                    if index == 0:
                        stack1.append(value)
                    elif index == 1:
                        stack2.append(value)
                    elif index == 2:
                        stack3.append(value)
                    elif index == 3:
                        stack4.append(value)
                    elif index == 4:
                        stack5.append(value)
                    elif index == 5:
                        stack6.append(value)
                    elif index == 6:
                        stack7.append(value)
                    elif index == 7:
                        stack8.append(value)
                    elif index == 8:
                        stack9.append(value)

                i += 1
                pos += 4

        linecount -= 1

#we have the arrays of each stack.  Now get the instructions ...

with open('2022_day05_instructions.txt') as csvfile:
    instructions = csv.reader(csvfile, delimiter=' ')

    # function to return qty crates in order ....
    def get_crates(array, qty):

        index = 0

        # get number of elements
        for i in array:
            index += 1

        start = index - qty
        end   = start + qty
        crates = []
        crates = array[start: end]

        return crates


    for row in instructions:

        # get qty, from and to values from row ....
        qty        = int(row[1])
        from_stack = int(row[3])
        to_stack   = int(row[5])

        from_stack_array = []
        crate = ' '


        #get the crate to move ...
        if from_stack == 1:
            from_stack_array = stack1;

        elif from_stack == 2:
            from_stack_array = stack2;

        elif from_stack == 3:
            from_stack_array = stack3;

        elif from_stack == 4:
            from_stack_array = stack4;

        elif from_stack == 5:
            from_stack_array = stack5;

        elif from_stack == 6:
            from_stack_array = stack6;

        elif from_stack == 7:
            from_stack_array = stack7;

        elif from_stack == 8:
            from_stack_array = stack8;

        elif from_stack == 9:
            from_stack_array = stack9;
        
        #get the last crate of current array
        crates = get_crates(from_stack_array, qty)

        #remove from original crate
        while True:

            if qty == 0:
                break

            if from_stack == 1:
                del stack1[-1]

            elif from_stack == 2:
                del stack2[-1]   

            elif from_stack == 3:
                del stack3[-1]

            elif from_stack == 4:
                del stack4[-1]

            elif from_stack == 5:
                del stack5[-1]

            elif from_stack == 6:
                del stack6[-1]

            elif from_stack == 7:
                del stack7[-1]

            elif from_stack == 8:
                del stack8[-1]

            elif from_stack == 9:
                del stack9[-1]

            qty -= 1


        #now add crates to maintain stack order
        if to_stack == 1:
            for i in crates:
                stack1.append(i)

        elif to_stack == 2:
            for i in crates:
                stack2.append(i)

        elif to_stack == 3:
            for i in crates:
                stack3.append(i)

        elif to_stack == 4:
            for i in crates:
                stack4.append(i)

        elif to_stack == 5:
            for i in crates:
                stack5.append(i)

        elif to_stack == 6:
            for i in crates:
                stack6.append(i)

        elif to_stack == 7:
            for i in crates:
                stack7.append(i)

        elif to_stack == 8:
            for i in crates:
                stack8.append(i)

        elif to_stack == 9:
             for i in crates:
                stack9.append(i)       

string =  stack1[len(stack1)-1]
string += stack2[len(stack2)-1]
string += stack3[len(stack3)-1]
string += stack4[len(stack4)-1]
string += stack5[len(stack5)-1]
string += stack6[len(stack6)-1]
string += stack7[len(stack7)-1]
string += stack8[len(stack8)-1]
string += stack9[len(stack9)-1]

string = string.replace('[','')
string = string.replace(']','')

print(string)






