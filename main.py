# PYTHON -Python is a general purpose, open source, high-level programming language and also provides number of libraries and frameworks.
# Python is a simple, general purpose, high level, and object-oriented programming language.
# It is popular for its simplicity, easy syntax and user-friendly environment.

## Usage of PYTHON:
    # Desktop Applications
    # Web Applications

    # Data Science
    # Artificial Intelligence
    # Machine Learning
    # Scientific Computing
    # Robotics
    # Internet of Things (IoT)
    # Gaming
    # Mobile Apps
    # Data Analysis and Preprocessing


#    PYTHON Tips to Keep in Mind:

 # 1. Make it Clear Why We Want to Learn
 #    a. Data Analysis and Processing
 #    b. Artificial Intelligence
 #    c. Games
 #    d. Hardware/Sensor/Robots
 #    e. Desktop Applications
 #
 # 2. Learn the Basic Syntax
 # 3. Write Code by Own
 # 4. Keep Practicing
 # 5. Make Notes as Needed
 # 6. Discuss Concepts with Other
 # 7. Do small Projects
 # 8. Teach Others
 # 9. Explore Libraries and Frameworks
 #      TensorFlow - It is an artificial intelligence library which allows us to create large scale AI based projects.
 #       Django - It is an open source framework that allows us to develop web applications. It is easy, flexible, and simple to manage.
 #       Flask - It is also an open source web framework. It is used to develop lightweight web applications.
 #       Pandas - It is a Python library which is used to perform scientific computations.
 #       Keras - It is an open source library, which is used to work around the neural network.
 # 10. Contribute to Open Source


# Python Variables:
#     Variable is a name that is used to refer to memory location.
#     Python variable is also known as an identifier and used to hold value.
#     Variables are group of letters and digits, but they have to begin with a letter or an underscore.
#     We don't need to declare explicitly variable in Python. When we assign any value to the variable, that variable is declared automatically.
#     The equal (=) operator is used to assign value to a variable.
print("John")
''' check the type of it using the Python built-in type() function'''    # ''' ''' - is also way of commenting lines in python
print(type("John"))

# Object Identity:
    # Every created object identifies uniquely in Python
    # Python provides a guarantee that no two objects will have the same identifier.
    # The built-in id() function, is used to identify the object identifier.

a = 1887
b = a
print(id(a))
print(id(b))
a = 500          # Reassigned variable a
print(id(a))

#The multi-word keywords can be created by the following method.
    # Camel Case - Each word in the middle of begins with a capital letter. There is no intervention of whitespace.For example - nameOfStudent, valueOfVaraible, etc.
    # Pascal Case - It is the same as the Camel Case, but here the first word is also capital. For example - NameOfStudent, etc.
    # Snake Case - In the snake case, Words are separated by the underscore. For example - name_of_student, etc.

# Multiple Assignment:
# 1. Assigning single value to multiple variables
# Eg:
x = y = z = 50
print(x)
print(y)
print(z)

# 2. Assigning multiple values to multiple variables:
# Eg:
a, b, c = 5, 10, 15
print(a)
print(b)
print(c)

# Python Variable 2 Types:

# 1. Local Variable
# Local variables are the variables that declared inside the function and have scope within the function.

# Declaring a function
def add():
    # Defining local variables. They has scope only within a function
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)
# Calling a function
add()
# Accessing local variable outside the function
# print(a)                               - throws NameError: name 'a' is not defined

# 2. Global Variables
# Global variables can be used throughout the program, and its scope is in the entire program.
# We can use global variables inside or outside the function.
# A variable declared outside the function is the global variable by default.
# Python provides the global keyword to use global variable inside the function.
# If we don't use the global keyword, the function treats it as a local variable.

# Declare a variable and initialize it
x = 101

# Global variable in function
def mainFunction():
    # printing a global variable  Akanksha
    global x
    print(x)
    # modifying a global variable
    x = 'Welcome Akanksha'
    print(x)

mainFunction()
print(x)

# Delete a variable:

# We can delete the variable using the del keyword.
#
# Syntax -
# del <variable_name>

# Assigning a value to x
x = 6
print(x)
# deleting a variable.
del x
# print(x)    - will throw NameError: name 'x' is not defined


# Maximum Possible Value of an Integer in Python :

# A Python program to display that we can store
# large numbers in Python

a = 10000000000000000000000000000000000000000000
a = a + 1
print(type(a))
print(a)

# we assigned a large integer value to variable x and checked its type.
# It printed class <int> not long int.
# Hence, there is no limitation number by bits and we can expand to the limit of our memory.
# Python doesn't have any special data type to store larger numbers.


# Print Single and Multiple Variables in Python :

# Example - 1 (Printing Single Variable)
# printing single value
a = 5
print(a)
print((a))

# Example - 2 (Printing Multiple Variables)

a = 5
b = 6
# printing multiple variables
print(a,b)
# separate the variables by the comma
print(1, 2, 3, 4, 5, 6, 7, 8)

# Basic Fundamentals:
# a)Tokens and their types.
# b) Comments

# a)Tokens:
# The tokens can be defined as a punctuator mark, reserved words, and each word in a statement.
# The token is the smallest unit inside the given program.
# There are following tokens in Python:
# 1. Keywords.
# 2. Identifiers(Variables).
# 3. Literals.
# 4. Operators.

# Python Data Types:
# Variables can hold values, and every value has a data-type.
# Python is a dynamically typed language; hence we do not need to define the type of the variable while declaring it.
# The interpreter implicitly binds the value with its type.

# Python provides us the type() function, to check the type of the variable
a=10
b="Hi Python"
c = 10.5
print(type(a))
print(type(b))
print(type(c))

## Standard data types:
# A variable can hold different types of values.
# For example - A person's name must be stored as a string whereas its id must be stored as an integer.
# Python provides various standard data types that define the storage method on each of them  , they are -
#     1. Numbers(Number stores numeric values.) - Integers, Float, Complex Number
#     2. Sequence Type - String, List, Tuple
#     3. Boolean
#     4. Set
#     5. Dictionary

# 1. Numbers
# NOTE : The isinstance() function is used to check an object belongs to a particular class.
# Number objects is created when a number is assigned to a variable.
# For example -
a = 5
print("The type of a", type(a))

b = 40.5
print("The type of b", type(b))

c = 1 + 3j
print("The type of c", type(c))
print(" c is a complex number", isinstance(1 + 3j, complex))

# 2. Sequence Type :
# The string can be defined as the sequence of characters represented in the quotation marks.
# In Python, we can use single, double, or triple quotes to define a string.

# Example - 1

str = "string using double quotes"
print(str)
s = '''''A multiline 
string'''
print(s)

# Example - 2

str1 = 'hello Akanksha' #string str1
str2 = ' how are you' #string str2lpll
print (str1[0:2]) #printing first two character using slice operator
print (str1[4]) #printing 4th character of the string
print (str1*2) #printing the string twice
print (str1 + str2) #printing the concatenation of str1 and str2

# List:
# Python Lists are similar to arrays in C.the list can contain different data types
# The items stored in the list are separated with a comma (,) and enclosed within square brackets [].
# We can use slice [:] operators to access the data of the list.
# The concatenation operator (+) and repetition operator (*) works with the list in the same way as they were working with the strings.
# Example:
list1 = [1, "hi", "Python", 2]
# Checking type of given list
print(type(list1))
# Printing the list1
print(list1)
# List slicing
print(list1[3:])    # 3rd place se leke pura end place tak
# List slicing
print(list1[0:2])   # start from 0 but end before 2
# List Concatenation using + operator
print(list1 + list1)
# List repetation using * operator
print(list1 * 3)

# Tuple:
# A tuple is similar to the list . Like lists, tuples also contain the collection of the items of different data types.
# The items of the tuple are separated with a comma (,) and enclosed in parentheses ().
# A tuple is a read-only data structure as we can't modify the size and value of the items of a tuple.

# Ex -
tup = ("hi", "Python", 2)
# Checking type of tup
print(type(tup))

# Printing the tuple
print(tup)

# Tuple slicing
print(tup[1:])   # 1st place se leke pura end place tak
print(tup[0:1])  # start from 0 but end before 1

# Tuple concatenation using + operator
print(tup + tup)

# Tuple repatation using * operator
print(tup * 3)

# # Adding value to tup. It will throw an error.
# tup[2] = "hi"
# print(tup)

# Dictionary :
# Dictionary is an unordered set of a key-value pair of items.
# It is like an associative array or a hash table where each key stores a specific value.
# Key can hold any primitive data type, whereas value is an arbitrary Python object.
# The items in the dictionary are separated with the comma (,) and enclosed in the curly braces {}.

# Ex -
d = {1: 'Jimmy', 2: 'Alex', 3: 'john', 4: 'mike'}
# Printing dictionary
print(d)
# Accesing value using keys
print("1st name is " + d[1])
print("2nd name is " + d[4])
print(d.keys())
print(d.values())

# Boolean :
# Boolean type provides two built-in values, True and False.
# These values are used to determine the given statement true or false.It denotes by the class bool.
# True can be represented by any non-zero value or 'T' whereas false can be represented by the 0 or 'F'.

# Ex -
# Python program to check the boolean type
print(type(True))
print(type(False))
# print(false)

# Set :
# Python Set is the unordered collection of the data type.
# It is iterable, mutable(can modify after creation), and has unique elements.
# In set, the order of the elements is undefined; it may return the changed sequence of the element.
# The set is created by using a built-in function set(), or a sequence of elements is passed in the curly braces and separated by the comma.
# It can contain various types of values

# Ex -
# Creating Empty set
set1 = set()

set2 = {'James', 2, 3, 'Python'}
# Printing Set value
print(set2)

# Adding element to the set
set2.add(10)
print(set2)

# Removing element from the set
set2.remove(2)
print(set2)

##Python Keywords :
    # Python Keywords are special reserved words that convey a special meaning to the compiler/interpreter.
    # Each keyword has a special meaning and a specific operation.
    # These keywords can't be used as a variable.

# 1. True - It represents the Boolean true, if the given condition is true, then it returns "True". Non-zero values are treated as true.
# 2. False - It represents the Boolean false; if the given condition is false, then it returns "False". Zero value is treated as false
# 3. None - It denotes the null value or void. An empty list or Zero can't be treated as None.
# 4. and - It is a logical operator. It is used to check the multiple conditions. It returns true if both conditions are true.
# 5. or - It is a logical operator in Python. It returns true if one of the conditions is true.
# 6. not - It is a logical operator and inverts the truth value.
# 7. assert - This keyword is used as the debugging tool in Python. It checks the correctness of the code. It raises an AssertionError if found any error in the code and also prints the message with an error.
# Example:
# a = 10
# b = 0
# print('a is dividing by Zero')
# assert b != 0
# print(a / b)

# 8. def - This keyword is used to declare the function in Python. If followed by the function name.
def my_func(a,b):
    c = a+b
    print(c)
my_func(10,20)

# 9. class - It is used to represents the class in Python. The class is the blueprint of the objects. It is the collection of the variable and methods.
# class Myclass:
#    #Variables……..
#    def function_name(self):
#       #statements………

# 10. continue - It is used to stop the execution of the current iteration.
a = 0
while a < 4:
  a += 1
  if a == 2:
    continue
  print(a)

# 11. break - It is used to terminate the loop execution and control transfer to the end of the loop. Consider the following example.
for i in range(5):
    if(i==3):
        break
    print(i)
print("End of execution")

# 12. If - It is used to represent the conditional statement. The execution of a particular block is decided by if statement. Consider the following example.
i = 18
if (i<12):
    print("I am less than 18")

# 13. else - The else statement is used with the if statement. When if statement returns false, then else block is executed. Consider the following example.
n = 11
if(n%2 == 0):
    print("Even")
else:
    print("odd")

# 14. elif - This Keyword is used to check the multiple conditions. It is short for else-if. If the previous condition is false, then check until the true condition is found. Condition the following example.
# marks = int(input("Enter the marks:"))
# if(marks>=90):
#     print("Excellent")
# elif(marks<90 and marks>=75):
#     print("Very Good")
# elif(marks<75 and marks>=60):
#     print("Good")
# else:
#     print("Average")

# 15. del - It is used to delete the reference of the object. Consider the following example.
a=10
b=12
del a
print(b)
# a is no longer exist
# print(a)

# 16. try, except - The try-except is used to handle the exceptions. The exceptions are run-time errors. Consider the following example.
a = 0
try:
    b = 1 / a
except Exception as e:
    print(e)

# 17. raise - The raise keyword is used to throw the exception forcefully. Consider the following example.
# a = 5
# if (a>2):
#    raise Exception('a should not exceed 2 ')

# 18. finally - The finally keyword is used to create a block of code that will always be executed no matter the else block raises an error or not. Consider the following example.']
a=0
b=5
try:
    c = b/a
    print(c)
except Exception as e:
    print(e)
finally:
    print('Finally always executed')

# 19. for, while - Both keywords are used for iteration. The for keyword is used to iterate over the sequences (list, tuple, dictionary, string). A while loop is executed until the condition returns false.
# Example: For loop

list = [1,2,3,4,5]
for i in list:
    print(i)

# Example: While loop

a = 0
while(a<5):
    print(a)
    a = a+1

# 20. import - The import keyword is used to import modules in the current Python script. The module contains a runnable Python code.
# Example:
import math
print(math.sqrt(25))

# 21. from - This keyword is used to import the specific function or attributes in the current Python script.
# Example:
from math import sqrt
print(sqrt(25))

# 22. as - It is used to create a name alias. It provides the user-define name while importing a module.
# Example:
import calendar as cal
print(cal.month_name[5])

# 23. pass - The pass keyword is used to execute nothing or create a placeholder for future code.
# If we declare an empty class or function, it will throw an error, so we use the pass keyword to declare an empty class or function.
# Example:
class my_class:
    pass
def my_func():
    pass

# 24. return - The return keyword is used to return the result value or none to called function.
# Example:
def sum(a, b):
    c = a + b
    return c
print("The sum is:", sum(25, 15))

# 25. is - This keyword is used to check if the two-variable refers to the same object. It returns the true if they refer to the same object otherwise false
# Example

x = 5
y = 5

a = []
b = []
print(x is y)
print(a is b)

# 26. global - The global keyword is used to create a global variable inside the function. Any function can access the global.
# ex-
def my_func():
    global a
    a = 10
    b = 20
    c = a + b
    print(c)
my_func()
def func():
    print(a)
func()

# 27. nonlocal - The nonlocal is similar to the global and used to work with a variable inside the nested function(function inside a function). Consider the following example.
# Example

def outside_function():
    a = 20
    def inside_function():
        nonlocal a
        a = 30
        print("Inner function: ",a)
    inside_function()
    print("Outer function: ",a)
outside_function()

# 28. lambda - The lambda keyword is used to create the anonymous function in Python. It is an inline function without a name. Consider the following example.
# Example :
#
a = lambda x: x**2
for i in range(1,6):
  print(a(i))

# 29. yield - The yield keyword is used with the Python generator. It stops the function's execution and returns value to the caller. Consider the following example.
def fun_Generator():
    yield 1
    yield 2
    yield 3
# Driver code to check above generator function
for value in fun_Generator():
  print(value)

# 30. with - The with keyword is used in the exception handling. It makes code cleaner and more readable. The advantage of using with, we don't need to call close().
# Example:

with open('file_path', 'w') as file:
    file.write('hello world !')


# 31. None - The None keyword is used to define the null value. It is remembered that None does not indicate 0, false, or any empty data-types. It is an object of its data type
# Example:

def return_none():
    a = 10
    b = 20
    c = a + b


x = return_none()
print(x)


str2='''''welcome  
to  
SSSIT'''
print(str2)

def intro():
  """
  This function prints Hello Joseph
  """
  print("Hi Joseph")
intro()
for i in range(10):
    print(i,end = ' ')
