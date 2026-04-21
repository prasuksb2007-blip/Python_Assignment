num = int(input("Enter a number: "))
i = 2
while i < num:
    if num % i == 0:
        print("Not a Prime Number")
        break
    i += 1
else:
    if num > 1:
        print("Prime Number")
    else:
        print("Not a Prime Number")