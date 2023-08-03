
amount = int(input("enter your amount: "))
remain = 0
while amount>0:
    if amount/500 >=1:
        numOfNotes=amount//500
        remain=amount-numOfNotes*500
        print("500 notes required: ",numOfNotes)
        amount=remain
    elif amount/50>=1:
        numOfNotes=amount//50
        remain=amount-numOfNotes*50
        print("50 notes required: ",numOfNotes)
        amount = remain
    elif amount/10 >=1:
        numOfNotes=amount//10
        remain=amount-numOfNotes*10
        print("10 notes required: ",numOfNotes)
        amount = remain
    else:
        print("remaining change is:",amount)
        amount=0




