

def getmax(l):
    if len(l)<=1:
        return None
    lar = l[0]
    seclar = None
    for x in l[1:]:
        if x>lar:
            seclar=lar
            lar=x

        if x!=lar:
            if seclar==None or seclar<x:
                seclar=x


    return lar , seclar



l = [1,2,3,45,44,76]
print(f'largest and second larget is',getmax(l))
