#DFS AND BFS
#dfs in python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
v=set()
def dfs(graph,v,ver):
    if ver not in v:
        print(ver,end="")
        v.add(ver)
        for i in graph[ver]:
            dfs(graph,v,i)
dfs(graph,v,'5')

#BFS in python
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
qr=[]
vis=[]

def bfs(vis,graph,n):
    vis.append(n)
    qr.append(n)
    while qr:
        m=qr.pop(0)
        print(m,end=" ")
        
        for i in graph[m]:
            if i not in vis:
                vis.append(i)
                qr.append(i)
bfs(vis,graph,'5')
