
"""
ID: jessety1
LANG: PYTHON3
TASK: crypt1
"""

with open('crypt1.in','r') as fin:
    np = int(fin.readline())
    holder = (fin.readline().strip().split())
#print (holder)

def checknum (abcde):
    ner = str(abcde)
    for i in range(len(ner)):
        #print (ner[i])
        #print(ner[i] in holder)
        if (ner[i] in holder) == False:
            return False
    return True

#print (checknum (2346))
abc = 0
de = 0

#print ('5' in holder)

count = 0
list_of_num = []

for i in range (1000):
    for i in range (100):
        num = abc*de
        if len(str(de)) == 2:
            fill = str (de)
            di = fill[0]
            d = int(di)
            ei = fill[1]
            e = int(ei)
        if len(str(num)) == 4 and len(str(de)) == 2 and len(str(abc)) == 3 and len(str(abc * e)) == 3 and len(str(abc * d))==3 and checknum(abc*d) == True and checknum(abc*e)== True and checknum(num)==True and checknum(abc) and checknum(de):
            list_of_num.append(num)
            count+= 1
        de += 1
    abc += 1
    de = 0

#print (list_of_num)
with open ('crypt1.out','w') as fout:
    fout.write (f"{count}\n")
#new_list_of_num = []
#for i in len(list_of_num):



'''
create function that checks if function is legal
-have counter, if 0 or 1 check for 3 digits
-if 2 check for 4 digits
checks if the digits used are legal

check abc*e
then abc*d
then de*abc
with open('crypt1.in','r') as fin:
    np = int(fin.readline())
    holder = (fin.readline().strip().split())

print (holder)



a,b,c,d,e = '','','','',''

if holder[0] != '0':
    a,b,c,d,e = holder[0],holder[0],holder[0],holder[0],holder[0]
else:
    a,b,c,d,e = holder[1],holder[1],holder[1],holder[1],holder[1]

results = []

for i in range (np):
    num = int(a+b+c)*int(e)
    results.append(num)
    e = holder[i-1]


print (results)
'''