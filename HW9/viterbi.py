from collections import defaultdict

def order(graph,indegree):
    start = [i for i in graph if indegree[i] == 0]
    res = []
    if start == []:return None
    while start!=[]:
        cur = start.pop()
        res.append(cur)
        while graph[cur]!= []:
            neibor = graph[cur].pop() #pop one neibor
            indegree[neibor]-=1    #remove the edge from cur to neibor by deduct indegree
            if indegree[neibor] <= 0:
                start.append(neibor)
    sumdegree = 0
    for i in indegree:
        sumdegree += indegree[i]
    if sumdegree == 0:
        return res
    else:
        return None

def backtrace(opt,best_idx):
    back = []
    pre = best_idx
    while best_idx > -1:
        back.insert(0,best_idx)
        best_idx = opt[best_idx][1]
    return back

def longest(n,edges):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    opt = defaultdict(lambda:(-1,-1))
    for (x,y) in edges:
        graph[x].append(y)
        indegree[y] += 1

    g = order(graph,indegree)
    #print g
    for (x,y) in edges:
        graph[x].append(y)
        indegree[y] += 1
        
    start = [i for i in graph if indegree[i] == 0]
    
    for v in g:
        if indegree[v] == 0:
            opt[v] = (0,-1)
        if graph[v]!=[]:
            for neibor in graph[v]:
                opt[neibor] = (opt[v][0] + 1,v)
    print opt    
    length,best_idx = max([(opt[i][0],i) for i in opt])
    back = backtrace(opt,best_idx)
    return length,back



if __name__ == "__main__":
    print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
