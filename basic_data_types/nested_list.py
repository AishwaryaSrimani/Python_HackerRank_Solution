# Q. Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
    # Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# with Pandas library

import pandas as pd

nest = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    nest.append([name, score])

x = pd.DataFrame(nest)
df = x[1].idxmin()

x.drop(df, inplace=True)

min_value_b = x[1].min()
result = x.loc[x[1] == min_value_b, 0]

a = result.values.tolist()
a.sort()
for i in a:
    print(i)
    


# without pandas library

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
     
scores = set([student[1] for student in students])
_2nd_lowest = sorted(scores)[1]

students_2nd_lowest = [student[0] for student in students if student[1] == _2nd_lowest]

students_2nd_lowest.sort()

for name in students_2nd_lowest:
    print(name)
