while True:
    s = input()
    if s:
        co = ''
        fco = ''
        to = ''
        fto = ''
        Input = ''
        lst = []
        for i in range(0,int(s)):
            lst.append(input())
        for i in lst:
            for j in i:
                if j.isdigit():
                    co += j

        fco = ''.join(lst)

        s = int(input())
        lst = []
        for i in range(0, int(s)):
            lst.append(input())
        for i in lst:
            for j in i:
                if j.isdigit():
                    to += j

        fto = ''.join(lst)
        # print(fco,"\n",fto)
        # print(co,"\n",to)
        ac = True
        pe = False
        if to!=co:
            ac = False
        if fco!=fto:
            pe = True
        # print(ac,pe)
        if not ac:
            print("wrong Ans")
        elif ac and pe:
            print("Presentation Error")
        else:
            print("Accepted")


    else:
        break
