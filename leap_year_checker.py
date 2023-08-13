
year = int(input("Which year do you want to check? "))
a = year % 4 
b = year % 100
c = year % 400

if a == 0:
    if b == 0:
        if c == 0:
            print("Leap")
        else:
                print("Not Leap")
    else:
        print("leap")

else:
    print("Not Leap")


