import sys

class AdjMatrixGraph:

    def __init__(self, dims):
        self.dims = dims
        self.graph = [[0 for x in range(dims)] for y in range(dims)]

    def min_path(self, src, target):

        all_distances = [sys.maxsize] * self.dims
        all_distances[src] = 0
        shortest_path_tree_set = [False] * self.dims

        for n in range(self.dims):
            # get a vertex from the unseen set of vertices
            i = self.minimal_dist(all_distances, shortest_path_tree_set)

            # add minimum distance vertex to the shortest path tree set
            shortest_path_tree_set[i] = True

            # if unprocessed and if current distnace greater than recomputed distance, add up distances
            for vertex in range(self.dims):
                if (self.graph[i][vertex] > 0 and shortest_path_tree_set[vertex] == False) \
                        and (all_distances[vertex] > (all_distances[i] + self.graph[i][vertex])):
                    all_distances[vertex] = all_distances[i] + self.graph[i][vertex]

        return all_distances

    # helper method to get vertex with minimal distance value, that is not in our shortest paths set
    def minimal_dist(self, distance, shortest_path_tree_set):
        min = sys.maxsize
        min_dist_index = 0
        for vertex in range(self.dims):
            if distance[vertex] < min and shortest_path_tree_set[vertex] == False:
                min_dist_index = vertex
                min = distance[vertex]
        return min_dist_index


g = AdjMatrixGraph(5)
g.graph = [[0, 5, 0, 5, 7],# A
           [0, 0, 4, 0, 0],# B
           [0, 4, 0, 8, 2],# C
           [0, 0, 8, 0, 6],# D
           [0, 3, 0, 0, 0] # E
           #A #B #C #D #E
           ]

a = 0
b = 1
c = 2
d = 3
e = 4
LABELS = ["A", "B", "C", "D", "E"]

def get_distance_from_to(stops, g, debug, only_direct):
    if len(stops) > 1:
        sliding_window = zip(stops,stops[1:])
        total_distance = 0
        for a,b in sliding_window:
            if only_direct:
                if g.graph[a][b] == 0:
                    return 0

            if g.graph[a][b] > 0:
                ab = g.graph[a][b]
            else:
                ab = g.min_path(a, b)[b]
            if ab > 0:
                if debug:
                    print(f"The distance of the route {LABELS[a]}-{LABELS[b]} is {ab}")
                total_distance += ab
            else:
                #print("NO SUCH ROUTE")
                return 0
        return total_distance

###### Driver code ########

#1. The distance of the route A-B-C. AB + BC

td = get_distance_from_to([a,b,c],g,False,True)

if td > 0 :
    print(f"1. The distance of the route A-B-C is {td}")
else:
    print("NO SUCH ROUTE")

#2. The distance of the route A-D.

td = get_distance_from_to([a,d],g,False,True)

if td > 0 :
    print(f"2. The distance of the route A-D is {td}")
else:
    print("NO SUCH ROUTE")

#3. The distance of the route A-D-C. AD + DC

td = get_distance_from_to([a,d,c],g,False,True)

if td > 0 :
    print(f"3. The distance of the route A-D-C is {td}")
else:
    print("NO SUCH ROUTE")

# 4. The distance of the route A-E-B-C-D.

td = get_distance_from_to([a,e,b,c,d],g,False,True)

if td > 0 :
    print(f"4. The distance of the route A-E-B-C-D is {td}")
else:
    print("NO SUCH ROUTE")

#5. The distance of the route A-E-D.

td = get_distance_from_to([a,e,d],g,False, True)

if td > 0 :
    print(f"5. The distance of the route A-E-D is {td}")
else:
    print("5. NO SUCH ROUTE")

#8. The length of the shortest route (in terms of distance to travel) from A to C.
td = get_distance_from_to([a,c],g,False, False)

if td > 0 :
    print(f"8. The distance of the route A-E-B-C-D is {td}")
else:
    print("8. NO SUCH ROUTE")


"""
TODO:
6. The number of trips starting at C and ending at C with a maximum of 3
stops.  In the sample data below, there are two such trips: C-D-C (2
stops). and C-E-B-C (3 stops).

7. The number of trips starting at A and ending at C with exactly 4 stops.
In the sample data below, there are three such trips: A to C (via B,C,D); A
to C (via D,C,D); and A to C (via D,E,B).

9. The length of the shortest route (in terms of distance to travel) from B
to B.

10. The number of different routes from C to C with a distance of less than
 30.  In the sample data, the trips are: CDC, CEBC, CEBCDC, CDCEBC, CDEBC,
CEBCEBC, CEBCEBCEBC.
"""


