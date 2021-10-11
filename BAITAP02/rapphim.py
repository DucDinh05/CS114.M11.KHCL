"""
 S=m*n
 canh a
int(m/a)* int(n/a)
 """
n,m,a = map(int, input().split())

if(m/a >int(m/a)):
    dai=int(m/a) +1
else:
    dai= int(m/a)
if(n/a >int(n/a)):
    rong = int(n/a) +1
else:
    rong = int(n/a)
print(dai*rong)
