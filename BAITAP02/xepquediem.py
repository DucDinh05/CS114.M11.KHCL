""" 
n que diem
PTD: 1 + 1 =2
mua them k 
q so testcase

input: q, n
output: k
"""
q = int(input())

for i in range(q):
    n = int(input())
    if(n==2):
        print(2)
    else:
        print(n%2)