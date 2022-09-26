a = input("Jön Henrik ma kosarazni?")
m = input("Jön Hanna ma kosarazni?")


d = "igen"
lek = "nem"

if a > d and a < lek:
    print("rt")
    
if m > d and m < lek:
    print("56")
    
if a == d and m == lek or a == lek and m == d :
    print(" csak az egyikük jön kosarazni.")
    
elif a == d and m == d:
    print(" mind a ketten jönnek kosarazni")
        
else:
    print("egyikük sem jön kosarazni")
