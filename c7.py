num = int(input("enter two digit number: "))
t = num // 10  # t for tens digit
o = num % 10   # o for ones digit
if (t+o==7) and (t ==7 or o ==7) and (num%7==0):
    print("This is a special num ")
else:
    print("this is just a normal num ")