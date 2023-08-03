units = int(input("enter your units: "))
total = 0
while units>0:
    if units > 250:
        total += (units - 250) * 8
        print("total charge is greater than 250 ",total)
        units=250
        #continue
    elif 151 <= units <= 250:
        total += (units-150)*5
        print("total charge is less than  250 ",total)
        units=150
        #continue
    elif 51 <= units <= 150:
        total += (units-50)*3
        print("total charge is less than 150 ",total)
        units = 50
        #continue
    else:
        total += units*2
        units=0
        #break
    
    print("total charge is from while loop: ", total)


surcharge = total*20/100
print("your surcharge is: ",surcharge)
bill_total = total+surcharge
print("your total bill is: ",bill_total)

