s1 = str(input())
s2 = str(input())
def check(s1, s2):
    if(len(s1) != len(s2)):
        return 0
    for i in range(len(s1)):
        if(s2[len(s1)-i-1] != s1[i]):
            return 0
    return 1

if(check(s1,s2) == 0):
    print("NO")
else:
    print("YES") 
