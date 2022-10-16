for n in range(int(input())):
    cab1, cab2 = list(map(int, input().split()))
    if cab1> cab2:
        print('SECOND')
    elif cab2> cab1:
        print('FIRST')
    else:
        print('ANY')
