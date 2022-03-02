
"""
ID: jessety1
LANG: PYTHON3
TASK: milk
"""

with open('milk.in','r') as fin:
    np = (fin.readline().strip())
    startlist = np.split()
    total_milk = int(startlist[0])
    num_of_farmers = int(startlist[1])
    farmers = []
    for i in range(num_of_farmers):
        holder = [int(c) for c in fin.readline().strip().split()]
        farmers.append(holder)

    farmers = sorted(farmers)
milk = 0
milk_cost = 0
for f in farmers:
    added_milk = f[1]
    if milk+added_milk >= total_milk:
        added_milk = total_milk - milk
    milk_cost = milk_cost+added_milk*f[0]
    milk = milk+added_milk
    '''
    print (milk)
    print (total_milk)
    print (milk_cost)
    '''
    if milk == total_milk:
        break
with open ('milk.out','w') as fout:
    fout.write (f"{milk_cost}\n")
