import os
import time

'''
gameOfLife
'''
def display_array(arr):
    '''
    Function display_array
    '''
    os.system('cls') #Clear terminal screen

    rows = len(arr)

    #Catch empty array
    if rows == 0:
        raise ValueError('Empty input array')

    cols = len(arr[0])

    # Print the contents to the console
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j],end=' ')#Print element

        print() #Print newline

    time.sleep(1) #Pause

def gameOfLife(rows,cols,arr,gen):
    '''
    gameOfLife
    '''

    # Generate a blank 2d output list
    output = [' '] * cols
    for i in range(cols):
        output[i] = [' '] * rows

    # Process throw the elements of the 2d list
    for i in range(cols):
        for j in range(rows):

            liveN = 0 # Living neighbors counter initialization

            if (arr[i][j] == '*'): #If the cell is alive
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
            # Else the current cell is dead
            else:
                if ((i-1) >= 0):

                    try:
                        if (arr[i-1][j] == '*'):
                            liveN += 1
                    except:
                        pass

                    try:
                        if (arr[i-1][j+1] == '*'):
                            liveN += 1
                    except:
                        pass

                    if ((j-1) >= 0):
                        try:
                            if (arr[i-1][j-1] == '*'):
                                liveN += 1
                        except:
                            pass
                if((j-1) >= 0):

                    try:
                        if (arr[i][j-1] == '*'):
                            liveN += 1
                    except:
                        pass

                    try:
                        if (arr[i+1][j-1] == '*'):
                            liveN += 1
                    except:
                        pass

                try:
                    if (arr[i][j+1] == '*'):
                        liveN += 1
                except:
                    pass

                try:
                    if (arr[i+1][j] == '*'):
                        liveN += 1
                except:
                    pass

                try:
                    if (arr[i+1][j+1] == '*'):
                        liveN += 1
                except:
                    pass

                if (liveN == 3):
                    output[i][j] = '*'
                else:
                    output[i][j] = ' '
    if (gen == 1):
        return output
    else:
        return gameOfLife(rows,cols,output,(gen-1))


####################TEST DATA
test = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','*','*','*',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
ctr = 1
while(ctr<40):
    display_array(gameOfLife(12,12,test,ctr))
    ctr += 1
