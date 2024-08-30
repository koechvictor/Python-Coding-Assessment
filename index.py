#bin/bash

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

#counts vowels in a string
def count_vowels(text):
    vowels = 'aeiou'
    return sum(1 for char in text if char in vowels)
