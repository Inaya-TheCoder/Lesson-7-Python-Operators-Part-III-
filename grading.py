a = int(input("Enter your Marks"))
b= int(input("Enter your Marks"))
c = int(input("Enter your Marks"))
tot = a + b + c
avg = tot/3
if avg >= 91 and avg <= 100:
    print ("WOW, I Am IMPRESSED!")
elif avg >= 81 and avg <= 90:
    print ("You DID GREAT!")
else:
    print ("invalid syntax")