"""
ID: jessety1
LANG: PYTHON3
TASK: milk3
"""
with open('milk3.in','r') as fin:
    holder = [int(c) for c in fin.readline().strip().split()]

#print (holder)
max_a = holder[0]
max_b = holder[1]
max_c = holder[2]
c = holder [2]
a = 0
b = 0
list_of_combos = []
final_list = []

visited = {}

def checkifexist (a,b,c):
    global visited
    return (a,b,c) in visited

def addVisit(a,b,c):
    global visited
    visited[(a,b,c)] = True

def move (a,b,c):
    if checkifexist(a,b,c):
        return
    addVisit(a,b,c)
    if a == 0: 
        #print(f"we find {a}, {b}, {c}")
        final_list.append (c)

    # a->b
    a1 = a
    b1 = b
    mid = a1 + b1
    if mid > max_b:
        b1 = max_b
        a1 = mid - max_b
    else:
        b1 = a1 + b1
        a1 = 0
        

    move(a1,b1,c)

    #a->c
    a3 = a
    c3 = c
    mid = a3 + c3
    if mid > max_c:
        c3 = max_c
        a3 = mid - max_c
    else:
        c3 = a3 + c3
        a3 = 0
        

    move(a3,b,c3)

    # b->a
    a2 = a
    b2 = b
    mid = a2 + b2
    if mid > max_a:
        a2 = max_a
        b2 = mid - max_a
    else:
        a2 = a2 + b2
        b2 = 0
        

    move(a2,b2,c)


    # b->c
    c4 = c
    b4 = b
    mid = c4 + b4
    if mid > max_c:
        c4 = max_c
        b4 = mid - max_c
    else:
        c4 = c4 + b4
        b4 = 0
        

    move(a,b4,c4)
    # c->a
    c5 = c
    a5 = a
    mid = c5 + a5
    if mid > max_a:
        a5 = max_a
        c5 = mid - max_a
    else:
        a5 = c5 + a5
        c5 = 0
        

    move(a5,b,c5)
    # c->b
    c6 = c
    b6 = b
    mid = c6 + b6
    if mid > max_b:
        b6 = max_b
        c6 = mid - max_b
    else:
        b6 = c6 + b6
        c6 = 0
        

    move(a,b6,c6)    
        

    
move (a,b,c)
final_list1 =  sorted(final_list)
#print (final_list1)

with open ('milk3.out','w') as fout:
    res = " ".join([str(i) for i in final_list1])
    #print(res)
    fout.write(f"{res}\n")