#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print("ROCK PAPER SCISSORS\n")
name = input("What is your name? ")

print("Good Luck !", name)
print("\nLet's Play!!\n")

print('Winning rules of the game are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice:: \n 1) Rock \n 2) Paper \n 3) Scissors \n")

    choice = int(input("Enter your choice :\n"))

    while choice > 3 or choice < 1:
        choice = int(input('Invalid!\n Enter a valid choice please '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('Your choice is: \n', choice_name)
    print('Now its Computers Turn......')

    compu_choice = random.randint(1, 3)
    
    while compu_choice == choice:
        compu_choice = random.randint(1, 3)

    if compu_choice == 1:
        compu_choice_name = 'RocK'
    elif compu_choice == 2:
        compu_choice_name = 'Paper'
    else:
        compu_choice_name = 'Scissors'
        
    print("Computer choice is: \n", compu_choice_name)
    print("\n")
    print(choice_name, 'Vs', compu_choice_name)
   
    if choice == compu_choice:
        print('Draw!!\n', end="")
        result = "DRAW"
  
    if (choice == 1 and compu_choice == 2):
        print('Paper wins!!\n', end="")
        result = 'Paper'
        
    elif (choice == 2 and compu_choice == 1):
        print('Paper wins!!\n', end="")
        result = 'Paper'

    if (choice == 1 and compu_choice == 3):
        print('Rock wins!!\n', end="")
        result = 'Rock'
        
    elif (choice == 3 and compu_choice == 1):
        print('Rock wins!!\n', end="")
        result = 'RocK'

    if (choice == 2 and compu_choice == 3):
        print('Scissors wins!!\n', end="")
        result = 'Scissors'
        
    elif (choice == 3 and compu_choice == 2):
        print('Scissors wins!!\n', end="")
        result = 'Rock'
    
    if result == 'DRAW':
        print("Its a tie!!!!\n")
    if result == choice_name:
        print("You win!!!!\n")
    else:
        print("Computer wins!!!!\n")

    print("Do you want to play again? (Y/N)")
    
    ans = input().lower()
    
    if ans == 'n':
        break


print("Thank You! Hope you had a great experience.")


# In[ ]:





# In[ ]:




