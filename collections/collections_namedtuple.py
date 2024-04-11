# Q. Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
    # Your task is to help Dr. Wesley calculate the average marks of the students.
    # Note:
    # 1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
    # 2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

    # Input Format

    # The first line contains an integer N, the total number of students.
    # The second line contains the names of the columns in any order.
    # The next N lines contains the marks, IDs, name and class, under their respective column names.
    
from collections import namedtuple

n = int(input())
f = input().split()
student = namedtuple('student', f)

marks = 0
for i in range(n):
    marks += int(student(*input().split()).MARKS)
    
num= marks/n
print(f"{num:.2f}")



# Another way

from collections import namedtuple

n = int(input())
f = input().split()
student = namedtuple('student', f)

marks = []
for i in range(n):
    b = student(*input().split()).MARKS
    marks.append(int(b))

num= sum(marks)/n
print(f"{num:.2f}")
