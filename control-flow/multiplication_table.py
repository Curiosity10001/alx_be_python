#variable input 
number = float (input("Enter a number to see its multiplication table:"))

#For loop to get the multipllication table up to 10
for i in range(1,6):
    multiplication = number * i
    print (f"{number}*{i}={multiplication}")
