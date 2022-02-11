"""
ID: jessety1
LANG: PYTHON3
TASK: beads
"""

with open('beads.in','r') as fin:
    num_Of_Beads = int(fin.readline().strip())
    bead_Color = fin.readline().strip()

count = 0
count2 = 0
final_count = 0
turn = 0 
bead_Colors = bead_Color + bead_Color
#print(bead_Colors)

for i in range (num_Of_Beads*2-1):
    #print("----------")
    count = 0
    current_color =  bead_Colors [i+1]
    for k in range (i + 1, num_Of_Beads*2-1):
        if current_color == "w":
            if bead_Colors[k] != "w":
                current_color = bead_Colors[k]
        if bead_Colors[k] == current_color or bead_Colors[k] == "w":
            count += 1
        else:
            break
    #print(f"count:{count} {bead_Colors[i+1:i+count+1]}")
    count2 = 0
    current_color =  bead_Colors [i]
    for k in range (i , -1, -1):
        if current_color == "w":
            if bead_Colors[k] != "w":
                current_color = bead_Colors[k]
        if bead_Colors[k] == current_color or bead_Colors[k] == "w":
            count2 += 1
        else:
            break
    if count2 + count > final_count:
        final_count = count2 + count
    if final_count > num_Of_Beads:
        final_count = num_Of_Beads
#     print(f"count2: {count2}  {bead_Colors[i-count2+1:i+1]}")
#     print(f"count={count2 + count}, i={i}")
# print (final_count)
with open ('beads.out','w') as fout:
          
    fout.write(f"{final_count}\n")