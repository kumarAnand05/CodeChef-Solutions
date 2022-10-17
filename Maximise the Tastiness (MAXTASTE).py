for n in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    out = 0
    
    # choice1
    if a > b:
        out+= a
    else:
        out+= b
        
    # choice2
    if c > d:
        out+= c
    else:
        out+= d
    print(out)
