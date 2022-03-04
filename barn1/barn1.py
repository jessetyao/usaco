"""
ID: jessety1
LANG: PYTHON3
TASK: barn1
"""
with open('barn1.in','r') as fin:
    np = (fin.readline().strip())
    startlist = np.split()
    max_boards = int(startlist[0])
    num_of_stalls = int(startlist[1])
    cow_in_stall = int(startlist[2])
    stallnum = []
    for i in range(cow_in_stall):
        holder = int(fin.readline())
        stallnum.append(holder)
stallnum.sort()
subtract = []
if max_boards > cow_in_stall:
    max_boards = cow_in_stall

for i in range (cow_in_stall-1):
    subtract.append((i,stallnum[i+1]-stallnum[i]))
subtract.sort(key=lambda x: x[1], reverse=True)
list_of_index = []
#print(subtract)

if max_boards == 1:
    x = subtract[0][0]
    list_of_index.append(x)
else:
    for i in range (max_boards-1):
        x = subtract[i][0]
        list_of_index.append(x)


list_of_index.sort()
#print (list_of_index)
#print(stallnum)
count = 0
for i in range (max_boards-1):
    if count == 0:
        count += stallnum[list_of_index[i]]-stallnum[0]+1 
        #print(count)
    else: 
        count += stallnum[list_of_index[i]]-stallnum[list_of_index[i-1]+1]+1
        #print(count)

#print(f"stallnum[-1] {stallnum[-1]} list_of_index[-1] {list_of_index} {stallnum[list_of_index[-1]]} ")
if max_boards != 1: 
    count += stallnum[-1]-stallnum[list_of_index[-1]+1]+1
else:
    count += stallnum[-1]-stallnum[0]
    count += 1

with open ('barn1.out','w') as fout:
    fout.write (f"{count}\n")




