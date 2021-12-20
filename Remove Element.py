for _ in ' '*int(input()):
    n,k=map(int,input().split())
    an=[int(x) for x in input().split()][:n]
    an.sort()
    if (n==1):print("YES")
    else:
        i,c=1,0
        while(i<n):
            if an[i]+an[0]<=k:c+=1
            i+=1
        if c==n-1:print('YES')
        else:print('NO')