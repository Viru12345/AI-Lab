age= int(input("Enter age: "))
if age<=12:
    print("child")
elif age>12 and age<=17:
    print("teenager")
elif age>=18 and age<65:
    print("Adults")
else:
    print("older adults")
