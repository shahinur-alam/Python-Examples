'''
This is an example of Python recursion function
'''

def factorial(n):
        if n==1:
            return 1
        else:
            return(n*factorial(n-1))
    
print("Please input an integer number to calculate factorial")
number=int(input())
print(factorial(number))
