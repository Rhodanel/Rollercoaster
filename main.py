print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("you can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age <= 12:
    print("Please pay $10")
  elif age <= 18:
    print("Please pay $15")
  elif age >= 60:
    print("Please pay $15")
  else:
    print("Please pay $20")
else:
  print("sorry, you have to grow taller before you can ride")
