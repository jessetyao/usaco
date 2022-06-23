"""
ID: jessety1
LANG: PYTHON3
TASK: ariprog
"""

with open('ariprog.in','r') as fin:
    N = int(fin.readline().strip())
    M = int(fin.readline().strip())
bismap = {}


for i in range (M+1):
    for j in range (i, M+1):
        bisquare = i*i + j*j
        #print(bisquare)
        #print ("i = " + str(i))
        #print ("j = " + str(j))
        bismap[bisquare] = True

# bismap = sorted(bismap)
bis = bismap.keys()
bis = sorted(bis)

#print (bis)
count = 0
diff = []
res = []
x = len(bis)
for i in range (x-N):
    for j in range (i + 1, x-N+2):
        d = bis[j]-bis[i]
        if d > (bis[-1]-bis[i])/(N-1) + 1:
            break
        for k in range (2, N):
            seq = bis[i] + k * d
           #print ("seq = " + str(seq))
           #print ("k = " + str(k))
           #print ("d = " + str(d))
            #if bis [i] == 37:
                #print ("seq = " + str(seq))
                #print ("k = " + str(k))
                #print ("d = " + str(d))
            if seq not in bismap:
               break
        else:
            #print(f"We found one {bis[i]}, {d}")
            res.append((bis[i], d))
            count += 1


res = sorted(res, key=lambda x: x[1])
#print(f"{res}")

with open ('ariprog.out','w') as fout:
    if count != 0:
        for i in range (len(res)):
                fout.write (str(res[i][0]) + " "+ str(res[i][1]) + "\n")
    else:
        fout.write ("NONE\n")



