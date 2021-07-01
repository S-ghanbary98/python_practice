# 1. Declare function that takes in a username argument as as string. then returns the name.

#def username(name):
#   return name

# 2. Declare a list with numbers 1 - 5. Iterate through the list and display the list

#ls = [1,2, 3,4,5]

#for i in ls:
#    print(i)

# 3. AND - && & == Which one will return a boolean value.
#name = "Shervin"
#if name == "Shervin":


# 4. What is the difference between a list and a tuple?
# Tuples are not mutable ()

# 5. Can we add an element to a list? Can we add an element to a tuple?, Can the element of tuples be of different types?
# Yes, No and Yes


# 6. Create a dictionary with key-value first_name and last_name
#dict = {"first_name": "Shervin","Last_name": "Ghanbary"}
#print(type(dict))
#dict["middle_name"] = "shervael"
#print(dict)

#Create a class called student, initalise the class and create an object of the class.


#class Student:
#    def __init__(self, name):
#        self.name = name


#student = Student("Chris")




# Create two functions that take two arguments each. Function one  = add values, function two subtract values.


def add(a, b):
    return a + b


def sub(x, y):
    return x - y

# Declare a dictionary cost, with eggs = 1.2 milk = 2.30 bread is 1.00
# Write a function that return the total value

dict = {"eggs": 1.2, "milk": 2.3, "bread": 1.00}

def total_value():
    sum = 0
    for value in dict.values():
        sum += value
    return sum

print(total_value())

# Prompt the user to enter an integer, declare a function that checks if the number is odd or even and display back to the user the result.

#enter = input("Integer?")

def OddEven():
    if enter % 2 == 0:
        return "Even"
    else:
        return "Odd"

#select the correct syntax-
#1 -super.__init().
#2- super()__init().
#3 super().__init().
#4 - Super().__init__()

#4

# Declare a tuple with 3 values and iterate through the tuple. Display the values


my_tuple = (3, 4, 5)

for i in my_tuple:
    print(i)


# Create a class called student with a method called student data that return student names. Create a class called devops student and inherit the student class. then print the name.
class student:





    def student_data(self):
        return "shervin"


class Devops(student):
    def __init__(self):
        super().__init__()

c = Devops()
print(c.student_data())


#Declare a variable named city and a method that takes city as an argument. function should check if city == london or not. Return true or false values

city = "London"

def check(city):
    if city == "London":
        return True
    return False
