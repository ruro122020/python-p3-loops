#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 0
    while i <= 10:
        print(i)
        i += 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # code goes here!
    return [i * i for i in int_list]

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz") 
        elif i % 5 == 0:
            print('Buzz') 
        elif i % 3 == 0:
            print('Fizz') 
        else:
            print(i)
    pass

