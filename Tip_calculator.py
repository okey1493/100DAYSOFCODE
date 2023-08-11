total_bill = float(input("What was the total bill? $"))
tip_perc = input("how much percentage bill will you want to give? 10, 12 or 15? ")
tip__perc = float(tip_perc)
a = (tip__perc/100)
tip = a * float(total_bill)
print(tip)
total_bill_tip = 150 + tip
print(total_bill_tip)
people = float(input("how many people split the bill? "))
each_person = total_bill_tip / people

per_person ="{:.2f}".format(each_person)
print(f"each person should pay: ${per_person}")
