class Graph:
    def __init__(self, g_dict = {}):
        self.g_dict = g_dict

    def add_edges(self, vertix, edges=[]):
        vert = self.g_dict.get(vertix)
        if vert is None:
            self.g_dict[vertix] = edges
        else:
            self.g_dict[vertix].extend(edges)
        return self.g_dict

    def bfs(self, val):
        visited = [val]
        queue = [val]
        while queue:
            deq = queue.pop(0)
            print(deq)
            for el in self.g_dict[deq]:
                if el not in visited:
                    queue.append(el)
                    visited.append(el)

    def dfs(self, val):
        visited = [val]
        stack = [val]

        while stack:
            pop_val = stack.pop()
            print(pop_val)
            for vertex in self.g_dict[pop_val]:
                if vertex not in visited:
                    visited.append(vertex)
                    stack.append(vertex)


    def bfs_sssp(self, start, end):
        queue = []
        queue.append(start)
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adj in self.g_dict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)
        print(path)






# g = Graph()
# (g.add_edges('A',['B']))
# (g.add_edges('A',['C']))
# (g.add_edges('B',['D', 'G']))
# (g.add_edges('C',['D', 'E']))
# (g.add_edges('D',['F']))
# (g.add_edges('E',['F']))
# (g.add_edges('G',['F']))
# g.bfs_sssp('A', 'F')
# g.dfs('A')




from collections import defaultdict
class TopologyGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_util(self, vertex, visited, stack):
        visited.append(vertex)
        for i in self.graph[vertex]:
            if i not in visited:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, vertex)

    def topological_sort(self):
        stack = []
        visited = []

        for k in list(self.graph):
            if k not in visited:
                self.topological_sort_util(k, visited, stack)
        print(stack)


# tg = TopologyGraph()
# tg.add_edge('A','C')
# tg.add_edge('C','E')
# tg.add_edge('E','H')
# tg.add_edge('E','F')
# tg.add_edge('D','F')
# tg.add_edge('F','G')
# tg.add_edge('B','D')
# tg.add_edge('B','C')
# tg.topological_sort()


class WeightedGraph:
    def __init__(self):
        self.w_graph = {}

    def add_edge(self, vertex, edge, weight):
        node = self.w_graph.get(vertex)
        edge_data = (edge, weight)
        if node:
            node.append(edge_data)
        else:
            self.w_graph[vertex] = [edge_data]
        return (self.w_graph)

    def dijkstra(self, start, end=None):
        path = defaultdict(list)
        visited = {start: 0}
        nodes = set(self.w_graph.keys())
        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None or visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break
            nodes.remove(min_node)
            curr_weight = visited[min_node]

            for edge in self.w_graph.get(min_node,[]):
                weight = curr_weight + edge[1]

                if edge[0] not in visited or weight < visited[edge[0]]:
                    visited[edge[0]] = weight
                    path[edge[0]].append(min_node)

        return visited, path

    def bellman_ford(self, start):
        nodes = list(self.w_graph.keys())
        v = len(nodes)
        dist = {i: float('inf') for i in nodes}
        dist[start] = 0
        for _ in range(v-1):
            for src, dest in self.w_graph.items():
                for d in dest:
                    destination = d[0]
                    weight = d[1]
                    if dist[src] + weight < dist[destination]:
                        dist[destination] = dist[src] + weight
                        
        for src, dest in self.w_graph.items():
            for d in dest:
                destination = d[0]
                weight = d[1]
                if dist[src] + weight < dist[destination]:
                    print('The graph contains negative cycle')
                    return
        print(dist)

                # import pdb; pdb.set_trace()

            # node = queue.pop(0)
            # print(node)
            # # print(self.w_graph.get(node, []))
            # for vert in self.w_graph.get(node, []):
            #     if vert[0] not in visited:
            #         queue.append(vert[0])
            #         visited.append(vert[0])
            #     if not path.get(vert[0]):
            #         path[vert[0]] = vert[1]
            #     elif path.get(vert[0]):
            #         if




    def __str__(self):
        for node in list(self.w_graph):
            print('{} : {}'.format(node, self.w_graph.get(node)))

def print_solution(nv, distance):

    for i in range(nv):
        for j in range(nv):
            if distance[i][j] == float('inf'):
                print(float('inf'), end=' ')
            else:
                print(distance[i][j], end=' ')
        print(' ')

def floyd_warshall(graph):
    distance = graph
    nv = len(graph)

    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

    print_solution(nv, distance)

graph = [
    [0,8,float('inf'),1],
    [float('inf'),0,1,float('inf')],
    [4,float('inf'),0,float('inf')],
    [float('inf'),2,9,1]
]

floyd_warshall(graph)
# wg = WeightedGraph()
# wg.add_edge('A', 'B', 2)
# wg.add_edge('A', 'C', 5)
# wg.add_edge('B', 'C', 6)
# wg.add_edge('B', 'D', 1)
# wg.add_edge('B', 'E', 3)
# wg.add_edge('C', 'F', 8)
# wg.add_edge('D', 'E', 4)
# wg.add_edge('E', 'G', 9)
# wg.add_edge('F', 'G', 7)

# print(wg.dijkstra('A'))
# print('==================')
# print(wg)

# wg.add_edge('A', 'C', 6)
# wg.add_edge('A', 'D', 6)
# wg.add_edge('B', 'A', 3)
# wg.add_edge('C', 'D', 1)
# wg.add_edge('D', 'C', 2)
# wg.add_edge('D', 'B', 1)
# wg.add_edge('E', 'B', 4)
# wg.add_edge('E', 'D', 2)

# wg.bellman_ford('E')



        
