# given list  : [["a"], ["b",["a"]], ["c",["b",["a"]]], ["d",["c",["b",["a"]]]],"e"]

# result list : ["a", "b", "a", "c", "b", "a", "d", "c", "b", "a", "e"]

# wirte a function which produces the result list with the given list
import itertools

def flatten_list(a):
    result_list = []
    for s in a:
        for el in s:
            result_list.append(el)
    return result_list

def flatten_list_v2(a):       
    return list(itertools.chain(*a))


def flatten_list_v3(a):
    if len(a) == 0:
        return []    
    elif isinstance(a[0], list):
        return flatten_list_v3(a[0]) + flatten_list_v3(a[1:])
    else:
        return a[:1] + flatten_list_v3(a[1:])
    
    
# driver code

a = [
    ["a"], 
    ["b",["a"]], 
    ["c",["b",["a"]]], 
    ["d",["c",["b",["a"]]]],"e"]
#print(flatten_list_v3(a) == ["a", "b", "a", "c", "b", "a", "d", "c", "b", "a", "e"])







"""
First position: start
Second: destination
Third: distance

# data = [
(1,2,1),
(1,3,4),(2,5,2),(2,4,2),(3,7,1),(3,8,1),(4,5,3),(4,6,3),(4,9,4),(5,7,1),(5,6,2),(6,7,2),(6,8,1),(6,9,2),(7,8,1),(8,9,2)]

there is a given list of tuples like above. each tuple has 3 elements. 
# first two elements show connectivity and the last element shows the distance of two points.
# find the shortest path from 1 to 9. and print path and distance. when multiple paths exists, print all paths
"""

class G:
    def __init__(self, v):
        self.V = v
        self.V_org = v
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v, w):
        if w == 1:
            self.graph[u].append(v)
        else:
            self.graph[u].append(self.V)
            self.graph[self.V].append(v)
            self.V = self.V + 1
        
    
    def print_path_distance(self, s, d):
        pass

    def shortest_path(data, s, d):
        visited = [False]* (self.V)
        parent = [-1]*(self.V)

        q = []

        q.append(s)
        visited[s] = True

        while q:
            ss = q.pop(0)

            if ss == d:
                return self.print_path_distance(parent, ss)
            
            for i in self.graph[ss]:
                if visited[i] == False:
                    q.append(i)
                    visited[i] = True
                    parent[i] = s

# driver code
a = [(1,2,1),(1,3,4),(2,5,2),(2,4,2),(3,7,1),(3,8,1),(4,5,3),(4,6,3),(4,9,4),(5,7,1),(5,6,2),(6,7,2),(6,8,1),(6,9,2),(7,8,1),(8,9,2)]
print(shortest_path(a))
