"""
ID: jessety1
LANG: PYTHON3
TASK: namenum
"""

num_map = {
    '2': ['A','B','C'],
    '5': ['J','K','L'],
    '8': ['T','U','V'],
    '3': ['D','E','F'],     
    '6': ['M','N','O'],    
    '9': ['W','X','Y'],
    '4': ['G','H','I'],     
    '7': ['P','R','S']
}

dict_map = {}
Not_found = True
def get_next(st, i):
    global Not_found
    #print(f"{i} --")
    g = og[i]
    char_ary = num_map[g]
    i = i + 1
    
    for ch in char_ary:
        nst = st+ch 
        if (i == len(og)):
            #print(dict_map[nst])
            if (nst in dict_map ):
                #print(nst)
                filehandle.write(f'{nst}\n')
                Not_found = False
        else:
            get_next(nst, i)


with open('dict.txt','r') as fin:
    for line in fin:
        og = (line.strip())
        dict_map[og] = True
#print(dict_map)

filehandle = open('namenum.out', 'w')



with open('namenum.in','r') as fin:
    og = (fin.readline().strip())
    ogLen = len(og)

start = ""
get_next(start, 0)
if (Not_found):
    filehandle.write(f'NONE\n')
filehandle.close()
    