# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:15:48 2024

@author: shahinur
@description: This is an example of linked List in Python
"""

#Creating a Node Class containing data and the infotmation about the next node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#Creating a Linked List Class for different operations        
class LinkedList:
    def __init__(self):
        self.head=None #Initializeing the first node in the list as none
    
    #Add a new node at the end of the list
    def append(self,data):
        new_node=Node(data)
        if self.head==None: #If the list is empty, make new node the head
            self.head=new_node
        else:
            last=self.head
            while last.next:    #Traverse till the last node
                last=last.next
            last.next=new_node      #Link the last node to the new node
            
            
            
            
lList=LinkedList()

lList.append(10)
lList.append(20)
lList.append(30)