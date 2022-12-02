import csv


# function to calculate points: win/lose/draw plus points for shape
def calc_my_score(game_result, opponent):

    my_shape = ' '
    points = 0

    #work out what shape I need to get reults set in "game_result"
    #than calculate total point for reult + shape

    #lose ...
    if game_result == 'X':

        points = 0

        #rock beats scissors
        if opponent == 'A':
            my_shape = 'scissors'

        #paper beats rock
        elif opponent == 'B':
            my_shape = 'rock'

        #scissors beats paper
        elif opponent == 'C':
            my_shape = 'paper'

    #draw ...
    elif game_result == 'Y':

        points = 3

        if opponent == 'A':
            my_shape = 'rock'

        elif opponent == 'B':
            my_shape = 'paper'

        elif opponent == 'C':
            my_shape = 'scissors'

    #win
    elif game_result == 'Z':

        points = 6

        #rock loses to paper
        if opponent == 'A':
            my_shape = 'paper'

        #paper loses to scissors
        elif opponent == 'B':
            my_shape = 'scissors'

        #scissors loses to rock
        elif opponent == 'C':
            my_shape = 'rock'

    # rock=1, paper=2, scissors=3
    if my_shape == 'rock':
        points += 1
    elif my_shape == 'paper':
        points += 2
    elif my_shape == 'scissors':
        points += 3

    return points

#save values into calories.csv and read by row ...
with open('strategy_day02.csv') as csvfile:
    readings = csv.reader(csvfile)

    #initialise variables
    opponent = ' '
    calc_my_shape_score = ' '
    points = 0
    total_points = 0

    for row in readings:

        string = row[0]
        opponent = string[0]
        game_result = string[2]

        #Get my shape based on result
        points = calc_my_score(game_result, opponent)

        #accumulate total points as we go along
        total_points += points

    #showtime
    print("total points: ",  total_points)
