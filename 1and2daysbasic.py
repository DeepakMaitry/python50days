'''
print("Hello Deepak!")

print("Hello \nWorld!") # new line 

print("Hello" + " World!") # concatenation

print("Hello " * 3) # repetition

print("Hello"[0]) # indexing

print("Hello"[1:4]) # slicing
print(len("Hello")) # length
print("Hello".upper()) # upper case
print("Hello".lower()) # lower case
print("  Hello  ".strip()) # trimming whitespace
print("Hello".replace("H", "J")) # replacing characters

print("World" in "Hello World") # membership test
print("World" not in "Hello World") # membership test

print("Hello {}".format("Deepak")) # string formatting
print(f"Hello {'Deepak'}") # f-string formatting
print("The value of pi is approximately {:.2f}".format(3.14159)) # formatted float

print("Hello".startswith("H")) # startswith
print("Hello".endswith("o")) # endswith
print("Hello World".split()) # splitting
print("-".join(["Hello", "World"])) # joining
print("Hello World".count("o")) # counting occurrences
print("Hello World".find("World")) # finding substring
print("Hello World".index("World")) # finding substring with index
print("Hello World".capitalize()) # capitalize

print("hello world".title()) # title case
print("Hello World".swapcase()) # swap case
print("Hello\tWorld") # tab character
print("Hello\rWorld") # carriage return
print("Hello\bWorld") # backspace
'''


#input function 

'''
name = input("Enter your name: ")
print("Hello " + name + "!")

age = input("Enter your age: ")
print("You are " + age + " years old.")

print("You are " + input("Enter your height in cm: ") + " cm tall.")

weight = input("Enter your weight in kg: ")
print("You weigh " + weight + " kg.")

city = input("Enter your city: ")
print("You live in " + city + ".")
'''
# variables 

# name = input("what is your name?")
# print("Hello " + name + "!")

# print(len(input("write something?")))

'''
name = input("what is your name?\n")
length = len(name)
print(length)
'''

# rules of variable naming
# 1. variable names must start with a letter or underscore (_)
# 2. variable names can only contain letters, numbers, and underscores
# 3. variable names are case-sensitive
# 4. variable names cannot be a reserved keyword in Python 

# Day 2:
# Data types 

# 1. int
# 2. float
# 3. str
# 4. bool
# 5. list
# 6. tuple
# 7. dict
# 8. set
# 9. None

# type() function
'''
print(type(10)) # int
print(type(10.5)) # float
print(type("10")) # str
print(type(True)) # bool
print(type([1, 2, 3])) # list
print(type((1, 2, 3))) # tuple
print(type({"name": "Deepak", "age": 20})) # dict
print(type({1, 2, 3})) # set
print(type(None)) # None
'''

# type conversion
'''
print(int(10.5)) # float to int
print(float(10)) # int to float
print(str(10)) # int to str
print(bool(1)) # int to bool
print(bool(0)) # int to bool
print(list((1, 2, 3))) # tuple to list
print(tuple([1, 2, 3])) # list to tuple
print(dict([("name", "Deepak"), ("age", 20)])) # list of tuples to dict
print(set([1, 2, 3])) # list to set
print(list({1, 2, 3})) # set to list
'''

# basic math operations
'''
print(10 + 5) # addition
print(10 - 5) # subtraction
print(10 * 5) # multiplication
print(10 / 5) # division
print(10 % 5) # modulus
print(10 ** 5) # exponentiation
print(10 // 5) # floor division
'''

# math functions
'''
print(round(10.5)) # round
print(abs(-10)) # absolute
print(max(10, 5)) # maximum
print(min(10, 5)) # minimum
print(sum([1, 2, 3])) # sum
print(pow(10, 5)) # power
print(divmod(10, 5)) # division remainder
'''
# order of operations
'''
print(10 + 5 * 2) # multiplication first
print((10 + 5) * 2) # parentheses first
'''

# string methods
'''
name = "Deepak"
print(name.upper()) # upper
print(name.lower()) # lower
print(name.capitalize()) # capitalize
print(name.title()) # title
print(name.swapcase()) # swapcase
print(name.count("e")) # count
print(name.find("e")) # find
print(name.index("e")) # index
print(name.replace("e", "a")) # replace
print(name.startswith("D")) # startswith
print(name.endswith("k")) # endswith
print(name.split()) # split
print(name.strip()) # strip
print(name.lstrip()) # lstrip
print(name.rstrip()) # rstrip
print(name.center(10)) # center
print(name.ljust(10)) # ljust
print(name.rjust(10)) # rjust
print(name.zfill(10)) # zfill
print(name.isupper()) # isupper
print(name.islower()) # islower
print(name.isalpha()) # isalpha
print(name.isdigit()) # isdigit
print(name.isalnum()) # isalnum
print(name.istitle()) # istitle
print(name.isspace()) # isspace
print(name.encode()) # encode
print(name.format()) # format
print(f"My name is {name}") # f-string
'''

'''
print("hello"[-1]) # last character
print("hello"[-3:-1]) # slicing with negative indices
print("hello world".replace("world", "there")) # replacing substring
print("hello world".upper().replace("WORLD", "THERE").lower()) # chaining methods

# we use , or _ to make large numbers more readable
print(1_000_000 + 2_000_000) # 3000000
print(1,000,000 + 2,000,000) # 3000000

'''

# f-strings with expressions
'''
name = "Deepak"
age = 20
print(f"My name is {name} and I am {age} years old.") # f-string
print(f"In five years, I will be {age + 5} years old.") # f-string with expression
print(f"My name in uppercase is {name.upper()}.") # f-string with method
print(f"My name in lowercase is {name.lower()}.") # f-string with method
print(f"My name in title case is {name.title()}.") # f-string with method
print(f"My name in swap case is {name.swapcase()}.") # f-string with method
print(f"My name in center is {name.center(10)}.") # f-string with method
print(f"My name in ljust is {name.ljust(10)}.") # f-string with method
print(f"My name in rjust is {name.rjust(10)}.") # f-string with method
print(f"My name in zfill is {name.zfill(10)}.") # f-string with method
print(f"My name in encode is {name.encode()}.") # f-string with method
print(f"My name in format is {name.format()}.") # f-string with method
print(f"My name in isupper is {name.isupper()}.") # f-string with method
print(f"My name in islower is {name.islower()}.") # f-string with method
print(f"My name in isalpha is {name.isalpha()}.") # f-string with
print(f"My name in isdigit is {name.isdigit()}.") # f-string with method
print(f"My name in isalnum is {name.isalnum()}.") # f-string with
print(f"My name in istitle is {name.istitle()}.") # f-string with
print(f"My name in isspace is {name.isspace()}.") # f-string with method
print(f"My name in startswith is {name.startswith('D')}.") # f-string with
print(f"My name in endswith is {name.endswith('k')}.") # f-string with
print(f"My name in split is {name.split()}.") # f-string with
print(f"My name in strip is {name.strip()}.") # f-string with
print(f"My name in lstrip is {name.lstrip()}.") # f-string with
print(f"My name in rstrip is {name.rstrip()}.") # f-string with
print(f"My name in count is {name.count('e')}.") # f-string with
print(f"My name in find is {name.find('e')}.") # f-string with
print(f"My name in index is {name.index('e')}.") # f-string with
print(f"My name in replace is {name.replace('e', 'a')}.") # f-string with
print(f"My name in capitalize is {name.capitalize()}.") # f-
print(f"My name in title is {name.title()}.") # f-
print(f"My name in upper is {name.upper()}.") # f-
print(f"My name in lower is {name.lower()}.") # f-
print(f"My name in swapcase is {name.swapcase()}.") # f-
print(f"My name in center is {name.center(10)}.") # f-
print(f"My name in ljust is {name.ljust(10)}.") # f-
print(f"My name in rjust is {name.rjust(10)}.") # f-
print(f"My name in zfill is {name.zfill(10)}.") # f-
print(f"My name in encode is {name.encode()}.") # f-
print(f"My name in format is {name.format()}.") # f-
print(f"My name in isupper is {name.isupper()}.") # f-
print(f"My name in islower is {name.islower()}.") # f-
print(f"My name in isalpha is {name.isalpha()}.") # f-
print(f"My name in isdigit is {name.isdigit()}.") # f-
print(f"My name in isalnum is {name.isalnum()}.") # f-
print(f"My name in istitle is {name.istitle()}.") # f-
print(f"My name in isspace is {name.isspace()}.") # f-
'''

'''
len("Hello")
print(type(len("Hello"))) # int
print(type("abc")) # str
print(type(10)) # int
print(type(10.5)) # float
print(type(True)) # bool
print(type([1, 2, 3])) # list
print(type((1, 2, 3))) # tuple 
print(type({"name": "Deepak", "age": 20})) # dict
print(type({1, 2, 3})) # set
print(type(None)) # None
''' 

# type conversion

'''
print(int(10.5)) # float to int
print(float(10)) # int to float
print(str(10)) # int to str
print(bool(1)) # int to bool
print(bool(0)) # int to bool
print(list((1, 2, 3))) # tuple to
print(tuple([1, 2, 3])) # list to tuple
print(dict([("name", "Deepak"), ("age", 20)])) # list of tuples to dict
print(set([1, 2, 3])) # list to set
print(list({1, 2, 3})) #
print(set([1, 2, 3])) # list to set
print(list({1, 2, 3})) # set to list
print(tuple({1, 2, 3})) # set to tuple
print(dict({"name": "Deepak", "age": 20}.items())) # dict to dict
print(dict({"name": "Deepak", "age": 20}.keys())) # dict to dict
print(dict({"name": "Deepak", "age": 20}.values())) # dict to dict
print(set({"name": "Deepak", "age": 20}.items())) # dict to set
print(set({"name": "Deepak", "age": 20}.keys())) # dict to set
print(set({"name": "Deepak", "age": 20}.values())) # dict to set
print(list({"name": "Deepak", "age": 20}.items())) # dict to list
print(list({"name": "Deepak", "age": 20}.keys())) # dict to list
print(list({"name": "Deepak", "age": 20}.values())) # dict to list
print(tuple({"name": "Deepak", "age": 20}.items())) # dict to tuple
print(tuple({"name": "Deepak", "age": 20}.keys())) # dict to tuple
print(tuple({"name": "Deepak", "age": 20}.values())) # dict to tuple
print(str(10)) # int to str
print(str(10.5)) # float to str
print(str(True)) # bool to str
print(str([1, 2, 3])) # list to str
print(str((1, 2, 3))) # tuple to str
print(str({"name": "Deepak", "age": 20})) # dict to str
print(str({1, 2, 3})) # set to str
print(str(None)) # None to str
'''
# we cannot concatenate different data types directly

# mathematical operations 
'''
print(10 + 5) # addition
print(10 - 5) # subtraction
print(10 * 5) # multiplication
print(10 / 5) # division
print(10 % 5) # modulus
print(10 ** 5) # exponentiation
print(10 // 5) # floor division  # removes decimal part
'''
#
# math functions
'''
print(round(10.5)) # round
print(abs(-10)) # absolute
print(max(10, 5)) # maximum
print(min(10, 5)) #
print(sum([1, 2, 3])) #
print(pow(10, 5)) # power
print(divmod(10, 5)) # division remainder
'''
# order of operations
# PEMDAS
# parentheses , exponents , multiplication , division , addition , subtraction

# BMI Calculator
'''
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")
'''

''' 
bmi = 63 / (1.65 **2)
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bmi, 2))
print(f"{bmi:.2f}")
'''

'''
score = 0
score += 1
score -= 1
score *= 2
score /= 2
score += 5
score -= 3
score *= 4
score /= 2
print(f"Your score is {score}")

# note: you can use +=, -=, *=, /= with any mathematical operation 
# note : f string can contain any expression
'''

'''
# tip calculator 
print("Welcome to the tip calculator!")
print("---------------------------------")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_amount = (tip / 100) * bill
total_bill = bill + tip_amount
bill_per_person = total_bill / people
print(f"Each person should pay: ${bill_per_person:.2f}")

# note: always round up to 2 decimal places when dealing with money
'''
