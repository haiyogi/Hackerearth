t=int(input())
liftA=0
liftB=7
for t in range(0,t):
    floor=int(input())
    if(floor-liftA<=liftB-floor):
        print("A")
        liftA=floor
    else:
        print("B")
        liftB=floor