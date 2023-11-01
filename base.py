# functions

def yes_no (question):
  valid = False
  while not valid:
     response = input(question).lower()

     if response == "yes" or response == "y":
         response = "yes"
         return response

     elif response == "no" or response == "n":
         response = "no"
         return response

     else:
         print("Please answer the question with Yes or No \n")

# Introduction welcome user to quiz and tell them what it is

from random import randint

# Number checker function
def num_check (question):
  error = "Please enter a whole number"

  valid = False
  while not valid:
    try:
      # Ask question:
      response = int(input(question))
      return response

    except ValueError:
      print(error)
# Tell user what quiz is
def instruction():
  print()
  print("Welcome to a Mathematic quiz :D ")
  print("""In this quiz you will be tested with 21 questions
about times tables questions, 
varying from 1x - 10x tables-tables.

- You will have a life score of 2:

>(1 life score will be taken off upon answering a question incorrect )

> (The goal is to complete all 21 questions without losing a life score)
""")
# Main Routine

played_before = yes_no ("Have you tried this quiz before?: ")

print("You chose {}".format(played_before))

if played_before == "no":
  instruction()

print()
print("Beginning Quiz.... \n")

while True:
  num1 = randint(1,10)
  num2 = randint(1,10)
  product = num1 * num2
  response = num_check(f'What is {num1} x {num2}? = ')
  if response == product:
    print("Correct!")
  else:
    print("Incorrect..")