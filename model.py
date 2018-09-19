# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 16:05:40 2018

@author: mm17do
"""

y0 = 50
x0 = 50


import random
import operator
import matplotlib.pyplot
import time
import agentframework


num_of_agents = 10
num_of_iterations = 100

random_number = random.random()

if random_number < 0.5:
    y0 = y0 + 1

else:
    y0 = y0 - 1


print (y0)

if random_number < 0.5:
    x0 = x0 + 1
    
else:   
    x0 = x0 -1
    
print (x0)

if random_number < 0.5:
    y0 = y0 + 1

else:
    y0 = y0 - 1


print (y0)

if random_number < 0.5:
    x0 = x0 + 1
    
else:   
    x0 = x0 - 1
    
print (x0)

if random_number < 0.5:
    y0 = y0 + 1

else:
    y0 = y0 - 1


print (y0)

if random_number < 0.5:
    x0 = x0 + 1
    
else:   
    x0 = x0 -1
    
print (x0)











y1 = 50
x1 = 50


random_number = random.random()

if random_number < 0.5:
    y1 = y1 + 1

else:
    y1 = y1 - 1


print (y1)

if random_number < 0.5:
    x1 = x1 + 1
    
else:   
    x1 = x1 - 1
    
print (x1)

if random_number < 0.5:
    y1 = y1 + 1

else:
    y1 = y1 - 1


print (y1)

if random_number < 0.5:
    x1 = x1 + 1
    
else:   
    x1 = x1 - 1
    
print (x1)

if random_number < 0.5:
    y1 = y1 + 1

else:
    y1 = y1 - 1


print (y1)

if random_number < 0.5:
    x1 = x1 + 1
    
else:   
    x1 = x1 - 1
    
print (x1)

dy = y0 - y1
dx = x0 - x1

dy1 = dy**2
dx1 = dx**2

sum = dy1 + dx1

answer = sum**0.5

print("Answer:", answer )

#Multiple-valued variables
#or, containers

# 1) Strings
# 2) Tuples
# 3) Lists 

    
# 1)

#python counts at 0, so to extract a number or charater, a = "rob", print(a),
# print(len(a)) - this gives me values
#in a string
#Access  individual valyes by indexing
#print (a[0], a[1])
#To get the final item in a unknown length, use a[length(a)-1] or a[-1]

# Strings are immutable - can the data be changed after its stored in an object
# i.e., I can't change a single value in it,
# i.e., a[1] = 'a' is not allowed.

# a = 'rob'
# b = 'sturman'
# print(a+b)

#Apostrophes and quotation marks do not have a particular use, 
#they are usually dealt with ..

# c= "Rob's bike"
# d = 'Rob is "awesome"'
# e = "Rob's bike is \"awesome\ ""
# f = ''' Use a whole bunch of quotes '''

# 2) Tuples
    
# q = (1, 2, 3, 4)

#Tuples are also immutible, 
#they are indexed in the same way as strings, 
#therefore to change a value in the tuples, we must REDEFINE the tuple. 

#Brackets are not neccesary in Tuples,  w = 2, 3, 4 works well too
#For an empty Tuple is r = (), just brackets 

# 3) Lists
    
# Defined with square brackets [], k = [5, 6, 7, 8]

#Lists are mutable, e.g. to change k[2] it is = k[2] = 33, changing k to = [5, 6, 33 ...]

# Labels in lists work differently with integers
# a = [1,2,3]
# b = a
# b[0] = 100 - changes BOTH values in lists, so a = [100,2,3]
# Unlike integers that do not change. 

#To make duplicate of list that WILL NOT change, we use Slices

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# A slice is a duplicate, 
# Which is done by, 
# a[:] 

#Sublists - a [2:6] and  a[:4]


# Ranges

# Use range() function

# List(range(0,10,3)) - up in 3's for numbers 0-9
# List(range(0,10,- 3)) - down in 3's for numbers 0-9 
# range() is only for integers 

# () = used in tuples
# [] = in lists 
# {} = in sets 

#q = [[1,2,3],[4,5,6,7,8,9], 3]
#q[1][3], is the second list and the 4th indexed value in the list

# Math elements suchas addition and multplication are not effective in tuples
# a = [1,2,3]
# b = a*2
# b = [1,2,3,1,2,3]

# b = a + (4,)
# b = [1,2,3,4]

#Packing and Unpacking
#To swap values we do a,b = b,a

#2D Sequences
#a = [1...]
#b = [...]
#zip(a,b)

#Sets eliminate duplicates within a list of values or characters  

y0 = random.randint(0,99)

x0 = random.randint(0,99)

start = time.clock()
agents = [] #Creating an empty list 

agents.append([y0,x0]) # Adding coordinates of 2 lists into another list using 
# [] brackets 

print (agents)
#Generate a single random value between 0 and 98
y1 = random.randint (0,99)
x1 = random.randint (0,99)

y2 = random.randint (0,99)
x2 = random.randint (0,99)

y3 = random.randint (0,99)
x3 = random.randint (0,99)

y4 = random.randint (0,99)
x4 = random.randint (0,99)

agent_co_ords = [[y0,x0], [y1,x1], [y2,x2], [y3,x3], [y4,x4]]

print(agent_co_ords)

#To eliminate the need for labels we use the random.radint() command,
#within [] brackets 
agents = []
agents.append([random.randint (0,99), random.randint (0,99)])

#To find the agent furthest from x 
print(max(agents))

#To find the maximum x value we must add an additional arguement to the max
#function, import the operator function
print(max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()

end = time.clock()
print("time = " + str(end - start))

#Functions

# def squared(x):
    # x_squared = x**2
    # return x#_squared
# x is only defined within the function not outside 
# def double_it(z):
    #return 2*z

# def pythagoras(a,b):
    #c_squared = a**2 + b**2
    #return c_squated**0.5, c_squared
    
# def show_me():
    # print ("rob")
    # return None
    
#Numpy arrays

#import numpy as np - I can access all fucntions associated to numpy in an
#abbreviation 

#a = np.array([1,2], [3,4])
#print (a)

#print (np.ndim(a)) - lists in array
#print (np. shape(a)) - 2 or 3 dimensions
#print (np.size(a))
#print (a.min())
#print (a.sum())

#b = np.array(range(20))
#print(b.reshape(4,5))

#c = np.zeros([4,3])
#d = np.ones([2,5])
#e = np.eye(5)

#numpy arrays are mutable, like lists 
#numpy has arange for real numbers, operates like the range() function

#print(np.arange(1.1, 2.5, 0.2))

#To avoid having to manually create numbers we use
#q = np.linspace(1.0, 20.0, 150)
#print(q)

#Slicing for lists, but a bit better 

# a = np.arange(0,15)
# print (a[3:6])
# print (a [12:5:-1])
# b = np.array(range(20))
# b = b.reshape(4,5)
# print(b)

# selecting columns and rows

# b[1][:] - translates to the 2st row
# b[:,1] - translates to the 2nd column 


#Elementwise Operations
#print(np.sin(b)) - elements apply ACROSS WHOLE ARRAY rather than just a single
#value

#Control flow

#if conditions 

#x = 1
#if x<10:
#print ('rob is awesome')

#else:
    # print ('lunchtime')

# elif x<15:
    #print('dinnertime')
# else:
    # print('beer')
    
#while loop

#If a condition is true, while creates a loop

#n = 10
#tr = 0

#while n>0:
    # tr += n
    # n-= 1
#print (tr)

#for i in range(10):
    # print(i**2+i+1)
    
#for _ in range(5):
    #print('rob')

#for a in [4,6,23,7,3]:
    # for b in "rob" :
    # print (a,b)

#Make sure to indent in loops to avoid never ending loops
 
for i in range(num_of_agents):
    agents.append([random.randint (0,99), random.randint (0,99)])

print (agents)

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() <0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
        if random.random() <0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else:
            agents[i][1] = (agents[i][1] - 1) % 100
print(agents)

#Defining the functions
def distance_between(agents_row_a, agents_row_b):
        distance_between = (((agents_row_a[0] - agents_row_b[0])**2) + ((agents_row_a[1] - agents_row_b[1])**2))**0.5
        return distance_between
 
for k in range(num_of_agents):
    for i in range(num_of_agents):
       print(distance_between(agents[k], agents[i]))



#Plotting agents
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range(num_of_agents):
  matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.show()

#Creating the class
 
a = agentframework.Agent(1,2)
print(a.columny, a.columnx)
a.movement()
print(a.columny, a.columnx)


#Classes
# def gcd (a,b):
# r = a%b
# if r==0
#   return b
#else:
#   return gcd(b,r)

#class Rational -creating a class called rational

#   def __init__(self,a,b):- self is the object

        #hcf = gcd(a,b)
        #self.__n = a - numerator/hcf
        #self.__d = b - denominator/hcf

#   def getNumerator(self):
#       return self.__n

#   def getDenominator(self):
#       return self.__d

#   def _mul_(self,rhs):
        
#        a = self.__n * rhs.getNumerator()
#        b = se;f.__d * rhs.getDenominator()
#        return Rational(a,b)

#Object for printing
#   def _repr_(self):
#       str = '%d' % self.__n
#       str = str + '/'
#       str = str + '%d' % self.__d
#       return str 

#Jitse Nieson - j.nieson@leeds.ac.uk (Day 3)

#class Person:
    # def __init__(object, attributes):
    # def __init__(self) - object is always named self
    # Our example, the attributes are Money and Happiness
    
    #def __init__(self, money, happiness):
        #self.money = money
        #self.happiness = happiness
    # To run this, we create our person
    # Debbie = Person(100, 10) - just type Debbie in the console
    #This is not insightful, so we will create a method which are objects.append
    #i.e. numbers = [2, 5, 10]
    #i.e. numbers.append(20) - append adds values or charaters to the list
    
    #To return to our person class, we'll add a method
    # with two assumptions: Working increases money, but happiness reduces
   
    #def work(self):
        #self.money = self.money + 10
        #self.happiness = self.happiness - 5
        
    #Run the class once more
    #Debbie = Person(100, 10) 
    #Two ways of printing now
    #print("Debbie's money:", Debbie.money) -Old way
    #print(f" Debbie's money = {Debbie.money},"
         #(f" Debbie's happiness= {Debbie.happiness},"
           
    # def consume(self):
        #'''Consumption decreases money, increases happiness'''
        #self.happiness += 7
        #self.money -= 8
        #Debbie.consume()
    
    #A new way to represent our class, printing
    #def __repr__(self):
        #return (f"A personn with money = {self.money} "
                #f" and happiness = {self.happiness}" )
        
    #To make things interesting, we will add an interaction between agents
    #def interact(self, other):
        #'''Interact with another person; increases happiness for both'''
        #self.happiness += 1
        #other.happiness += 1
        
    #Create another person to interact with
    #rob.person(500, 5)
    #rob.interact(Debbie)
    #Print('After interaction:')
    #print(Debbie)
    #print(rob)
    
#Input and Output (I/O)

#result = input('Say something') 

#A string and a number(int) cannot not be added together

#To open an external file in python, there are two processes

#my_file = open('hi.txt,'w')
#my_file.write('Oh hello') - the results will simply be count of charaters 
#my_file.close() - to stop writing

#If we do not allovate a specific place to save the document
#it will save in the m drive or default area in searchbar 
#file_for_reading = open('hi.txt', r) - if we dont allocate an command,
#it automatically reads the file

#text_in_file = file_for_reading.read()
#print(text_in_file)
#file_for_readng.close()


#To import a file that we have full of data 
#file_for_reading = open('hi.txt', r)
#text_in_file = file_for_reading.read()
#file_for_readng.close()
#print(text_in_file)


#open files this way, to avoid forgetting to close files ->
# with open('hi.txt', r) as file_for_reading:
      #text_in_file =  file_for_reading.read()
#print(text_in_file) - ensure the file directory is in the same place as program

#To read files line by line
#with open('hi.txt', r) as file_for_reading:
   #for line in file_for_reading:
       #print ('I read a line and it is: ', repr(line))
       
#Split the words
#with open('hi.txt', r) as file_for_reading:
   #for line in file_for_reading:
       #words = line.split()
       #print('I read the line and it is:  ',repr(words))
       
#Construct persons
#with open('hi.txt', r) as file_for_reading:
   #for line in file_for_reading:
       #words = line.split()
       #money = int(words[0])
       #happiness = int(words[1])
       #person = Person(money, happiness)
       #print('I read the line and I created this person:  ',person)
       
#def read_persons_from_file(filename):
    #'''return a list of persons. File should be a text file with two numbers
    #seperated by space on each line'''
    
    #persons = []
        
    #with open(filename, r) as file_for_reading:
        #for line in file_for_reading:
            #words = line.split()
            #money = int(words[0])
            #happiness = int(words[1])
            #person = Person(money, happiness)
            #persons.append(person)
    #return persons
    
#Read data from file and let everybody work
#person_list = read_persons_from_file('agent-data.txt')
#for person in person_list:
    #person.work()


#Also some things that are good about R about reading files
#Are in pandas, simply import it at the beginning of the code

#To read data that is numerical, use numpy with is also imported into the code
#numpy.loadtxt('agent-data.txt')

#To write into the file
#def write_persons_to_file(filename, persons):
    #'''Save a list of Person to file so that it can be read by read_persons_from_file'''
    #with open(filename, w) as file_for_writing:
        #for person in persons:
         #-> we need to make strings to return the values to the file
         #s = f'{person.money} {person.happiness}'
         #file_for_writing.write(s)
    
#write_persons_to_file('workieworkie.txt', person_list\n)

