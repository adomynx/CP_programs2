n=int(input())
lst1=[]
sum1=0
for i in range(n):
    m=int(input())
    
    lst=[int(i) for i in input().split()][:m]
    lst=sorted(lst)
    for j in range(len(lst)-1):
        ss=abs(lst[j]-lst[j+1])
        sum1=sum1+ss
    lst1.append(sum1)
    sum1=0
lst=[]


print(*lst1)
