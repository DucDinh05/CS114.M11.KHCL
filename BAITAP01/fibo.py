x = int(input())

if x <= 0 or x > 30:
    print("So",x,"khong nam trong khoang [1,30].")
else:
    pfibo=0
    nfibo=1
    for i in range(1,x):
        temp = nfibo
        nfibo = pfibo + nfibo
        pfibo = temp
    print(nfibo)
