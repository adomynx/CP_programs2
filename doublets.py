s = input()
st = ' '
while True:
    if s:
        lst=[]
        lst.append(s)
        st = input()
        while True:
            if st:
                lst.append(st)
                st = input()
            else:
                break
        count = 0
        fin = [lst[0]]
        k = 0
        for i in lst:
            count = 0
            for j,m in zip(i,fin[k]):
                if j!=m:
                    count += 1
            if count==1:
                fin.append(i)
                k = k+1
            print(fin)
        if len(fin)<2:
            print("No Solution")
        else:
            for i in fin:
                print(i)
        s = input()
    else:
        break
