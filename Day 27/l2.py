#many arguments


#we use *args for this purpose note srgs is not a keyword can use any

def fun(*args):
    print(args)
    sum = 0  #args can also be acessed through index since it is tuple
    for n in args:
        sum += n
    return sum

print(fun(2, 3, 4, 5, 6, 6))


#if we need to acess using name then we use **kwargs\
def funn(n, **kwags):
    n += kwags["add"]
    n *= kwags["mul"]
    print(n)

funn(2, add=3, mul=5)



def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)