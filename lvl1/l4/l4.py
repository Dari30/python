one=1
while one<10:
    print(f"cong{one}")
    one+=3
c=0
while c<10:
    c+=1
    if c%2==0:
        continue
    print(c)
while True:
    print("This is endless loop")
    ans = input("Do you want to stop the loop?y/n")
    if ans =="y":
        break

