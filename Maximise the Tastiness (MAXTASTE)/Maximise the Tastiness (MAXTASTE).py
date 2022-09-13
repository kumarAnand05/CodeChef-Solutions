test_case = int(input())
for n in range(test_case):
    input1 = [(input())]
    ingredient_list = input1[0].split()
    ingredient_list = list(map(int, ingredient_list))
    
    sum = 0
    # choice1
    if ingredient_list[0] > ingredient_list [1]:
        sum += ingredient_list[0]
    else:
        sum += ingredient_list[1]
        
    # choice2
    if ingredient_list[2] > ingredient_list [3]:
        sum += ingredient_list[2]
    else:
        sum += ingredient_list[3]
    print(sum)

"""
The above code works by taking the input and splitting it into a list of strings.
Then we convert each string to an integer and add them together.
"""