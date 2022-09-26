import random

x = random.randint(1,2)

r = int(input("1 vagy 2"))

print(x)
if x > r:
    print("nem talalt")
    
if x < r:
    print("nem talalt")
    
if x == r:
    print("talalt")
