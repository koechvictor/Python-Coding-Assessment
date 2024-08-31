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
