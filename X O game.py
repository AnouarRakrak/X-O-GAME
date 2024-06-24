# --------------------------
# --------- X O GAME -------
# --------------------------
blanks= ["1","2","3","4","5","6","7","8","9"]# the number of blanks in the board
win_forms=[["1","2","3"],["4","5","6"],["7","8","9"],["1","4","7"],["2","5","8"],["3","6","9"],["3","5","7"],["1","5","9"]] # wins conditions (diagonaly or horizontaly or verticaly)

for blank in range(0,9,3): # to draw the board
    print(" | ".join(blanks[blank:blank+3]))
    if blank == 6:
        break
    print("-"*9)
a=True
while a==True: # to make the game in loop
    player_1_Input=input("enter you are the X (to surrender type << done >>) : ")# to get the choose of player one
    
    if player_1_Input in blanks:# if the choose is empty blank (a number on it)
        blanks[(int(player_1_Input)-1)] = "X"# replace that number by "X"
        
        for Xs in win_forms:# to put the sign in the forms
            if player_1_Input in Xs:
                Xs[Xs.index(player_1_Input)] = "X"
        
        for blank in range(0,9,3):# redraw the new board
            print(" | ".join(blanks[blank:blank+3]))
            if blank == 6:
                break
            print("-"*9)

    elif player_1_Input == 'done':# if the plyer one went to end the game by type 'done'
        break# break the while loop
    
    for form in win_forms: # to check if the condition form elements in all like the sign
        if form[0] == form[1] == form[2] == "X":
            print("Player 1 Wins !!!")
            a=False # if true break the while loop
    if a==False:
        break
    
    player_2_Input=input("enter you are the O (to surrender type << done >>) : ")# to get the choose of player two
    
    if player_2_Input in blanks:# if the choose is empty blank (a number on it)
        blanks[(int(player_2_Input)-1)] = "O"# replace that number by "O"
        
        for Os in win_forms: # to put the sign in the forms
            if player_2_Input in Os:
                Os[Os.index(player_2_Input)] = "O"
        
        for blank in range(0,9,3):# redraw the new board
            print(" | ".join(blanks[blank:blank+3]))
            if blank == 6:
                break
            print("-"*9)
    
    elif player_2_Input == 'done':# if the plyer one went to end the game by type 'done'
        break# break the while loop
    
    for form in win_forms:
        if form[0] == form[1] == form[2] == "O":# to check if the condition form elements in all like the sign
            print("Player 2 Wins !!!")
            a=False # if true break the while loop
    if a==False:
        break