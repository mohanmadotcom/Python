import random

firstset = ['0','1','2','3']
secondset = ['4','5','6','7']
thirdset = ['8','9']

lottery = ""

for char in firstset:
    lottery += random.choice(firstset)

for char in secondset:
    lottery += random.choice(secondset)

for char in thirdset:
    lottery += random.choice(thirdset)

print(lottery)
