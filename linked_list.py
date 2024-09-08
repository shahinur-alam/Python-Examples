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
            
            
    #Insert a node at the beginning
    def append_at_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head 
        self.head=new_node
    
    #Display Linked List Items
    def display(self):
        current=self.head
        while current:
            print (current.data, end=" ->")
            current=current.next
        print("None")
        
    def delete(self, key):

        #Deleting the head
        if self.head and self.head.data==key:
            self.head=self.head.next
            return
        
        #if the key is not the first element
        current=self.head
        prev=None
        if current and current.data!=key:
            prev=current
            current=current.next
            
            
        #if the key is not in the list
        if current is None:
            print("Data not in the list")
            return         
         
            
        prev.next=current.next #Unlink the node
            
lList=LinkedList()

lList.append(10)
lList.append(20)
lList.append(30)

lList.append_at_begin(40)

lList.display()

lList.delete(40)

lList.display()

lList.delete(20)

lList.display()