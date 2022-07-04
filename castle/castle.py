"""
ID: jessety1
LANG: PYTHON3
TASK: castle
"""

from math import comb


castle = []
with open('castle.in','r') as fin:
    bound= fin.readline().strip().split()
    n = int(bound[0])
    m = int(bound[1])
    # castle = [[0]*m]*n
    for i in range (m):
        room = [[int(r),False] for r in fin.readline().strip().split()]
        castle.append(room)

#print(castle)
room_count = 0
largest_room = 0
room_size = 0
room_list = []
combine_room_size = 0

def connect (r,c, connectroom):
    global castle
    global room_size
    global largest_room
    global visited
    #print(f"connect castle [{r}][{c}]={castle[r][c]}")
    rn = castle[r][c][0]
    if (castle[r][c][1]):
        return

    castle[r][c][1] = True
    room_size += 1
    connectroom.append([r,c])
    if room_size > largest_room:
        largest_room = room_size
    #print(f"room[{r}][{c}]: {rn}")
    if rn & 1 == 0:
        connect(r,c-1,connectroom)
    if rn & 2 == 0:
        connect(r-1,c,connectroom)
    if rn & 4 == 0:
        connect(r,c+1,connectroom)
    if rn & 8 == 0:
        connect(r+1,c,connectroom)
    
    
    
for i in range (m):
    for j in range (n):
        room_size = 0
        #print(f"entry [{i}][{j}]")
        if not castle[i][j][1]:
            connectroom = []
            connect(i,j, connectroom)
            room_count += 1
            room_list.append(connectroom)
#print (room_count, largest_room, room_list)

# def Sorting(lst):
#     lst2 = sorted(lst, key=len,reverse=True)
#     return lst2

def comparetworoom(list1, list2):
    wall_list = []
    for r1 in list1:
      for r2 in list2:
        if r1[1] == r2[1]:
            if abs(r1[0]-r2[0]) == 1:
                room = [0,0,'']
                #print(f"[{r1[0]+1}, {r1[1]+1}], [{r2[0]+1}, {r2[1]+1}]")
                if r1[0] > r2[0]:
                    room[0] = r1[0]+1
                else:
                    room[0] = r2[0]+1
                room[2] = 'N'
                room[1] = r1[1]+1
                wall_list.append(room)
                

        elif r1[0] == r2[0]:
            if abs(r1[1]-r2[1])== 1:
                room = [0,0,'']
                #print(f"[{r1[0]+1}, {r1[1]+1}], [{r2[0]+1}, {r2[1]+1}]")
                if r1[1] > r2[1]:
                    room[1] = r2[1] +1
                else:
                    room[1] = r1[1]+1
                room[2] = 'E'
                room[0] = r1[0]+1
                wall_list.append(room)
                
        else:
            continue
    return wall_list

comb_list = [[0,0,0]]* (len(room_list) * len(room_list) //2)
ct = 0
for i in range(len(room_list)):
    ilength = len(room_list[i])
    for j in range(i+1,len(room_list)):
        comb_list[ct]= [i,j,ilength+len(room_list[j])]
        ct += 1

comb_list.sort(key=lambda cbsize: cbsize[2], reverse=True)
for k in range(ct):
    cb = comb_list[k]
    wall_list = comparetworoom(room_list[cb[0]], room_list[cb[1]])
    if(len(wall_list) != 0):
        #print(f"We found it")
        #print(wall_list, combine_room_size)
        combine_room_size = len(room_list[cb[0]]) + len(room_list[cb[1]])
        break

a = sorted(wall_list, key=lambda x: (x[1], -1*x[0]))
#print(a)
# print(Sorting(comb_list))

with open ('castle.out','w') as fout:
          
    fout.write(f"{room_count}\n{largest_room}\n{combine_room_size}\n{a[0][0]} {a[0][1]} {a[0][2]}\n")
