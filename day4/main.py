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

user_choice = int(input("What do you want to choose?\n0 for Rock.\n1 for Paper.\n2 for Scissors\n\n"))
images = [rock, paper, scissors]
print(images[user_choice])

computer_choice = random.randint(0,2)
print(f"\nComputer choice is {computer_choice}")
print(images[computer_choice])

if user_choice >= 3 or user_choice < 0:
  print("Invalide number")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif user_choice < computer_choice:
  print("You lose")
elif user_choice >computer_choice:
  print("You win!")
elif user_choice == computer_choice:
  print("Draw!")
