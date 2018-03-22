

def upside(a):
    count=0
    count1=0
    for i in range(len(a)):
        if a[i].isupper():
            count +=1
            #print(count)


        elif a[i].islower():
            count1 +=1
            #print(count1)

        else:
            pass
    print("original string",a)
    print("No of upper case character:" , count)
    print("No of lower case character: " , count1)


word=input("Enter a string")
#print(a)
#n=a
upside(word)
#print(count)
#print(count1)
