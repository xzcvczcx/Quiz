from random import randint

round = 0

score = 2

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

# Game loop + Score count
while True:
  round += 1
  print("Round {}".format(round))
  num1 = randint(1,10)
  num2 = randint(1,10)
  product = num1 * num2
  response = num_check(f'What is {num1} x {num2}? = ')
  if response == product:
    print("Correct!")
  else:
    print("Incorrect..")
    score -=1
  print("Life score: {} \n".format(score))

# End of game when run out of lives
  if score == 0:
    print("you dead L try again never back down never what?""")
    break
    
print("well done you got {} rounds".format(round))