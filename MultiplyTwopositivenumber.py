def multiply(a,b):
    if b==0:
        return 0
    else:
        return a+multiply(a,b-1)
x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
output=multiply(x,y)
print("The value is : ",output)