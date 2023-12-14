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
import requests

response = requests.get("https://www.example.com")
print(response.status_code)
