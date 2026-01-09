# if else structure
'''
if condition: 
    do this
else:
    do this 
'''

'''
#Example1
age = 20
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 4 spaces indentation is important in Python otherwise error will occur

# Example2
num = int(input("What is the number you want to check?"))
if num%2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
'''

# nested if else
'''
if condition:
    if condition:
        do this
    else:
        do this
else:
    do this
'''

'''
# Example
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
        if num % 2 == 0:
            print("The number is even.")
        else:
            print("
            The number is odd.")
else:
    print("The number is negative.")
'''

# elif condition 

'''
if condition:
    do this
elif condition:
    do this
else:
    do this
''' 
# Example
'''
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
'''

# logical operation 
'''
and 
or 
not 
'''
# Example
'''
num = int(input("Enter a number: "))
if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
elif num > 0 and num % 2 != 0:
    print("The number is positive and odd.")
elif num < 0 and num % 2 == 0:
        print("The number is negative and even.")
elif num < 0 and num % 2 != 0:
    print("The number is negative and odd.")
else:
    print("The number is zero.")
'''
