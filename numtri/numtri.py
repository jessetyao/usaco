"""
ID: jessety1
LANG: PYTHON3
TASK: numtri
"""
'''

listofnum = []
with open('numtri.in','r') as fin:
    np = int(fin.readline())
    for i in range (np):
        listofnum.append( [int(c) for c in fin.readline().strip().split()] )
            
maxsum = 0
def solve(sum, i, j):
    global maxsum
    global listofnum
    sum += listofnum[i][j]
    if i == np-1:
        if (sum > maxsum):
            maxsum = sum
        return
    solve(sum, i+1, j)
    solve(sum, i+1, j+1)

solve(0,0,0)
with open ('numtri.out','w') as fout:
   fout.write (f"{maxsum}\n")
''' 

fin = open('numtri.in','r')
n = int(fin.readline())
nums=[ list(map(int,e.strip().split(" "))) for e in fin.readlines()]

for i, line in enumerate(nums):
    if i!=0:
        for j,e in enumerate(line):
            if j==0 :
                nums[i][j]=nums[i][j]+nums[i-1][j]
                continue
            elif e==line[-1] :
                nums[i][j]=nums[i][j]+nums[i-1][j-1]
            if i!=n-1:
                if nums[i][j]>=nums[i][j-1]:
                    nums[i+1][j]+=nums[i][j]
                else :
                    nums[i+1][j]+=nums[i][j-1]

with open('numtri.out','w') as fout:
    fout.write(f'{max(nums[-1][:])}\n')