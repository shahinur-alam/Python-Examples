# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:57:12 2024

@author: shahinur
@description: This is an example of stack in Python
"""

#This is a stack implementation using append() and pop() method

stack_var=[10,20,30]

stack_var.append(40) #push element, Python does not have push method
stack_var.append(50)

print("Stack after appending",stack_var)

stack_var.pop()

print("Stack after pop",stack_var)

stack_var.pop()

print("Stack after pop",stack_var)