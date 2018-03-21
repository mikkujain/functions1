a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("Enter third number"))
#result1=0
def max1(x,y,z):
    result=0
    if x>y and x>z:
        print("A is greater")
        result=x
    elif y>z:
        print("B IS greater")
        result=y
    else:
        print("C is greater")
        result=z
    print(result)

max1(a,b,c)
#print(result1)
