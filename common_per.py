"""from collections import Counter

def common_permutation(a, b):
    return ''.join(k * v for k, v in sorted((Counter(a) & Counter(b)).items()))

print( common_permutation('pretty', 'women'))
print( common_permutation('walking', 'down'))
print(common_permutation('the', 'street'))
#print common_permutation('aaabbbbccdddddd', 'bbdddcccaaaaaaadd')
#print common_permutation('bbdddcccaaaaaaadd','aaabbbbccdddddd')"""

from itertools import permutations  


n=input()
m=input()
lst=[]
ss=[ch for ch in n]
ss1=[ch for ch in m]
perm = permutations(ss) 




#for i in list(perm): 
        #print (i) 
perm1 = permutations(ss1)

 
#for i in list(perm1): 
        #print (i) 


for i in range(len(ss)):
    for j in range(len(ss1)):
        if(ss[i]==ss1[j]):
            lst.append(ss[i])


print(''.join(sorted(set(lst))))
