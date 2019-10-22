n=int(input("Enter the no of shoes and penalties"))
shoe=[]
days=[]
penalty=[]
x=[]
for i in range(n):
    a,b=input("Enter values").split(" ")
    shoe.append(int(a))
    days.append(int(b))
    penalty.append(shoe[i]/days[i])
    x.append(shoe[i]/days[i])

penalty.sort()

print(penalty)
print(x)

count=0
i=0
final=[]
for i in range (n):
   a= penalty[i]
   b=x.index(a)
   final.append(b+1)
   x[b]=9999

print(final)        
