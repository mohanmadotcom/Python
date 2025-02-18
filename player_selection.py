import random

# Method 1
player = ["Rohit", "Kohli", "Gill", "KL Rahul", "Jaiswal"]
selected_player = player[(random.randint(0,4))]
print(selected_player)

# Method 2

print(random.choice(player))
