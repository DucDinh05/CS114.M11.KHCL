""" Danh sach lien ket """
""" 
D0: Insert Head(<1000)
D1: Insert Tail(<1000)
D2: Find fist a-> Insert b(a,b<1000)
D3: Find fist n -> Delete n
D4: Delete all n
D5: Delete head
D6: End
"""

from sys import stdin
list_ans = []
while True:
  k = [int(i) for i in stdin.readline().split()]
  if k[0] == 0:
    list_ans.insert(0, k[1])
  elif k[0] == 1:
    list_ans.append(k[1])
  elif k[0] == 2:
    try:
      index = list_ans.index(k[1]) + 1
      list_ans.insert(index, k[2])
    except:
      list_ans.insert(0, k[2])
  elif k[0] == 3:
    try:
      index = list_ans.index(k[1])
      list_ans.pop(index)
    except:
      pass
  elif k[0] == 4:
    list_ans[:] = (i for i in list_ans if i != k[1])
  elif k[0] == 5:
    if len(list_ans) != 0:
      list_ans.pop(0)
  elif k[0] == 6:
    break
print(*list_ans)
