import random

def roll():
    return random.randint(1, 6)

while True:
    x = roll()
    print(x)
    if x == 6:
        break
