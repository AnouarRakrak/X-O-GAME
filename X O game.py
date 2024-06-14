# --------------------------
# --------- X O GAME -------
# --------------------------
blanks= ["1","2","3","4","5","6","7","8","9"]# the number of blanks in the board

for blank in range(0,9,3): # to draw the board
    print(" | ".join(blanks[blank:blank+3]))
    if blank == 6:
        break
    print("-"*9)

while True: # to make the game in loop
    player_1_Input=input("enter you are the X (to surrender type << done >>) : ")# to get the choose of player one
    
    if player_1_Input in blanks:# if the choose is empty blank (a number on it)
        blanks[(int(player_1_Input)-1)] = "X"# replace that number by "X"
        for blank in range(0,9,3):# redraw the new board
            print(" | ".join(blanks[blank:blank+3]))
            if blank == 6:
                break
            print("-"*9)
    elif player_1_Input == 'done':# if the plyer one went to end the game by type 'done'
        break# break the while loop
    
    player_2_Input=input("enter you are the O (to surrender type << done >>) : ")# to get the choose of player two
    
    if player_2_Input in blanks:# if the choose is empty blank (a number on it)
        blanks[(int(player_2_Input)-1)] = "O"# replace that number by "O"
        for blank in range(0,9,3):# redraw the new board
            print(" | ".join(blanks[blank:blank+3]))
            if blank == 6:
                break
            print("-"*9)
    elif player_2_Input == 'done':# if the plyer one went to end the game by type 'done'
        break# break the while loop