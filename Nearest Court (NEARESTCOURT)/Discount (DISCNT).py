import math

test_cases = int(input())

for n in range(test_cases):
    input_string = [input()]
    input_list = input_string[0].split()
    input_list = list(map(int, input_list))
    input_list.sort(reverse= True)
    x = int(input_list[0])
    y = int(input_list[1])
    
    diff = y - x
    if diff%2 == 0:
        print(int((diff/2)*(-1)))
    else:
        div = diff/2
        out = int((math.ceil(div) - 1)*(-1))
        print(out)

"""
The above code works by first sorting the input list in descending order.
Then, we find the difference between the two numbers and divide it by 2.
If the difference is even, then we simply print the result of dividing the
difference by 2. If the difference is odd, then we need to round up the
division and subtract 1 from the result.
"""