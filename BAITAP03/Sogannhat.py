""" 
arr A da sap xep tang dan
n so pt
k so gan x nhat
so nho hon
"""

n = int(input())
arr = list(map(int, input().strip().split()))[:n]
k, x = map(int, input().split())
#Phan chuoi
Nhohon = []
Lonhon = []
kq = []

for i in range(len(arr)):
  if arr[i] <= x:
    Nhohon.append(arr[i])
  else:
    Lonhon.append(arr[i])

#Lay k phan tu dau hoac cuoi
if len(Lonhon) == 0:
  for i in range(len(Nhohon)):
    if i >= len(Nhohon) - k:
      print(arr[i], end = ' ')
elif len(Nhohon) == 0:
  for i in range(0, k):
    print(arr[i], end = ' ')
else:
  count = 0 
  l = 0
  r = 0

  while (count < k) and (len(Nhohon) - 1 - l >= 0) and (r < len(Lonhon)):
    if x - Nhohon[len(Nhohon) - 1 - l] <= Lonhon[r] - x:
      kq.append(Nhohon[len(Nhohon) - 1 - l])
      l += 1
    else:
      kq.append(Lonhon[r])
      r += 1
    count += 1

  while count < k and len(Nhohon) - 1 - l >= 0:
    kq.append(Nhohon[len(Nhohon) - 1 - l])
    l += 1
    count += 1

  while count < k and len(Lonhon) > r:
    kq.append(Lonhon[r])
    r += 1
    count += 1

  kq.sort()
  for i in range(len(kq)):
    print(kq[i], end = ' ')