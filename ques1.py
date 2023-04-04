m=int(input(" Enter the month  "))
d=int(input(" Enter the day  "))
y=int(input(" Enter the year  "))
f=1
if m > 0 and m<=12:
    d=1
else:
    f=0
if d> 0 and d<=31:
    d=1
else:
    d=0
if y >0 and y <=99:
    f=1
else:
    f=0

if f ==0:
    print("invalid")   
else: 
    print("Success: Congratulations! you entered the correct date.")
    print("the date is",m,"/",d,"/",y)

