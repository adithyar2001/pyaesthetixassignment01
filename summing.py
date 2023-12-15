number = int(input("enter the number:"))
value = number
sum=0
while number > 0:
    sum +=number
    print(number)
    number-=1
    
print("sum of first",value, "numbers:",sum)