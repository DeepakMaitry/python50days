# randomisation and python lists 
'''
import random 
import day4my_module

print(day4my_module.pi)


random_integer = random.randint(0, 10)   # 0<= n <= 10
print(random_integer)

random_float = random.random()  # 0.0 <= n < 1.0
print(random_float)

random_float_range = random.random() * 10  # 0.0 <= n < 10.0
print(random_float_range)

random_uniform = random.uniform(1, 10)  # 1.0 <= n < 10.0
print(random_uniform)   # the only difference between randint and uniform is that randint returns integers while uniform returns floats

'''
'''
import random

random_integer = random.randint(0, 1)

if(random_integer == 1):
    print("Heads")
else:
    print("Tails")
'''

'''
# Python Lists

states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
print(states_of_america[0])
print(states_of_america[-1])
print(states_of_america[1:3])
states_of_america[1] = "Pencilvania"
print(states_of_america)
states_of_america.append("Virginia")  # append adds single element to the end of the list
print(states_of_america)
states_of_america.extend(["Maryland", "Massachusetts"])
print(states_of_america)    

# search for more - list data structures
# https://docs.python.org/3/tutorial/datastructures.html
'''
'''
import random
friends = ["Alice", "Bob", "Charlie", "David"]

random_friend = random.choice(friends)
print(random_friend)

# option 2 

random_index = random.randint(0, len(friends) - 1)
random_friend = friends[random_index]
print(random_friend)
'''

'''
states_of_america = ["Delaware", "Pennsylvania", "New Jersey"]
num_of_states = len(states_of_america)
print(num_of_states)
print(states_of_america[num_of_states - 1])
'''

'''
fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
print(fruits_and_veg)
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
'''


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

# rock wins against scissor
# paper wins against rock
# scissors wins against paper

import random 

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)
print("Your choice:")
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)
else:
    print("Invalid choice")

print("Computer's choice:")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
elif computer == 2:
    print(scissors)
else:
    print("Invalid choice")

if user == computer:
    print("It's a draw")
elif user == 0 and computer == 2:
    print("You win")
elif user == 1 and computer == 0:
    print("You win")
elif user == 2 and computer == 1:
    print("You win")
else:
    print("You lose")
