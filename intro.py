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

def instruction():
  print()
  print("Welcome to a Mathematic quiz :D ")
  print("""In this quiz you will be tested with 21 questions
about times tables questions, 
varying from 1x - 10x tables-tables.
  
- You will have a life score of 2:

>(1 life score will be taken off upon answering a question incorrect )
  
> (You will recieve a point the aim is to get 21 points)""")

# Main Routine

played_before = yes_no ("Have you tried this quiz before?: ")

print("You chose {}".format(played_before))

if played_before == "no":
  instruction()