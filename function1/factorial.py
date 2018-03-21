
#a=n
def fact(n):
    if n<0:
        print("factorial does not exist for -ve numbers")
        print("plese give the another value")

    elif n==0:
        print("the factorial of 0 is always 1")

    else:
        for i in range(1,n):
            n=n*i
        return n

a=int(input("Enter a number"))
if a>0:
    #print("factorial no ",a,"is:",n)
    print("factorial no ", a, "is", fact(a))
