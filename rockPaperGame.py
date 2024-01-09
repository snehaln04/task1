import random
while True:

 user_score = 0 
 comp_score = 0
 ties = 0

 print("Rules for the game: ")
 print("""
    1. Paper VS Rock ---> Paper
    2. Rock VS Scissors ---> Rock
    3. Scissosrs VS Paper ---> Scissors """)
 
 print(""" Choices are -
      1. ROCK
      2. PAPER
      3. SCISSORS""")
 choice = int(input("enter your choice from 1-3 : "))
 print()

 while(choice > 3 or choice <1):
  choice= int(input("please enter valid input"))
 if(choice==1):
    user_choice = "Rock"

 elif(choice==2):
   user_choice = "Paper"
 else:
   user_choice = "Scissors"
 print("user's choice is ", user_choice)
 print()
 print("now its computer turn.....")
 print()

 computer = random.randint(1,3)
 if(computer == 1):
  comp_choice = "Rock"
 elif(computer == 2):
  comp_choice = "Paper"
 else:
  comp_choice = "Scissors"
 print("computer choice is ", comp_choice)
 print()


 if(user_choice == comp_choice):
  print("it's tie")
  result = "tie"
 elif(user_choice =="rock" and comp_choice =="scissors")or(user_choice =="scissors" and comp_choice =="paper")or(user_choice =="paper" and comp_choice =="rock"):
  print("you win")
  result = "you win"
 else:
  print( "you lose")
  result = "you lose"

 if((user_choice == "Paper" and comp_choice == "Rock")) or ((user_choice == "rock" and comp_choice == "Paper")):
  print("paper win")
  result = "paper"

 elif((user_choice == "rock" and comp_choice == "scissors")) or ((user_choice == "scissors" and comp_choice == "rock")):
  print("rock win")
  result = "rock"
 else:
  print("scissors win")
  result = "scissors"

 if(result=="tie"):
  ties += 1
 elif(result=="user_choice"):
  user_score += 1
 else:
  comp_score += 1

 print("scores are")
 print("your score is: ", user_score)
 print("computer score is: ", comp_score)
 print("ties are:",ties)

 play_again = input("Do you want to play again....(Yes/No): ")
 if(play_again=="Yes"):
  break
 else:
  print("GAME OVER......")
  print("Thanks for playing.....")
