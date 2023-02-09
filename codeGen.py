import random as r


num = int(''.join(str(r.randint(0, 9)) for _ in range(4)))

print(num)
if num == input():
    exit()