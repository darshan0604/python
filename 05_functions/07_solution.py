def valueArgs(*args):
    for i in args:
        print(i) 
    return sum(args)

print("\nSum of given arguments ",valueArgs(10,20,20))