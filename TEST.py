# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:38:12 2018

@author: mm17do
"""

import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.columny - agents_row_b.columny)**2) + 
    ((agents_row_a.columnx - agents_row_b.columnx)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(1,2))

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].movement()

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].columny, agents[i].columnx)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)