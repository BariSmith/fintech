
m = [4, 9, 8, 5, 1, 3, 7, 2, 6]
l = 4

def slice_less():
    m.sort()
    for x in m:
        if x >= l:
            print(x)
        

slice_less()