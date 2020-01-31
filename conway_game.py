import os 
import time

def display_array(ar):
    "clear the screen, display the contents of an array, wait for 1sec"
    os.system("clear")

    rows = len(ar)  # grab the rows

    if rows == 0:
        raise ValueError("Array contains no data")

    cols = len(ar[0])   # grab the columns - indices start at 0!

    for i in range(rows):
        for j in range(cols):
            print(ar[i][j], end=' ')    # no carriage return, space separated
        print()

    time.sleep(1)