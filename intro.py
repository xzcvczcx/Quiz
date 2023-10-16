
# Introduction welcome user to quiz and tell them what it is
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
  print("Please answer the question with Yes or No")

def intro ():
  print("     Welcome to De Quiz     " )
