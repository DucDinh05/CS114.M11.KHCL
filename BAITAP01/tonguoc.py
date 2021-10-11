n = int(input())
tongUoc = 0
for i in range(1,int(n/2)+1):
    if n%i == 0:
        tongUoc = tongUoc + i
print(tongUoc)
