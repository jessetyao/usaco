content = []

with open("gift1.in") as f:
    content = f.readlines()
    

content = [x.strip(" \n\r") for x in content] 
print(content)
num_of_people = int(content[0])

peoples = []

for i in range(1, 1+num_of_people):
    people = {"name": content[i]}
    peoples.append(people)

print(peoples)

