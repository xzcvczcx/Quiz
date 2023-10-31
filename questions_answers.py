from random import randint

# Number checker function
def num_check (question):
  error = "Please enter a whole number \n"

  valid = False
  while not valid:
    try:
      # Ask question:
      response = int(input(question))
      return response

    except ValueError:
      print(error)

while True:
  num1 = randint(1,10)
  num2 = randint(1,10)
  product = num1 * num2
  response = num_check(f'What is {num1} x {num2}? = ')
  if response == product:
    print("Correct! \n")
  else:
    print("Incorrect.. \n")