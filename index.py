#!bin/bash

#Returns sum of numbers
def add_numbers(num1, num2):
    return num1 + num2

#returns True if the number is even, and False otherwise
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

#Reverses a string
def reverse_string(text):
    return text[::-1]

#Returns count of vowels in a string
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text if char in vowels)

#calculates factorial
def calculate_factorial(n):
    if n == 0:
        return 1;
    else:
        return n * calculate_factorial(n-1);

def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

#apply decorator
def apply_decorator(func):
    return decorator_func(func)

#sort by age tuples
def sort_by_age(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

#Merge Dictionaries
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
            return merged_dict

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")
