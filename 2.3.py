a = int(input("adj meg egy egész számot"))

if a % 3 == 0:
    print("csak 3-mal osztható,")
    
if a % 4 == 0:
    print("csak 4-gyel osztható,")
    
    
    
if a % 3 == 0 and a % 4 == 0:
    print("3-mal és 4-gyel is osztható,")
    
else:
    print("sem 3-mal, sem 4-gyel nem osztható!")