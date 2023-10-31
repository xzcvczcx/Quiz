from random import randint

error = "Please enter a whole number"

while True:
  num1 = randint(1,10)
  num2 = randint(1,10)
  product = num1 * num2
  response = int(input(f'What is {num1} x {num2}? = '))

  if not response:
    print(error)
  
  ans = int(response)
  print('Correct! \n' if ans == product else 'Incorrect... \n')