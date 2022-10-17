for n in range(int(input())):
    x,y= list(map(int, input().split()))
    
    diff= abs(x-y)
    if diff%2==0:
        print(diff//2)
    else:
        print((diff+1)//2)
    
