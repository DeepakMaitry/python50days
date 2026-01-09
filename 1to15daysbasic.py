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

name = input("what is your name?")
print("Hello " + name + "!")

