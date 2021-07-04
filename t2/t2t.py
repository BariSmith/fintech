



def foo():
    for x in range(11, 80):
        if x in  range(11, 80):
            if x % 3 == 0 and x % 5 == 0:
                print (x, "$$@@")
            elif x % 5 == 0:
                print (x, "@@")
            elif x % 3 == 0 :
                print(x, "$$")

foo()