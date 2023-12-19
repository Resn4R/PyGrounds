#Chapter 1: Introduction to Python
print("Hello, World!")

name = 'Python'
name2 = "Python"
print("hello, {name}".format(name=name))

print(type(name2))

x = 10
y = 2

print(x + y) # 12
print(x - y) # 8
print(x * y) # 20
print(x / y) # 5.0
print(x ** y) # 100
print(x % y) # 0
print(x // y) # 5


#Chapter 2: Control Flow and Data Structures

if x < y:
    print (str(x)+' is less than '+str(y))
else:
    print(str(x)+' is more than '+str(y))
    
fruits = ['apple', 'banana', 'tomato']
for i, fruit in enumerate(fruits):
    print(i,fruit)
    
count = 0 

while count < 10:
    print(count)
    count += 1 #count++ doesn't work
    
def add(x,y):
    return x+y 
    
def multiply(x,y):
    return x*y
    
print(add(x,y))
print(multiply(x,y))

#Chapter 3: Advanced Data Structures and Exception Handling

tupleTest = ("Python", 69, "Cool", True)
print(tupleTest)
print(int(True),int(False))

dictionarySample = {
    'name':'Alice',
    'age':30,
    'employed':True
}

print(dictionarySample["name"])
print(type(dictionarySample))

setSample = { 'apple','banana', 'orange','lemon' }
print(setSample)

def divide(x: float, y: float) -> float:
    #error handling
    try:
        return x / y
    except ZeroDivisionError: 
        print("can't divide by zero")

print(divide(10,0))
print(divide(10,1))
    
#Create a dictionary that maps your favorite things to a list of your top three of each.
exerciseDictionary = {
    "Games": ["Star Citizen","Squad","Sea of Thieves"],
    "Food": ["Ramen","pizza","bread"],
    "Films": ["Watchmen","Ghost in the Shell","SomethingSomethingIDK"]
    }
    
listSample = [10,1350,3,246,43,3,2,2,3,4,5,1]

def convertToSet(x: list) -> set:
    return set(x)
    
convertedList = convertToSet(listSample)

print(listSample)
print(convertedList)

#Chapter 4: File I/O and Modules

#create a new file and write in it
with open("example.txt", "w") as f:
    f.write("Hello, World!")

#read from file
with open("example.txt", "r") as f: 
    print(f.read())
    
#packages
#import requests

#response = requests.get("https://www.example.com")
#print(response.status_code)


with open("testFile.txt", "w") as file:
    file.write("this is a sample text\nNew line to see if it works")
with open("testFile.txt", "r") as file:
    print(file.read())


#Chapter 5: Object-Oriented Programming in Python

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"hello, my name is {self.name} and i'm {self.age}.")

p = Person("Johnny", 30)
p.greet()

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def introduce(self):
        super().greet()
        print(f"I'm in grade {self.grade}")
        
s = Student("James", 23, 12)
s.introduce()

#Exercises

#Create a Car class with properties like brand, model, and year, and methods to perform operations like start and stop.
#Create an object of your Car class and call its methods.
#Create a Tesla class that inherits from your Car class. Add an additional property like autopilot and an additional method to activate it.

class Car:
    def __init__(self, brand, model, year, isOn):
        self.brand = brand
        self.model = model
        self.year = year
        self.isOn = isOn
    
    def start(self):
        isOn = True
        
    def stop(self):
        isOn = False
        
class Tesla(Car):
    def __init__(self, brand, model, year, isOn, autopilot):
        super().__init__(brand, model, year, isOn)
        self.autopilot = autopilot
    
    def toggleAutopilot(self):
        if self.autopilot == True:
            self.autopilot = False
        else:
            self.autopilot = True

tesla = Tesla("Tesla", "Model Y", 2023, False, False)
print(tesla.toggleAutopilot())

#Chapter 6: Python Standard Library, APIs and Databases
import math
print(math.sqrt(16))

import datetime
now = datetime.datetime.now()
print(now)

#import requests
#response = requests.get('https://jsonplaceholder.typicode.com/posts')
#for post in posts[:5]: #only the first 5
    #print(post['title'])

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS stocks")

c.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')

c.execute("INSERT INTO stocks VALUES ('2023-07-03','BUY','RHAT',100,35.14)")

conn.commit()
conn.close()

#Exercises

#Use the math module to calculate the factorial of a number.
math.factorial(5)

#Use the datetime module to get the current date and time and format it in the ‘YYYY-MM-DD HH:MM:SS’ format.
formattedTime = now.strftime('%Y-%m-%d %H:%M:%S')
print(f"{formattedTime}")

#Use the requests module to fetch data from ‘https://jsonplaceholder.typicode.com/posts’ and print the title of each post.

#import requests
#response = requests.get('https://jsonplaceholder.typicode.com/posts')
#for post in posts:
    #print(post['title'])

#Create an SQLite database, create a table named ‘employees’ with fields for ‘name’, ‘position’, and ‘salary’, then insert some rows of data.
db = sqlite3.connect('sample.db')
curse = db.cursor()
curse.execute("DROP TABLE IF EXISTS employees")
db.commit
#using example.db and cursor object
curse.execute('''CREATE TABLE employees(name text, position text, salary real)''')
curse.execute("INSERT INTO employees VALUES('John Doe', 'Salesman', 30000)")
db.commit

curse.execute("SELECT * FROM employees")
results = curse.fetchall()

for row in results:
    print(row)
    
# Chapter 7: Data Analysis with Python

import numpy as np 

a = np.array([1,2,3])
print(a)

import panda as pd 

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 32, 37],
    'City': ['New York', 'Los Angeles', 'London']
}
df = pd.DataFrame(data)

print(df)

import matplotlib.pyplot as plt 
x1 = [1,2,3,4,5]
y1 = [2,3,5,7,11]

plt = plot(x1,y1)
plt.show

# Exercises

# Create a NumPy array of 10 numbers and print the mean, median, and standard deviation.
testArray = [0,1,2,3,4,5,6,7,8,9]
print(mean(testArray))
print(median(testArray))
print(deviation(testArray))

# Create a line graph using Matplotlib. The x-axis should be a list of integers from 1 to 10, and the y-axis should be the squares of those integers.
x = [1,2,3,4,5,6,7,8,9,10]
y = [n ** 2 for n in x]
plt = plot(x,y)
plt.show

# Create a pandas DataFrame from a dictionary of lists, each containing 5 elements.
sampleData = {
    ['bob','jim','paul'] : ['dev', 'prj man', 'devops']
}
frame = pd.DataFrame(sampleData)