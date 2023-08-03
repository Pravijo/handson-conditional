a = int(input("A score is : "))
b = int(input("B score is: "))
c = a+b
if (a >= 300 or b >= 300) and c < 500:
    print("you can team up ")
else:
    print("you can not team up ")