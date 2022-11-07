# cook your dish here
n = int(input())

while n > 0:
    n = n-1
    a,b,c,d = int(input()).split()
    new_a = a-c
    new_b = b-d
    if new_a > new_a:
        print("First")
    elif new_b > new_a:
        print("Second")
    else:
        print("Any")