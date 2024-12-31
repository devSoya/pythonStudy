from random import randint

user_choice = int(input("Choose number ."))
pc_choice = randint(1, 50) # I imported this

if user_choice == pc_choice:
  print("You won!")
elif user_choice > pc_choice:
  print("Lower!")
elif user_choice < pc_choice:
  print("Higher!")