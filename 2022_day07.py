with open('2022_day07_input.txt') as infile:
    lines = infile.readlines()

    #dirs: dictionary of all directories and current size
    dirs = {}
    dirs['/'] = 0

    cwd = str('')
    parm = ''
    cmd  = ''

    #stack is where we are as we move through the directory structure ...
    stack = []

    # iterate through each line ...
    for line in lines:
        list = line.split()

        # command
        if list[0] == "$":

            if len(list) > 2:
                cmd  = list[1]
                parm = list[2]
            
                #if commans is "cd" get where we're going to and maintain current position in stack
                if cmd == 'cd':

                    #root
                    if parm == '/':
                        cwd = '/'
                        stack = []
                        stack.append('/')

                    #go back one level
                    elif parm == '..':
                        del stack[-1]
                        cwd = stack[-1]

                    #parm is directory.  If not in dictionary then add it
                    else:
                        if cwd == '/':
                            cwd += parm 
                        else:
                            cwd = cwd + '/' + parm

                        if cwd not in dirs:
                            dirs[cwd] = 0

                        stack.append(cwd)

        
        else:
            #if file it has a size.  Add this to current dir value in vars
            #last entry is stack is current directory
            if list[0] != 'dir':
                if list[0].isdigit:
                    this_size = int(list[0])
                    pos = stack[-1]

                    for key, value in dirs.items():

                        #update all directories in path (it states that indirect files should be included in total)
                        if key in pos:
                            
                            cwd = stack[-1]
                            current_value = dirs[key]
                            new_value = current_value + this_size
                            dirs[key] = new_value


total = 0
for key, value in dirs.items():
    if value < 100000:
        total += value

print(dirs)     #print array of all directories (not needed, just to see extent)
print(total)    #showtime!

#
#part 2 .....
#

print(" ")
print("Part 2")

total_disk = int(70000000)
required   = int(30000000)

used       = dirs['/'] 
unused     = total_disk - used
needed     = required - unused

print("used:", used)
print("unused:", unused)
print("we need:", needed)

current_lowest = required
directory = ''

#cycle through array and find lowest value > min needed
for key, value in dirs.items():
    if value >= needed:
        if value < current_lowest:
            current_lowest = value 
            directory = key 

#showtime ...
print("directory:", directory, "size:", current_lowest)















   

