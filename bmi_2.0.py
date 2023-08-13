height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height ** 2 

if bmi < 18.5:
   print(f"your bmi is {bmi}, you are UNDERWEIGHT")
elif bmi < 25:
    print(f"your bmi is {bmi}, you have a NORMAL WEIGHT")
elif bmi < 30:
     print(f"your bmi is {bmi}, you are SLIGHTLY OVERWEIGHT")
elif bmi < 35:
     print(f"your bmi is {bmi}, you are OBESE")
else:
     print(f"your bmi is {bmi}, you are CLINICALLY OBESE")
