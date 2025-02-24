import random

firstset = ['0','1','2','3']
secondset = ['4','5','6','7']
thirdset = ['8','9']


lottery = []
for char in range(0, 4):
    lottery.append(random.choice(firstset))

for char in range(0, 4):
    lottery.append(random.choice(secondset))

for char in range(0, 2):
    lottery.append(random.choice(thirdset))

print(lottery)
random.shuffle(lottery)
print(lottery)

password = ""
for char in lottery:
    password += char

print(f"Your lottery is: {password}")
