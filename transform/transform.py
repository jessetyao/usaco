"""
ID: jessety1
LANG: PYTHON3
TASK: transform
"""

def compare(og1,og2):
    for l in range (N):
        for k in range (N):
            if og1[l][k] != og2[l][k]:
                return False
    return True


def tx1(og, nw):
    for i in range (N):
        for j in range (N):
            tested [j][N-i-1] = og [i][j]
            #print (tested[j][N-i-1])
    #printary("og", og)
    #printary("tested", tested)
    #printary("nw", nw)
    if compare(tested, nw):
        return True
    else:
        return False


def tx2(og, nw):
    for i in range (N):
        for j in range (N):
            tested [N-i-1][N-j-1] = og [i][j]
            #print (tested[j][N-i-1])
    if compare(tested, nw):
        return True
    else:
        return False

def tx3(og, nw):
    for i in range (N):
        for j in range (N):
            tested [N-j-1][i] = og [i][j]
            #print (tested[j][N-i-1])
    if compare(tested, nw):
        return True
    else:
        return False

def printary(title, og):
    print(title + " \n")
    for g in og:
        print (g)
    print ("\n")
    return

def mirror(og,nw): 
    for i in range (N):
        for j in range (N):
            tested [i][N-j-1] = og [i][j]
            #print (tested[j][N-i-1])
    #printary("og", og)
    #printary("tested", tested)
    #printary("nw", nw)
    if compare(tested, nw):
        return True
    else:
        return False
def combination (og, nw):
    for i in range (N):
        for j in range (N):
            tested [i][N-j-1] = og [i][j]
    for i in range (N):
        for j in range (N):
            comb1 [j][N-i-1] = tested [i][j]
    if compare(comb1, nw):
        return True

    for i in range (N):
        for j in range (N):
            comb2 [N-i-1][N-j-1] = tested [i][j]
            #print (tested[j][N-i-1])
    if compare(comb2, nw):
        return True

    for i in range (N):
        for j in range (N):
            comb3 [N-j-1][i] = tested [i][j]
    if compare(comb3, nw):
        return True
    else:
        return False

nw = []
og = []
with open('transform.in','r') as fin:
    N = int(fin.readline().strip())
    for i in range (N):
        og.append(list(fin.readline().strip()))
    for i in range (N):
        nw.append(list(fin.readline().strip()))


comb1 = [ [0]*N for i in range(N) ]
comb2 = [ [0]*N for i in range(N) ]
comb3 = [ [0]*N for i in range(N) ]

# printary(og)
# printary(nw)
tested = [ [0]*N for i in range(N) ]
result = ""

if tx1(og, nw):
    result = ("1\n")
elif tx2(og, nw):
    result = ("2\n")
elif tx3(og, nw):
    result = ("3\n")
elif mirror (og, nw):
    result = ("4\n")
elif combination (og, nw):
    result = ("5\n")
elif compare (og, nw):
    result = ("6\n")
else: 
    result =  ("7\n")

with open ('transform.out','w') as fout:
          
    fout.write(f"{result}")