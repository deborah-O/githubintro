# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:15:47 2018

@author: mm17do
"""

import random

class Agent:
    
    def __init__(self, columny, columnx):
        self.columny = columny
        self.columnx = columnx
    
    def randomstart(self):
        '''To ensure agents begin at random points'''
        self.columny = self.columny(random.randint(0,99))
        self.columnx = self.columnx(random.randint (0,99))

    def movement(self):
        '''To ensure agents move randomly'''
        if random.random( ) <0.5:
            self.columny = (self.columny + 1) % 100
        else:
            self.columny = (self.columny - 1) % 100
        if random.random( ) <0.5:
            self.columnx = (self.columnx + 1) % 100
        else:
            self.columnx = (self.columnx - 1) % 100
        
a = Agent(1,2)
print(a.columny, a.columnx)

a.movement()
print(a.columny, a.columnx)

