'''[[5,1,9,11]
   [2,4,8,10]
   [13,3,6,7]
  [15,14,12,16]]    to
  [[15,13,2,5]
   [14,3,4,1]
   [12,6,8,9]
  [16,7,10,11]]'''

List= [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
n=len(List)
for i in range(0,len(List)):
    x=1
    for j in range(n,0,-1):
        print(List[j-x][i],end=" ")
    x+=1
    print()
