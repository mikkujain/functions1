def prime(a):
    if a>0:
        for i in range(2,a):
            if a%i==0:
                print("it's not a prime number")
                break

        else:
            print("its a prime number")


number=int(input("Enter a number "))
print("To check it is prime or not",number)
prime(number)
