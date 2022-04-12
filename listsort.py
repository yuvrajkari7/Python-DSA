


# using sorted function

def issort(l):
    sl = sorted(l)
    if sl==True:
        return True
    else:
        return False

l=[1,2,3,4,44,23]
# issort(l)
if issort(l):
    print('yes')

else:
    print('NO',l)