# Q. The National University conducts an examination of N students in X subjects.
    # Your task is to compute the average scores of each student.
    # The first line contains N and X separated by a space.
    # The next X lines contains the space separated marks obtained by students in a particular subject.
    
n, x = list(map(int, input().split()))

marks = []
for i in range(x):
    b = list(map(float, input().split()))
    marks.append(b)

avg = [sum(a)/len(a) for a in zip(*marks)]

for item in avg:
    print(item)