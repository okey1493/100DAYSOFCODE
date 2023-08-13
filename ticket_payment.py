print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("you are qualified to ride the rollercoaster")
  age = int(input("what is your age"))
  if age < 12:
    print("you have to pay a fee of $5")
  elif age <= 18:
    print("you have to pay a fee of $7")
  elif age >18:
    print("you have to pay a fee of $20")
    
else:
  print("you need to grow some height so come back later '-' ")
