n=int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i ," is even")
    else:
        print(i ,"is odd")
    if i%2==0 or i%3==0:
        print(i ,"is comp")
    else:
        print(i,"is not comp")
