import random
def display(matrix):
    for x in matrix:
        print(x)

def auto_choice(matrix):
    row = random.randint(0,2)
    col = random.randint(0,2)
    print(row,col, matrix[row][col])
    if matrix[row][col] == '_' or matrix[row][col] != 'X':
        matrix[row][col] = 'O'



    
def winner(matrix, mark):
    
    #check all the rows
    for i in matrix:
        row = all(x == mark == i[0] for x in i)
        if row:
            print("Winner")
            return row

    #check all columns

    for idx in range(len(matrix[0])):
     
        # getting column
        col = [ele[idx] for ele in matrix]
        
        # checking for all Unique elements
        column = all(x == mark == col[0] for x in col)
        if column:
            print(col, column, 'all euqal')
            print("Winner")
            return column
    
    
    #check the 2 digonals
    middleCell = len(matrix) % 2
    firstCell = matrix[0][0]
    lastCell = matrix[len(matrix)-1][len(matrix)-1]
    lastOfFirstRow = matrix[0][len(matrix)-1]
    firstOfLastRow = matrix[len(matrix)-1][0]
    
    firstDiagonal = firstCell == matrix[middleCell][middleCell] == lastCell == mark
    secondDiagonal = firstOfLastRow ==  matrix[middleCell][middleCell] == lastOfFirstRow == mark
    # if (firstDiagonal or secondDiagonal):
    #     print("Winner")
    #     return True
    
    
    return False
            

def user_choice():
    choice = 'wrong'
    acceptable_range = range(0,3)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number(0-2): ")
        
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                
    return int(choice)
    
def replacement_choice(matrix, row, position):
    
    user_placement = input("Type a string to place a position: \n")
    if matrix[row][position] == '_' or matrix[row][position] != 'O':
       matrix[row][position] = user_placement
    return matrix[row][position]
        


def gameOn_choice():
    choice = 'wrong'
    
    while choice not in ['Y', 'N']:
        choice = input("Keep playing? (Y or N): ")
        if choice not in ['Y', 'N']:
            print("invalid choice")
            
        if choice == 'Y':
            return True
        else:
            return False


matrix = [ ['_' for x in range(3)] for y in range(3)]

def game():
    #start
    print("Here is the board you will play with: \n")
    display(matrix)
    row = user_choice()
    position = user_choice()
    
    replacement_choice(matrix, row, position)
    auto_choice(matrix)
    display(matrix)
    endForX = winner(matrix, 'X')
    endForO = winner(matrix, 'O')
    game_on = gameOn_choice()
    
    if game_on and (not endForX or not endForO):
        game()
    
game()