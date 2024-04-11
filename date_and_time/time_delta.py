# Q. Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:
    # Day dd Mon yyyy hh:mm:ss +xxxx
    # Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
    # Input Format
    # The first line contains T, the number of testcases.
    # Each testcase contains 2 lines, representing time t1 and time t2.
    
    
import os    
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_format = "%a %d %b %Y %X %z"
    date_1 = datetime.strptime(t1, date_format)
    date_2 = datetime.strptime(t2, date_format)
    return str(abs(int((date_2.timestamp()-date_1.timestamp()))))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
