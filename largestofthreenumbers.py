a =int(input("enter first number:"))
b =int(input("enter second number:"))
c =int(input("enter third number:"))

print("numbers:",a,"," ,b ,",",c)
if a>b and a>c:
    print(a," is the largest number.")
elif b>a and b>c:
    print(b," is the largest number.")
else:
    print(c," is the largest number.")