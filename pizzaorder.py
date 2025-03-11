print("welcome to pizza corner:")
size = input("what pizza size do you want S, M or L:")
chilli = input("do you want chilli on pizza Y or N:")
extra_cheese = input("do you want extra_cheese on pizza Y or N:")
bill = 0
if size == "M":
    bill += 15
elif size == "S":
    bill += 10
elif size == "L":
    bill += 20
else:
    print("wrong choices:")
    if chilli == "Y":
        if size == "M":
            bill += 2
        else:
            bill +=3
    if extra_cheese == "Y":
        bill +=1
print(f"your final bill is:${bill}")
