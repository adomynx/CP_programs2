t=int(input("Enter no of test cases"))
for i in range(t):
    print()
    n=int(input())
    lst=[]
    lst2=[]
    for i in range(n):
        x=int(input())
        lst.append(x)
        lst2.append(x)

    lst2.sort()
    A=lst2[0]
    B=lst2[1]
    b=lst2[len(lst2)-2]
    a=lst2[len(lst2)-1]
    if(2*A+b+a<A+2*B+a):
        print(2*A+b+a+B)
        print(A," ",a)
        print(A)
        print(A," ",b)
        print(A)
        print(A," ",B)
    else:
        print(3 * B + A + a)
        print(A, " ", B)
        print(A)
        print(b, " ", a)
        print(B)
        print(A, " ", B)
