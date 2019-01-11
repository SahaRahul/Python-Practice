# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 22:33:09 2019

@author: rahul
"""

def add(x, y):
    z = x + y
    return z

def subt(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z


while True:
    
    print("\nSelect an option for operation : ")
    print("1 - Addition (x + y)")
    print("2 - Substract (x - y) ")
    print("3 - Multiply (x * y) ")
    print("0 - Exit")
    
    opt_list = list((0,1,2,3))
    
    option = int(input())
    if option in opt_list:
        if option == 1:

            print("Enter value of X = ")
            x = float(input())
            print("Enter value of Y = ")
            y = float(input())
    
            result = add(x,y)
            print("\nResult = " + str(result))
        elif option == 2:
            
            print("Enter value of X = ")
            x = float(input())
            print("Enter value of Y = ")
            y = float(input())
 
            result = subt(x,y)
            print("\nResult = " + str(result))
        elif option == 3:
            
            print("Enter value of X = ")
            x = float(input())
            print("Enter value of Y = ")
            y = float(input())
 
            result = multiply(x,y)
            print("\nResult = " + str(result))
        else:
            print("\nThank You")
            break
    else:
        print("\nEnter a valid option between 0, 1, 2, 3")
        continue
        