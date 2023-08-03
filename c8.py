name = input("enter your name: ")

if name[:3]== "nxt":
    print("first 3 letters are nxt")
#s=0
for i in name[3:]:
    if i.isdigit():
        print("digits in this string are: ",int(i))
        #print("digit value",i.isdigit())
        if int(i) % 2 == 0 or int(i) % 7 == 0:
            #print("number is divisible by 2 or 7 ")
            print("This is a special number ")
        else:
            print("non divisible by 2 or 7 ")








"""s1 = []
for i in name:
    s=i.isdigit()
    if s=="true":
        print("there is a integer in name ",i)

    ##s1.append(s)
    #print(s)
    #if  int in (name3:))"""