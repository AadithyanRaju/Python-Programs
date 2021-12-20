for _ in range(int(input())):
    c1=int(input())
    c2=int(input())
    if c1%2==0:
        if c2%2==0 or c1>1:
            print('Yes')
    else:
        print('No')