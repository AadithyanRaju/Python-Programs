for i in range(int(input())):
    n=int(input())
    s=input()[:n]
    a,b,c=s.count('0'),s.count('1'),s.count('?')
    while(c>0):
        if(a>b):
            s=s[:s.find('?')]+'1'+s[s.find('?')+1:]
            b+=1
            c-=1
        else:
            s=s[:s.find('?')]+'0'+s[s.find('?')+1:]
            a+=1
            c-=1
    print(s)