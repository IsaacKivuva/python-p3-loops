#!/usr/bin/env python3

def happy_new_year():
    counter = 11
    while counter > 1:
        counter -=1
        print(counter)
        
    print("Happy New Year!")

def square_integers(int_list):
    squared = [num **2 for num in int_list]
        
    return squared
    
    
  

def fizzbuzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print ("FizzBuzz")
        elif i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        else:
            print (i)