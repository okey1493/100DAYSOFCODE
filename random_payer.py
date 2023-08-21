#how to use split fxn
# items = "okey, obi, ngo, ada, too, chike"
# names = items.split(", ")

# print(names)


import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_of_payers = len(names)
num_random_payer = random.randint(0, num_of_payers - 1)

print(num_random_payer)
payer = names[num_random_payer]

print(payer + "is going to buy the meal today")
