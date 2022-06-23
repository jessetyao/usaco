"""
ID: jessety1
LANG: PYTHON3
TASK: sprime
"""
def checkprime(n): 
    d= 3
    while d * d <= n:
        if n % d == 0:
            return False
        d= d + 2
    return True

with open('sprime.in','r') as fin:
    N= int(fin.readline().strip())

primecandidate = [1, 3, 7, 9]
total_list = []
TOTAL = 10 ** (N-1)
num = 0
def generate_next_int(num):
    primelist = []
    for i in primecandidate:
        todo = num * 10 + i
        if checkprime(todo):
            primelist.append(todo)
    return primelist
            
def generate_from_list(num, total_list):
    if (num // TOTAL) >= 1:
        total_list.append(num)
        return
    plist = generate_next_int(num)
    for i in plist:
        generate_from_list(i, total_list)
primecandidate2 = [2,3,5,7]

for i in primecandidate2:
    generate_from_list(i,total_list)

with open('sprime.out','w') as fout:
    for i in total_list:
        fout.write(f'{i}\n')