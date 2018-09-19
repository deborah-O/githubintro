# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:53:31 2018

@author: mm17do
"""
import csv
import matplotlib.pyplot

environment = []
    
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader:	
    rowlist = []
    for value in row:				
        rowlist.append(value)
    environment.append(rowlist)
         				

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
