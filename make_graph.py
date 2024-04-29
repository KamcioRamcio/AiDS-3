import random 
import matplotlib.pyplot as plt
import networkx as nx
from tabulate import tabulate


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
    
    def edge_serach(self, start, end):
        if start in self.adj.list:
            if end in self.adj_list[start]:
                return True
        return False
    def path_search(self,start,end):
        visited = [False]*self.nodes
        path = []
        self.path_search_util(start,end,visited,path)
        
    def path_search_util(self,start,end,visited,path):
        visited[start] = True
        path.append(start)
        if start == end:
            print(path)
        else:
            for i in self.adj_list[start]:
                if visited[i] == False:
                    self.path_search_util(i,end,visited,path)
        path.pop()
        visited[start] = False
    def shortest_path(self,start,end):
        visited = [False]*self.nodes
        path = []
        self.shortest_path_util(start,end,visited,path)
    
    
            
if __name__ == "__main__":
    nodes = 10  # specify the number of nodes
    saturation = 0.5  # specify the saturation
    g = Graph(nodes)
    g.generate(saturation)
#   g.table()
#   g.matrix()
#   print("Adjacency list:", g.adj_list)
#    
#    G = nx.DiGraph(g.adj_list)
#    nx.draw_spring(G, with_labels=True)
#    plt.show()
#
#    # Add edges from a list
#    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
#    g.user_provided(edges)
#
#    G = nx.DiGraph(g.adj_list)
#    nx.draw_spring(G, with_labels=True)
#    plt.show()