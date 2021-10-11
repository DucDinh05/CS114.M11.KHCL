N = int(input())

def luythua(a,n):
    s = 1
    for i in range(0,n):
        s = s*a
    return s

m = str(N)
k = len(str(N))
M = int(0)

for i in m:
   M = M + luythua(int(i),k)
if N == M:
    print("True")
else:
    print("False")

