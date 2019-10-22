from sys import stdin

lst=[]
lst1=[]
lst2=[]
ww=0
ss1=[]
while True:
    m=stdin.readline().strip()
    if len(m)==0:
        break
    lst.append(m)
#print(lst)
for i in lst:
    ss=[ch for ch in i]
    print(ss)
    ww=ww+len(ss)
    print(ww)
    ss1.append(ss)
    lst1.append(len(ss))
    ss=[]
print(ss1)
print(lst1)

rr=ww//len(lst)
for i in range(len(lst1)):
    if(lst1[i]==rr):
        s=""
        s=s.join(ss1[i])
        lst2.append(s)
s1=""
s1=s1.join(lst2)
print(s1)
