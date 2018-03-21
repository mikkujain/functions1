n=int(input("Enter a number"))
#fact1=0
a=n
def fact(a):
    if a<0:
        print("factorial does not exist for -ve numbers")
        print("plese give the another value")

    elif a==0:
        print("the factorial of 0 is always 1")

    else:
        for i in range(1,n):
            a=a*i

fact(n)
if a>0:
    print("factorial no ",n,"is:",a)
