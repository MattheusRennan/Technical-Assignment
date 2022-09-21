#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Game board

board= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

# menu to play or exit the game
def menu():
    play=1
    while play:
        play = int(input("0. Exit \n"+
                              "1. Play\n"))
        if play:
            game()
        else:
            print("Bye")


# Game

def game():
    round_nbr=0

    while check_winner() == 0:
        print("\nPlayer ", round_nbr%2 + 1)
        print_board()
        line  = int(input("\n Choose line :"))
        column = int(input("Choose column:"))

        if board[line-1][column-1] == 0:
            if(round_nbr%2+1)==1:
                board[line-1][column-1]=1
            else:
                board[line-1][column-1]=-1
        else:
            print("Spot already filled")
            round_nbr -=1

        if check_winner():
            print("\nPlayer ",round_nbr%2 + 1," won after ", round_nbr+1," rounds")
            print_board()  
        round_nbr +=1

# print the board with X and O        
def print_board():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()        
        

# checking out the winner       
def check_winner():
    #checking vertically
    for i in range(3):
        total = board[i][0]+board[i][1]+board[i][2]
        if total==3 or total ==-3:
            return 1

     #checking horizontally
    for i in range(3):
        total = board[0][i]+board[1][i]+board[2][i]
        if total==3 or total ==-3:
            return 1

    #checking diagonally
    diagonal1 = board[0][0]+board[1][1]+board[2][2]
    diagonal2 = board[0][2]+board[1][1]+board[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0


                
menu()


# In[ ]:





# In[ ]:




