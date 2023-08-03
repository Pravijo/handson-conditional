maths = int(input("enter your marks"))
social = int(input("enter your marks"))
science = int(input("enter your marks"))
total = (maths + social + science)
print("total marks scored: ", total)
if total >= 50:
    print("student passed ")
else:
    print("student failed")