
#Ask user for there name variable example


"""
multiline comment
"""
print("Hello, ")
name = input("What is your name? ")

name = name.strip() #strip is used to remove any leading or trailing whitespace from the input
name = name.capitalize()

name=name.title() #title is used to capitalize the first letter of each word in the string
print("Hello ",end="") #end is used to change the end character of the print statement, by default it is a new line
print(name)

print("Hello, " + name) #concatenation
print("Hello,",name) #multiple arguments


print(f"hello,{name}") #f string, it is a way to format strings in python, it is available in python 3.6 and above, it is more efficient than concatenation and multiple arguments, it is also more readable