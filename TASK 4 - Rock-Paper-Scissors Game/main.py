import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 
game = [rock, paper, scissors]
user = int(input("What do you wanna choose?\n Press 0 for Rock\n Press 1 for Paper\n Press 2 for Scissors\n"))
print(f"You choose:\n {game[user]}")
computer = random.randint(0,2)
print(f"Computer choose:\n {game[computer]}")

if user == 2 and computer == 0 :
  print("You Lose")
  
elif user == 0 and computer == 2 :
  print("You Win")
  
elif user < 0 or user > 2:
 print("You types an invalid number. You Lose")
  
elif computer > user:
  print("You Lose")
  
elif computer < user:
  print("You Win")

elif computer == user:
  print("Its a Draw")



