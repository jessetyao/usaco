"""
ID: jessety1
LANG: PYTHON3
TASK: gift1
"""

people = {}
po = []
with open('gift1.in','r') as fin:
    np = int(fin.readline().strip())
    for i in range(np):
        name= fin.readline().strip()
        people[name] = 0
        po.append(name)
        
    for i in range(np):
        #name
        giver1 = fin.readline().strip()
        #amount give and number of people
        (money1, ptg) = [int(x) for x in fin.readline().strip().split()]
        if ptg != 0:
            people[giver1] = people[giver1] -money1 + money1 % ptg

        for j in range(ptg):
            #GET list of people to give to
            g = fin.readline().strip()
            people[g] += money1//ptg
with open ('gift1.out','w') as fout:
    for p in po:    
        fout.write (f"{p} {people[p]}\n")
