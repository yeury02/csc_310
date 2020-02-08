# Yeury Galva Liriano
# Timothy Terrence Colaneri
# CSC310 Assignment 1

import os
import time
import sys
from random import randint

'''
gameOfLife
This program simulates Conways game of life within 2 dimensional
python lists.
'''
def get_board_size(rows,cols):
    '''
    get_board_size
    This function takes in two parameters, 
    1 - rows: the requested number or rows for output array
    2 - cols: the requested number of columns for the output array
    This function then produces a randomly generated array of spaces
    and asterisks for the gameOfLife function.
    This function then returns the generated array.
    '''
    board = [] #initialize output array

    for i in range(0, cols): #iterate the columns
        each_row = []
        for j in range(0, rows): #iterate the rows

            r = randint(0, 1) #randomly assign space or * to the element
            if r == 1:
                each_row.append('*')
            if r == 0:
                each_row.append(' ')
        board.append(each_row)

    return board #return the randomly generated array


def gameOfLife(rows, cols,arr, gen):
    '''
    gameOfLife
    This function takes in:
    1 - rows- the # of rows in the 2d python list
    2 - cols- the # of cols in the 2d python list
    3 - arr- the 2d python list, the 'board'
    4 - gen- # of iteratons of Conway's game of life

    The function then simulates Conway's game of life
    and returns a 2d python list containing the output.
    '''
    # Generate a blank 2d output list
    output = [' '] * cols
    for i in range(cols):
        output[i] = [' '] * rows

    # Process throw the elements of the 2d list
    for i in range(cols):
        for j in range(rows):

            liveN = 0 # Living neighbors counter initialization

            # UGLY if switch ahead
            # Python exhibits different behaviors if we run off the
            # left or right hand side of a list.
            # therefore we use if checks to catch left side runoffs
            # and try/excepts to catch right side run offs

            if (arr[i][j] == '*'): #If the cell is alive      *ALIVE CELL*
                                 # Counts its living neighbors

                if ((i-1) >= 0): # Negative index catch
                    if (arr[i-1][j] == '*'): #                check (x-1,y)
                       liveN += 1

                    try: #Catch going off the right side
                        if (arr[i-1][j+1] == '*'):#           check (x-1,y+1)
                            liveN += 1
                    except IndexError:
                        pass

                    if ((j-1) >= 0): # Negative index catch
                        if (arr[i-1][j-1] == '*'): #          Check (x-1,y-1)
                            liveN += 1

                if((j-1) >= 0):# Negative index catch

                    if (arr[i][j-1] == '*'):#                 Check (x,y-1)
                        liveN += 1

                    try:# Catch going off the right side
                        if (arr[i+1][j-1] == '*'):#           Check (x+1,y-1)
                            liveN += 1
                    except IndexError:
                        pass

                try:#Catch going off the right side
                    if (arr[i][j+1] == '*'):#                 Check (x,y+1)
                        liveN += 1
                except IndexError:
                    pass

                try:#Catch going off the right side
                    if (arr[i+1][j] == '*'):#                 Check (x+1,y)
                        liveN += 1
                except IndexError:
                    pass

                try:#Catch going off the right side
                    if (arr[i+1][j+1] == '*'):#               Check (x+1,y+1)
                        liveN += 1
                except IndexError:
                    pass

                #Print the cells next value to the output list
                if (liveN == 2) or (liveN == 3):# cell is still alive
                    output[i][j] = '*'
                else:                           # cell died
                    output[i][j] = ' '
            # Else the current cell is dead                     *DEAD CELL*
            else:
                if ((i-1) >= 0):# Negative index catch

                    try:#Catch going off the right side
                        if (arr[i-1][j] == '*'):#               Check(x-1,y)
                            liveN += 1
                    except IndexError:
                        pass

                    try:#Catch going off the right side
                        if (arr[i-1][j+1] == '*'):#             Check(x-1,y+1)
                            liveN += 1
                    except IndexError:
                        pass

                    if ((j-1) >= 0):# Negative index catch
                        try:#Catch going off the right side
                            if (arr[i-1][j-1] == '*'):#         Check(x-1,y-1)
                                liveN += 1
                        except IndexError:
                            pass
                if((j-1) >= 0):# Negative index catch

                    try:#Catch going off the right side
                        if (arr[i][j-1] == '*'):#               Check(x,y-1)
                            liveN += 1
                    except IndexError:
                        pass

                    try:#Catch going off the right side
                        if (arr[i+1][j-1] == '*'):#             Check(x+1,y-1)
                            liveN += 1
                    except IndexError:
                        pass

                try:#Catch going off the right side
                    if (arr[i][j+1] == '*'):#                   Check(x,y+1)
                        liveN += 1
                except IndexError:
                    pass

                try:#Catch going off the right side
                    if (arr[i+1][j] == '*'):#                   Check(x+1,y)
                        liveN += 1
                except IndexError:
                    pass

                try:#Catch going off the right side
                    if (arr[i+1][j+1] == '*'):#                 Check(x+1,y+1)
                        liveN += 1
                except IndexError:
                    pass

                #Print the cells next value to the output list
                if (liveN == 3):
                    output[i][j] = '*'
                else:
                    output[i][j] = ' '

    # If there are no more generations to iterate, return the output
    # Else run another generation
    if (gen == 1):
        return output
    else:
        return gameOfLife(rows,cols,output,(gen-1))

def display_array(board):
    '''
    Function display_array
    This function displays the contents a 1d or 2d python list
    that is passed into it.
    '''
    os.system('cls') #Clear terminal screen

    rows = len(board)

    #Catch empty array
    if rows == 0:
        raise ValueError('Empty input array')

    cols = len(board[0])

    # Print the contents to the console
    for i in range(rows):
        for j in range(cols):
            print(board[i][j],end=' ')#Print element

        print() #Print newline

    time.sleep(1) #Pause


if __name__ == '__main__':
    '''
    Main function
    '''
    if len(sys.argv) != 4: # arguments check
        sys.stdout.write("you must pass filename, rows, columns, and generations in that order as command line arguments")
        sys.exit(1)
    else:                   #run game of life
        rows, cols, gen = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        board = get_board_size(rows,cols)

        i = 1
        while(i<gen):       #Display the generations
            display_array(gameOfLife(rows,cols,board,i))
            i += 1