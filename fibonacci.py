#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
user_input = input("User input: ")

if user_input.isdigit():
  m = int(user_input)
# Validate that the input is a positive integer
  if m > 0:
    a = 0
    b = 1
    print()
    print("Expected Outcome:", end = " ")
# Use a for loop to print the Fibonacci sequence up to that many terms.
    for i in range(m):
      print(a, end = " ")
      a, b = b, a + b
  else:
      print("Please enter a positive integer.")
else:
      print("Please enter a positive integer.")

      
      
