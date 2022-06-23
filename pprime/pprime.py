"""
ID: jessety1
LANG: PYTHON3
TASK: pprime
"""

numbers = []
lowerbound = 0

def checkprime(n):
    if(n < lowerbound):
      return False
    if n & 1 == 0:
        return False
    d= 3
    while d * d <= n:
        if n % d == 0:
            return False
        d= d + 2
    return True

def add_to_queue(num, upper, lower):
    global numbers
    if num <= upper and num >= lower and checkprime(num):
        numbers.append(num)

with open('pprime.in','r') as fin:
    bound= fin.readline().strip().split()
     
    lowerbound = int(bound[0])
    upperbound = int(bound[1])

#print (bound)
x  = len (bound[1])//2

#print (x)
y = len (bound[0])
#print(range (10^x))
#print(lowerbound)
for i in range (10**x):

    if (i < 10):
        add_to_queue(i, upperbound, lowerbound)

    # if x%2 == 0:
    number_s = str(i)
    reverse_s = number_s[::-1]
    finalnum = int(number_s+reverse_s)
    #print (f"even => {finalnum}")
    # if finalnum > upperbound:
    #     print(f"we reach upperbound even {finalnum}")
    #     break
    add_to_queue(finalnum, upperbound, lowerbound)
    
    for j in range (10):
        number_j = str(i)
        reverse_j = number_j[::-1]
        finalnum = int(number_j + str(j)+ reverse_j)
        #print (f"{i}, {j}, odd => {finalnum}")
        #if finalnum > upperbound:
            #print(f"we reach upperbound odd {finalnum}")
            #continue
        add_to_queue(finalnum, upperbound, lowerbound)

numbers.sort()

with open('pprime.out','w') as fout:
    for i in numbers:
        fout.write(f'{i}\n')
    


