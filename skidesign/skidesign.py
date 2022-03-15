
"""
ID: jessety1
LANG: PYTHON3
TASK: skidesign
"""
list_of_hills = []
with open('skidesign.in','r') as fin:
    N = int(fin.readline().strip())
    for i in range (N):
        t = int(fin.readline().strip())
        list_of_hills.append(t)

x = 0
y = 17
cost = 0
total_cost = float('inf')
difference = 0
for j in range (84):
    for i in range (N): 
        if list_of_hills[i] < x:
            difference = x-list_of_hills[i]
            cost += difference*difference
        elif list_of_hills[i] > y: 
            difference = list_of_hills[i]-y
            cost += difference*difference
        #print(f"{list_of_hills[i]} {x} {difference}  {y}")
    if total_cost > cost:
        total_cost = cost
        #print(f"total cost {total_cost} {x} {y}")
    cost = 0
    x +=1
    y +=1

with open ('skidesign.out','w') as fout:
   fout.write (f"{total_cost}\n")