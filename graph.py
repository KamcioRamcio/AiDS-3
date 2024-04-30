import random 
import queue




# jakiś mądry człowiek powiedział, że naukowcy mówią nodes a nie verticles pozdro
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
    # Wazne: degree sie liczy, bo powino byc tak ze zaczynasz od node który ma degree 0 i idziej rosnaco
    def degree(self, node):
        return sum(1 for edges in self.adj_list.values() if node in edges)
    
    def Khan_Algorithm(self):
        # w naszym przypadku nie ma znaczenia czy to indegree czy outdegree bo jest to graf skierowany na 100%
        in_degree ={n: 0 for n in self.adj_list}
        for n in self.adj_list:
            for neighbour in self.adj_list[n]:
                in_degree[neighbour] += 1
        
        q = queue.Queue()
        for n in in_degree:
            if in_degree[n] == 0:
                q.put(n)
        
        order = []
        while not q.empty():
            node = q.get()
            order.append(node)
            
            for neighbour in self.adj_list[node]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    q.put(neighbour)
        
        # mozna jeszcze sprawcic czy nie ma cyklu w grafie nizej warunek
        if len(order) != len(self.adj_list):
            return print("Cykl w grafie")
        
        else:
            return order
        
    
    # Algorytm Tarjana
    # Ale to jest dym brachu
    # https://www.youtube.com/watch?v=_1TDxihjtoE spoko wytłumaczone
    #
    def Trajan_Algorithm(self):
        # Po ludzku wytłumacze bazowo kazdy wierzchołek ma index -1 ,sygnalizuje, że dla danego wierzchołka nie ustalono jescze indexu
        index = {n: -1 for n in self.adj_list}
        # Jest to wartość, która będzie reprezentować najniższy numer porządkowy w komponencie silnie spójnej dla danego wierzchołka.
        low_link = {n: -1 for n in self.adj_list}
        # Info czy dany wierzchołek jest na stosie czy nie
        on_stack = {n: False for n in self.adj_list}

        stack = []
        order = []
        
        # jak nie dałem tego w liste to nie działało 
        index_counter = [0]
        
        def strong_connect(node):
            index[node] = index_counter[0]
            low_link[node] = index_counter[0]
            index_counter[0] += 1
            stack.append(node)
            on_stack[node] = True
            
            for neighbour in self.adj_list[node]:
                if index[neighbour] == -1:
                    strong_connect(neighbour)
                    low_link[node] = min(low_link[node], low_link[neighbour])
                elif on_stack[neighbour]:
                    low_link[node] = min(low_link[node], index[neighbour])
            
            if low_link[node] == index[node]:
                component = []
                while True:
                    neighbour = stack.pop()
                    on_stack[neighbour] = False
                    component.append(neighbour)
                    if neighbour == node:
                        break
                order.extend(component)
            
        for node in self.adj_list:
            if index[node] == -1:
                strong_connect(node)
        return order
      
    def to_latex(self, filename):
        with open(filename, 'w') as f:
            f.write("\\documentclass{article}\n")
            f.write("\\usepackage{tikz}\n")
            f.write("\\begin{document}\n")
            f.write("\\begin{figure}\n")
            f.write("\\centering\n")
            f.write("\\begin{tikzpicture}[auto, node distance=2cm, every loop/.style={},]\n")
            for node in self.adj_list:
                # zamiast circle mona dawać rózne figury
                f.write(f"\\node[draw, circle] ({node}) at ({node * 360/self.nodes}:3cm) {{$ {node} $}};\n")
            for node, edges in self.adj_list.items():
                for neighbour in edges:
                    if neighbour != node:  
                        f.write(f"\\path[->] ({node}) edge node {{}} ({neighbour});\n")
            f.write("\\end{tikzpicture}\n")
            f.write("\\caption{Directed Graph}\n")
            f.write("\\end{figure}\n")
            f.write("\\end{document}\n")
            
#if __name__ == "__main__":
#    nodes = 10  # specify the number of nodes
#    saturation = 0.5  # specify the saturation
#    g = Graph(nodes)
#    g.generate(saturation)
#    g.table()
#    g.matrix()
#    print("Adjacency list:", g.adj_list)
#    print(g.BFS(0))
#    print(g.DFS(0))
#    print(g.degree(0))
#    print(g.Khan_Algorithm())
#    print(g.Trajan_Algorithm())
#    g.to_latex('graph.tex')


     