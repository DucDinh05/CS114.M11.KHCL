"""  Binary Tree  """
""" 
a: 1 or 2 or 3
    1: player_onl
    2: player_off
    3: check
b: ma so
"""
from sys import stdin, stdout
Onl_List = set()
array = []
count = 0
while (1):
  k = [int(i) for i in stdin.readline().split()]
  if len(k) == 0:
    continue
  if k[0] == 0:
    break
  elif k[0] == 1:
    Onl_List.add(k[1])
  elif k[0] == 3:
    if(k[1] in Onl_List):
      Onl_List.remove(k[1])
  else:
    if k[1] in Onl_List:
      array.append(1)
    else:
      array.append(0)

for i in range(len(array)):
  print(array[i])