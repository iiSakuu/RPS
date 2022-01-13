# a simple and first version of rock paper scissors
 
import random 
 
print("Hello, welcome to Rock Paper Scissors!")
 
# begin with 0 score
 
score_1 = 0
score_2 = 0
 
available_choices = ['rock', 'paper', 'scissors']
 
# the computer's list of responses
computer_choices = ['rock', 'paper', 'scissors']
 
while score_1 < 3 and score_2 < 3:

    print(f'Player score is {score_1}')
    print(f'Player 2 score is {score_2}')

    choice = input('Please choose Rock, Paper or Scissors\n')
    
    while choice.lower() not in available_choices:
        choice = input('Please choose one of the 3 options!\n')
    
    response = random.choice(computer_choices)
 
    print(f'Computer choice was: {response}')
 
    #evaluating the choices
    if choice.lower() == response:
        score_1 += 0
        print('This round is a draw!')
    elif choice.lower() == "rock":
                if response == "scissors":
                    score_1 += 1
                    print('You win this round!')
                else:
                    score_2 += 1
                    print('The computer wins this round!')
    elif choice.lower() == "paper":
                if response == "rock":
                    score_1 += 1
                    print('You win this round!')
                else: 
                    print('The computer wins this round !')
                    score_2 += 1
    elif choice.lower() == "scissors":
                if response == "paper":
                    score_1 += 1 
                    print('You win this round!')
                else:
                    score_2 += 1
                    print('The computer wins this round !')


print('Game over!')
        
print(f'The final score is: {score_1} - {score_2}')
 
#final score check
if score_1 == 3:
    print('You win this game!')
elif score_1 == score_2:
    print('Looks like it\'s a draw!')
else:
    print('Sorry, you lost! Better luck next time!')
# add score system up to 3