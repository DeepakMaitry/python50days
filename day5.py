# have i been pwned website to check website 

# for loop 
'''
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
'''

'''
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = 0
for score in student_scores:
    total_score += score
print(total_score)

# or using sum() function

total_score = sum(student_scores)
print(total_score)

# this will give average 
average_score = total_score / len(student_scores)
print(average_score)

# max() function 
highest_score = max(student_scores)
print(highest_score)

# min() function
lowest_score = min(student_scores)
print(lowest_score)

#using for loop finding maximum 
highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print(highest)

'''

'''
# range function 

print(range(1, 10)) # this will do nothing 

for number in range(1, 10):  # last is not included here 10 is not included
    print(number)

for number in range(1, 11): # 11 is not included
    print(number)

for number in range(1, 11, 2): # add 2 in next element
    print(number)

total = 0
for number in range(1, 101): # sum of 1 to 100
    total += number
print(total)
'''

# password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy level
password = ""
for char in range(1, nr_letters + 1):         # to avoid adding 1 in last use this range(0, nr_letters)
    password += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
print(password)

# hard level
password_list = []
for char in range(1, nr_letters + 1):         
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")

#Example 
'''
import random
x = [1, 2, 3, 4, 5]
random.shuffle(x)
print(x)
'''
