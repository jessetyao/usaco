"""
ID: jessety1
LANG: PYTHON3
TASK: ride
"""

with open('ride.in','r') as fin:
    comet1 = fin.readline().strip()
    comet2 = fin.readline().strip()

total=1 
total1=1
for c in comet1:
    b = (ord(c)-64)
    total = total*b
final1 = total % 47
for c in comet2:
    a = (ord(c)-64)
    total1 = total1*a
final2 = total1 % 47
with open ('ride.out','w') as fout:
    if final1 == final2:
        fout.write ("GO\n")
    else:
        fout.write ("STAY\n")

