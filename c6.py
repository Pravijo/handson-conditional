esal = int(input("employee salary is: "))
eyear = int(input("employee years of experience is: "))
if eyear>=5:
    per = 5/100
    esal1 = esal*per
    print("employee gets bonus ",esal1)
else:
    print("work {} more years to get bonus ".format(5-eyear))