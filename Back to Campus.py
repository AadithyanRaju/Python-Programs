for _ in range(int(input())):
    k,n=map(int,input().split())
    c=0
    while k>=n:
        c+=1
        k-=n
    print(c)