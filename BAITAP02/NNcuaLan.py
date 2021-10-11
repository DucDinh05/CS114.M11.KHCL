""" 
Duoi:
Man adj: -lios
Woman adj: -liala

Man N:-etr
Woman N: -etra

Man V: -initis
Woman V: -inites

Rule: adj + N + V
        1 N
        1 sex
 """


a = str(input()).split(' ')
# Mã hóa
def encodes(a): 
    if(a.endswith('lios')):
        return 1
    elif(a.endswith('liala')):
        return -1
    elif(a.endswith('etr')):
        return 2
    elif(a.endswith('etra')):
        return -2
    elif(a.endswith('initis')):
        return 3
    elif(a.endswith('inites')):
        return -3
    else:
        return 0

b=[]
for i in range(len(a)):
    b.append(encodes(a[i]))

#check sex
def man(b):
    for i in range(len(b)):
        if(b[i] < 0):
            return 0
    return 1
def woman(b):
    for i in range(len(b)):
        if(b[i] > 0):
            return 0
    return 1

#check 1 N
def only1N(b):
    if(b.count(2) == 1 or b.count(-2) == 1 ):
        return 1
    else:
        return 0

#check thu tu
def thutu(b):
    for i in range(1,len(b)):
        if(abs(b[i-1]) > abs(b[i])):
            return 0
    return 1

# main
if(only1N(b) == 0):
    print('NO')
elif (man(b) == 0 and woman(b) == 0):
    print('NO')
elif (thutu(b) == 0):
    print('NO')
else:
    print('YES')