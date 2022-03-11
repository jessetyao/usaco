"""
ID: jessety1
LANG: PYTHON3
TASK: combo
"""


with open('combo.in','r') as fin:
    np = (fin.readline().strip())
    combo1 = (fin.readline().strip().split())
    combo2 = (fin.readline().strip().split())

np = int(np)
for i in range(0, len(combo1)):
    combo1[i] = int(combo1[i])
for i in range(0, len(combo2)):
    combo2[i] = int(combo2[i])

difference = 0
holder = []

for i in range (3):

    combobig = combo1[i] if combo1[i] > combo2[i] else combo2[i]
    combosmall = combo1[i] if combo1[i]<= combo2[i] else combo2[i]

    dis1 = combobig - combosmall 
    dis2 = combosmall + np - combobig

    dis = dis1 if dis1 < dis2 else dis2
    # print(combobig, combosmall, dis1, dis2, dis)
    if dis > 4:
        holder.append(0)
    if dis == 4 :
        holder.append(1)
    if dis == 3:
        holder.append(2)
    if dis == 2:
        holder.append(3)
    if dis == 1:
        holder.append(4)
    if dis == 0:
        holder.append(5)
print (holder)
if np == 1:
    count = 1
elif np == 2:
    count = 8
elif np == 3:
    count = 27
elif np == 4:
    count = 64
elif np == 5:
    count = 125

else:
    count = 250-holder[0]*holder[1]*holder[2]
#print (count)

with open ('combo.out','w') as fout:
   fout.write (f"{count}\n")