#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
user_input = input("How many terms of the Fibonacci sequence do you want?: ") 
# Validate that the input is a positive integer.
if int(user_input) > 0:
  n = int(user_input)
  print("Fibonacci Sequence: ".format(user_input))
else:
  print("Invalid! Please enter a valid integer")
# Use a for loop to print the Fibonacci sequence up to that many terms.
a, b = 0,1
for i in range(n):
  print(a,b)
  a, b = b, a + b
