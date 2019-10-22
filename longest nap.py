from operator import mul


n=int(input())
lst=[]
lst2=[]
lst4=[]
for i in range(n):
    lst1=[str(i) for i in input().split()][:50]
    #r=m.split()
    #ss=m.replace(':',',')
    lst.append(lst1[0])
    lst.append(lst1[1])
    #print(lst1)    


    
#print(lst)
for i in lst:
    my_time=i
    fact=(60,1)
    t1=sum(i*j for i,j in zip(map(int,my_time.split(':')),fact))
    lst2.append(t1)
#print(lst2)
rr=len(lst2)
even_pos=lst2[2:rr:2]
odd_pos=lst2[1:rr-1:2]
#print(even_pos)
#print(odd_pos)
for i,j in zip(even_pos,odd_pos):
    if(lst2[-1]!=1080):
        if(i!=j):
            diff=i-j
            diff1=1080-lst2[-1]
            lst4.append(diff)
lst4.append(diff1)
            #time_slot_start=lst[i]
maximum_time=max(lst4)
print('Longest nap will last for',maximum_time,'minutes')
#print(int(lst[0][1])-int(lst[1][0]))
