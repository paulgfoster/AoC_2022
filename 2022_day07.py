with open('2022_day07_input.txt') as infile:
    lines = infile.readlines()

    dirs = {}
    dirs['/'] = 0

    cwd = str('')
    count = 0
    parm = ''
    cmd  = ''

    #track where we are ...
    stack = []

    # iterate through each line ...
    for line in lines:
        list = line.split()

        count += 1
        # command
        if list[0] == "$":

            if len(list) > 2:
                cmd  = list[1]
                parm = list[2]
            
                #if cd get where we're going to and maintain current position in dirstack
                if cmd == 'cd':
                    if parm == '/':
                        cwd = '/'
                        stack = []
                        stack.append('/')
                    elif parm == '..':
                        del stack[-1]
                        cwd = stack[-1]
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
            if list[0] != 'dir':
                if list[0].isdigit:
                    this_size = int(list[0])
                    pos = stack[-1]

                    for key, value in dirs.items():

                        if key in pos:
                            
                            cwd = stack[-1]
                            current_value = dirs[key]
                            new_value = current_value + this_size
                            dirs[key] = new_value


total = 0
for key, value in dirs.items():
    if value < 100000:
        total += value

print(dirs)
print(total)

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

for key, value in dirs.items():
    if value >= needed:
        if value < current_lowest:
            current_lowest = value 
            directory = key 

print("directory:", directory, "size:", current_lowest)















   

