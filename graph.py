import random 
import queue



# jakiś mądry człowiek powiedział, że naukowcy mówią edges a nie verticles pozdro
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {n: [] for n in range(nodes)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def generate(self, saturation):
        for u in range(self.nodes):
            for v in range(u + 1, self.nodes):
                if random.random() < saturation:
                    self.add_edge(u, v)
        # ile maksymalnie moze być maksymalnie wierzchołków zeby nadal grapf by acuklocizny i skierowany
        # nie ze jestem madry ludzie w internecie sa calkiem ogarnieci
        max_edges = self.nodes * (self.nodes - 1) / 2
        # ile podal uzytowknik wsm 
        actual_edges = sum(len(self.adj_list[v]) for v in range(self.nodes))
        
        while actual_edges > max_edges:
            u = random.randint(0, self.nodes - 1)
            if self.adj_list[u]:
                self.adj_list[u].pop()
                actual_edges -= 1
                
    

    def user_provided(self, edges_list):
        for u, v in edges_list:
            self.add_edge(u, v)
            
    def table(self):
        for node, edges in self.adj_list.items():
            print(f"Node {node}: {edges}")   
    
    def matrix(self):
        #trzeba dodac opisy kolumn i wierszy 
        matrix = [[0]*self.nodes for _ in range(self.nodes)]
        for node, edges in self.adj_list.items():
            for edge in edges:
                matrix[node][edge] = 1
        for row in matrix:
            print(' '.join(str(cell) for cell in row))  
    # def list wystarczy dac print("Adjacency list:", g.adj_list)
    
    # ty ja nie rozumiem troche tego 3 zadania podkunt 3, wyszkuwanie krawedzi grafu 
    def edge_serach(self, start, end):
        if start in self.adj.list:
            if end in self.adj_list[start]:
                return True
        return False
    
    # Przechodzenie wszerz grafu
    def BFS(self, start_node):
        visited = set()
        q = queue.Queue()
        q.put(start_node)
        order = []
        while not q.empty():
            node = q.get()
            if node not in visited:
                visited.add(node)
                order.append(node)
                for neighbour in self.adj_list[node]:
                    if neighbour not in visited:
                        q.put(neighbour)
        return order
    # przechodzenie w głąb grafu
    def DFS(self,start_node, visited = None):
        if visited is None:
            visited = set()
        order = []
        if start_node not in visited:
            visited.add(start_node)
            order.append(start_node)
            for neighbour in self.adj_list[start_node]:
                if neighbour not in visited:
                    order += self.DFS(neighbour, visited)
        return order
    # Algorytm Khana
    
    
    
    
    # Algorytm Tarjana
    
    
            
if __name__ == "__main__":
    nodes = 10  # specify the number of nodes
    saturation = 0.5  # specify the saturation
    g = Graph(nodes)
    g.generate(saturation)
#   g.table()
#   g.matrix()
    print("Adjacency list:", g.adj_list)
    print(g.BFS(0))
    print(g.DFS(0))
    
    