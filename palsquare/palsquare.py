"""
ID: jessety1
LANG: PYTHON3
TASK: palsquare
"""
from lib2to3.pytree import convert

base_number= 0
with open('palsquare.in','r') as fin:
    base_number= int(fin.readline().strip())
arr = []
arr1= []
numap = ['0','1','2','3','4','5',
            '6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def convert_base (i,base_number):
    temp = []
    while True:

        quo = divmod(i,base_number)
        temp.insert(0,quo[1])
        #if quo == (1,0) or quo == (1,1)  or quo == (1,2) :
            #print("not here")
            #break
        i = quo[0]
        if quo[0] == 0:
            break
        # print(quo)
    return(temp )

def check (result):
    for i in range(len(result)//2):
        if result[i] != result[len(result)-i-1]:
            return False
    else:
        return True

outF = open ('palsquare.out','w')

for i in range (1,301):
    result = convert_base(i*i, base_number) 

    if check(result):
            r2 = convert_base(i, base_number) 
            r3 = "".join([numap[x] for x in r2])
            v = "".join([numap[x] for x in result])
            outF.write(f"{r3} {v}\n")
outF.close()  



        #print (i)
        #print ("".join([str(x) for x in result]))
