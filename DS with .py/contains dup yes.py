def fin(List):
    d=dict()
    for i in List:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]<=1:
            return False
    return True
L=[1,2,3,4,2,3,4,1]
x=fin(L)
print(x)

