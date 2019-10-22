lst=[]
lst1=[]


for i in range(4):
    n=input()
    ss=[ch for ch in n]
    lst.append(ss)
    lst1.append(lst)
    ss=[]




m=input()
ss1=[ch for ch in m]
rr=ss1[0]
out = [(ind,ind2) for ind,i in enumerate(lst) 
                  for ind2,y in enumerate(i) if y == rr]
if(len(out)>1):
    out1=out[0]
print(out1)
