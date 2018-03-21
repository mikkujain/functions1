n=int(input("How many number u wnat to insert"))
list1=[]
#sum=0
def sum1(x):
    for i in range(n):
        x=int(input("which number u want to insert"))
        list1.append(x)
sum1(n)
print(list1)
print(sum(list1))
