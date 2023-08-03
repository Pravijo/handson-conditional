num = int(input("enter your number "))
l=num*num #square root of number
print(l)
n = num%10 #last digit of number
l1 = l%10 #last digit of sq root num
if n==l1:
    print("yes last digit is matching")
else:
    print("no last digit is not matching")