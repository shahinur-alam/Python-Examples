# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:03:40 2024

@author: shahinur
@description: This is an example of queue in Python
"""

#This is a queue implementation using deque method
from collections import deque

queue_var=deque()

queue_var.append(20)
queue_var.append(30)
queue_var.append(40) #push element, Python does not have push method
queue_var.append(50)

print("queue after appending",queue_var)

queue_var.popleft() #Pop from the left most element

print("queue after pop",queue_var)