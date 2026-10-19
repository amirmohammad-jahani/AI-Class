age = int(input("Enter age : "))
day = input("Enter day : ")

price = 0

if age < 5:
    price = 0
elif age < 12:
    price = 50000
elif age < 60:
    price = 100000
else:
    price = 60000


if day == "tuesday":
    price = price * 0.8
    
print(f"your ticket is {price}")