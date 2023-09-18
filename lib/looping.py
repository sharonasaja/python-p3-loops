#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
     countdown = 10
     while countdown > 0:
        print(countdown)
        countdown -= 1
    
     print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    #  Create an empty list to store squared elements
     squared_list = []  
    #  iterate through the interger list and Square each element and append to the new list
     for num in int_list:
        squared_list.append(num ** 2)  
    
     return squared_list
     

def fizzbuzz():
    # code goes here!fizzbuzz()
    # iterate through the numbers 1 to 101 for each number, it checks whether it's a multiple of 3 and/or 5  
     for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    
