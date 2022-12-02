import csv

# A X for Rock
# B Y for Paper
# C Z for Scissors

# function to calculate points scored from shape
def calc_shape_score(myplay):

    shape_score = 0;
    if myplay == 'X':
        shape_score = 1
    elif myplay == 'Y':
        shape_score = 2
    elif myplay == 'Z':
        shape_score = 3
    else:
        shape_score = 0

    return shape_score

#function to calculate result of play
#lost=0, draw=3, win=6
def get_result(oppenent, myplay):
    points = 0
    if opponent == 'A':
        if myplay == 'X':
            points = 3
        elif myplay == 'Y':
            points = 6;
        else:
            points = 0;

    elif oppenent == 'B':
        if myplay == 'Y':
            points = 3
        elif myplay == 'Z':
            points = 6;
        else:
            points = 0;

    elif oppenent == 'C':
        if myplay == 'Z':
            points = 3
        elif myplay == 'X':
            points = 6;
        else:
            points = 0;

    else:
        points = 0

    return points

#save values into calories.csv and read by row ...
with open('strategy_day02.csv') as csvfile:
    readings = csv.reader(csvfile)

    print(readings)

    #initialise variables
    opponent = ' '
    myplay = ' '
    points = 0
    shape_score = 0
    total_points = 0

    for row in readings:

        string = row[0]
        opponent = string[0]
        myplay = string[2]

        #Get points for Rock(1), Paper(2), Scissors(3))
        shape_score = calc_shape_score(myplay)

        #Did we win? Find out and score accordingly
        points = get_result(opponent, myplay)

        #accumulate total points as we go along
        total_points += shape_score + points

    #showtime
    print("total points: ",  total_points)
