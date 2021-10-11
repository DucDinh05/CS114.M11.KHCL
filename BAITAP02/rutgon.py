
#
""" 
a=12
b=16 
r = a%b = 12
a=b=16
b=r=12

r=4
a=12
b=4
"""
n = int(input())
def UCLN (a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

for i in range(n):
    a,b = map(int, input().split())
    ucln = UCLN(a,b)
    if(b//ucln != 1):
        print(a//ucln,' ',b//ucln)
    else:
        print(a//ucln)
 
      