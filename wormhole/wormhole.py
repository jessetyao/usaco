"""
ID: jessety1
LANG: PYTHON3
TASK: wormhole
"""
#add one to x to (x,y) everytime you loop through
#if it matches to a point find where it's connected to, then keep adding 1 from there
#if it goes back to the originial point or a point it hit before, stop it and count 1
#another loops will test each possible combination (how to calculate the combination for 12 wormholes?)

#def passage (point1, point2):
    #point1 = point2
    #return point1
#newpoint = []
#count_for_list_of_4 = 0
#def search(list, currentpoint):
    #for i in range(len(list)):
        #if list[i] == currentpoint:
            #newpoint = list[i]
            #return True
   # return False
    
#list_of_points = []
#list_of_x = []
#count = 0
#with open('wormhole.in','r') as fin:
    #N = int(fin.readline().strip())
   # for i in range (N):
        #t = [int(t) for t in fin.readline().strip().split()]
       # list_of_points.append(t)
       # list_of_x.append(t[1])
#print (list_of_points)

#list_of_x.sort()
#print (list_of_x)
#if N == 2:
    #while list_of_points[0][1] < list_of_points[1][1]:
       # list_of_points[0][1] += 1 
        #if list_of_points[0] == list_of_points[1]:
            #count+=1
            #break
#if N == 4: 
    #for i in range (4):
        #while list_of_points[i][1] < list_of_x[-1]:
            #list_of_points[i][1] += 1 
            #if search (list_of_points, list_of_points[i]):
                #count_for_list_of_4 +=1
                #passage (list_of_points[i],newpoint)
            #if count_for_list_of_4 > 3:
                #count+1
                #continue


#print (count)
    
from operator import truediv


list_of_y = [0]*13
list_of_x = [0]*13
partner = [0]*13
next_of_right = [0]*13

with open('wormhole.in','r') as fin:
    N = int(fin.readline().strip())
    for i in range (1, N+1):
        t = [int(t) for t in fin.readline().strip().split()]
        list_of_x[i] = t[0]
        list_of_y[i] = t[1]
#print (list_of_x)

def cycle_exists():
    for start in range (1,N+1):
        pos = start
        for count in range (N):
            pos = next_of_right[partner[pos]]
        if pos != 0:
            return True
    return False

def solve():
    total = 0
    i = 0
    for i in range (1, N+1): 
        if partner[i] == 0:
            break
    else:
        if cycle_exists():
            return 1
        else:
            return 0
        
    for j in range (i+1, N+1): 
        if partner[j] == 0: 
            partner[i] = j
            partner[j] = i
            total += solve()
            partner[i] = 0
            partner[j] = 0
    return total
for i in range (1, N+1):
    for j in range (1, N+1): 
        # print (next_of_right)
        if list_of_x[j]>list_of_x[i] and list_of_y[i] == list_of_y[j]:
            # print(i, j, next_of_right[i])
            if next_of_right[i] == 0 or (list_of_x[j]-list_of_x[i]) < list_of_x[next_of_right[i]]-list_of_x[i]:
                next_of_right[i] = j
# print (next_of_right)
v = solve()
with open ('wormhole.out','w') as fout:
   fout.write (f"{v}\n")