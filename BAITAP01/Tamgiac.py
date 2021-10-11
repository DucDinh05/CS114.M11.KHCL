import math

a = float(input())
b = float(input())
c = float(input())

if a + b <= c or a+c <= 2 or b+c <= a:
    print("Khong phai tam giac")
else:
    p = (a + b+ c)/2
    S = math.sqrt(p*(p-a)*(p-b)*(p-c))
if type(S) == int:
    S = int(S)
    
if a + b <= c or a+c <= 2 or b+c <= a:
    s=0
elif a == b and b == c:
    print("Tam giac deu, dien tich =",round(S,2))
elif a == b or b == c or a == c:
    print("Tam giac can, dien tich =",round(S,2))
elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Tam giac vuong, dien tich =",round(S,2)) 
else:
    print("Tam giac thuong, dien tich =",round(S,2))