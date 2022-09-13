loop = int(input())
for n in range(0, loop):
    input1 = ([input()])
    list1 = (input1[0]).split()
    num1 = int(list1[0])
    num2 = int(list1[1])
    if num1> num2:
        print('SECOND')
    elif num2> num1:
        print('FIRST')
    else:
        print('ANY')


"""
The above code works by splitting the input string into a list of strings and then converting each element to an integer.
The code then checks if num1 is greater than num2, if it is, it prints SECOND, if not, it checks if num2 is greater than num1,
if it is, it prints FIRST, otherwise it prints ANY.

"""