#w3school.com this one of the best resources you can use no learn# :)
#- use the testing.py to run your code


#starting out with  python :()#: take note that am also learning python
#We'll start by looking at the basics

#the print method can be used to log messeages in the console//the print method can also be used to debug in python like how we use console.log in javascript 
#- to run this command write = py lesson.py on your command line interface in your ide(code editor)
print('hello world')


#//////////////////////////
#start()
#//////////////////////////
#one of the most important things to do in python is to understand (indentations) according to me, indentation examples below
 # example 1 will not work because it is not following the indentation rules
name = 'mwaba' # this is a variable
if name == 'mwaba':
print('hi and hello')
else:
print('this is not mwaba')

#example 2 will work because it is following the indentation rules
name = 'mwaba'
if name == 'mwaba':
 print('hi and hello')
else:
 print('this is not mwaba')

 #make sure to learn indentation's in python

#//////////////////////////
#(end)
#//////////////////////////
#Variables are containers for storing data values.
text = 'this is an example of a vriable'
#groble variables:these are variables that can be used in and outside a function
balance = 12 # grobal variable

def myFun():
    if balance == 12:
        print('this is my amount')
    else:
        print('this is the wrong amount')

myFun()


#the global keyword allow's you to create a global variable inside a function here is an example
def myfunc2():
    global food
    food = 'rice'
    print('this is food')
myfunc2()

#if your code is not working even after checking on google or you think their is nothing wrong with your code: remember indentation's :)

#///////////////////////////
#(end)
#//////////////////////////
#python data types
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#///////////////////////////
#(end)
#//////////////////////////
#in storing multiple data types in python we use
#list/tuple/set/Dictionary

#List--
list = ['mwaba','john','mary']
 print(list)
#accessing items/items are indexed, the first item has index [0], the second item has index [1] in storing multiple data
 print(list[1])

 #you can also check for Existing Items in your list this way

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#tuple--
mythings = ('apple','laptop','flowers')
# these are anchangeable 


#set--
myset = {"apple", "banana", "cherry"}

#Dictionary--
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#checkout the full lesson on w3school.com
#////////////////////////
#(end)
#///////////////////////
#Looping in python
#for loops
list2 = ['johnny','mable','hope']
for x in list2:
 print(x)

#while loops
i = 1
while i < 6:
 print(i)
 i +=1




#///////////////////////
#(end)
#//////////////////////

#functions/a function in python is defined with the def key word 

def cal(num2):
  num = 5
  sum = num + num2
  print(sum)

cal(5)

#To call a function, use the function name followed by parenthesis
#we also have the lambda function 
#A lambda function can take any number of arguments, but can only have one expression. accouding to w3schools.com

x = lambda a : a + 10
print(x(5))


#///////////////////////
#(end)
#//////////////////////
#classes and objects
#python is an object oriented programming language.Almost everything in Python is an object

class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

p1 = person('alice',16)
print(p1.name)

#//////#
#this is not the end of this python lesson busy busy