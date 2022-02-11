"""
ID: jessety1
LANG: PYTHON3
TASK: milk2
"""


milking =[]
longest_interval = 0
interval = 0
interv = []
longest_nocow = 0
nocow = 0
with open('milk2.in','r') as fin:
    N = int(fin.readline().strip())
    for i in range (N):
        t = [int(t) for t in fin.readline().strip().split()]
        milking.append(t)
    
milking = sorted(milking)
print(milking)

for i in range (len(milking)):
    if i == 0:
        interv.append(milking[i])
    if interv[-1][1] >= milking[i][0] and interv[-1][0] <= milking[i][0]:
        if interv[-1][1]< milking[i][1]:
            interv[-1][1] = milking[i][1]
    else: 
        interv.append(milking[i])
x = len(interv)-1
for i in range (x, -1, -1):
    for j in range (i-1, -1, -1): 
        if interv [i][0] <= interv [j][0]:
            interv [j] = [0,0]



for i in range (len(interv)):
    if interv [i] == [0,0]: 
        continue
    interval = interv[i][1]-interv[i][0]
    if interval > longest_interval:
        longest_interval = interval
    if i < len(interv)-1:
        nocow = interv[i+1][0]-interv[i][1]
    if nocow > longest_nocow:
        longest_nocow = nocow

print(longest_interval)
print (longest_nocow)

print (interv)
    

with open ('milk2.out','w') as fout:
          
    fout.write(f"{longest_interval} {longest_nocow}\n")