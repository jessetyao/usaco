"""
ID: jessety1
LANG: PYTHON3
TASK: dualpal
"""
start= 0
with open('dualpal.in','r') as fin:
    start = (fin.readline().strip())
startlist = start.split()
N = int(startlist[0])
S = int(startlist[1])

def convert_base (i,base_number):
    temp = []
    while True:
        quo = divmod(i,base_number)
        temp.insert(0,quo[1])
        i = quo[0]
        if quo[0] == 0:
            break
    return(temp )

def check (result):
    for i in range(len(result)//2):
        if result[i] != result[len(result)-i-1]:
            return False
    else:
        return True
count = 0
base_count = 0
i = 0
base = 2
final_list = []

#assuming i starts at 0
while count < N:
    #print(f"S:{S}")
    for i in range (9):
        result = convert_base (S+1,base+i)
        #print(f"base: {base+i} {result}")
        
        if check(result):
            #print(f"found one")
            base_count += 1
        #print(f"base_count {base_count}")
        if base_count > 1:
            final_list.append(S+1)
            base_count == 0
            count += 1
            break
    #print(f"S:{S}, count:{count}")
    S += 1
    base_count = 0
    #if (S > 40):
        #break
#print (final_list)
    
outF = open ('dualpal.out','w')
for i in range (N):
    outF.write(f"{final_list[i]}\n")
outF.close()  

        
