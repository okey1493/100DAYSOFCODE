print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("you are qualified to ride the rollercoaster")
  age = int(input("what is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7")
  elif age >= 45 and age <=55:
    print("You can have a free ride. This is on the house")
  else:
    bill = 12
    print("Adult tickets are $12")
  
  wants_photo = input("would you like to take a photo? Y or N. ")
  if wants_photo == "Y":
     bill += 3
  print(f"your total bill is ${bill} ")
  
else:
  print("you need to grow some height so come back later '-' ")
