for n in range(int(input())):
    user= input().split()
    sub= int(user[1])-int(user[2])
    print(sub*int(user[0]))

"""
The above code works by taking the input of the number of students and the number of subjects.
Then it takes the marks of each student in each subject and calculates the total marks obtained by the student.
The total marks is then multiplied by the number of subjects and printed.
"""