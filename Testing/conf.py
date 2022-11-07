persion = {}

name = input("Enter your name :  ")
while True:
    for i in persion:
        if i == name:
            print("Welcome back ",name)
            persion[i]+=1
            break
    persion.insert