from collections import defaultdict

def order(n,edges):
    graph = defaultdict(list)  
    indegree = defaultdict(int)
    for (x,y) in edges:
        graph[x].append(y)      
        indegree[y]+=1
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
            
    
        
            
        
    
if __name__ == "__main__":
    g1 = order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
    g2 = order(3, [(0,1),(1,2),(2,0)])
    g3 = order(4, [(0,1), (1,2), (2,1), (2,3)])
    print g1
    print g2
    print g3

