import random 
import queue
from collections import deque

# DO SPRAWOZDANIA
# Algorytm Khana nie działa w grafach z cyklami a Tarjana działa nawet ponoć jest specjalnie przstosowany do grafów z cyklami
# Ważne jest jednak zauważyć, że BFS w grafach skierowanych może nie odwiedzić wszystkich wierzchołków, jeśli nie ma ścieżki od startowego wierzchołka do pozostałych wierzchołków w grafie. Jednak nadal będzie działał poprawnie, odwiedzając wszystkie wierzchołki, do których jest ścieżka z wierzchołka początkowego.
# Dlatego dodałem funckję w main do wybrania wierzcołka od którego zaczynamy BFS i DFS

# jakiś mądry człowiek powiedział, że naukowcy mówią nodes a nie verticles pozdro
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {n: [] for n in range(1, nodes+1)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def generate(self, saturation):
        for u in range(1, self.nodes+1):
            for v in range(u + 1, self.nodes+1):
                if random.random() < saturation:
                    self.add_edge(u, v)
        max_edges = self.nodes * (self.nodes - 1) / 2
        actual_edges = sum(len(self.adj_list[v]) for v in range(1, self.nodes+1))
        
        while actual_edges > max_edges:
            u = random.randint(1, self.nodes)
            if self.adj_list[u]:
                self.adj_list[u].pop()
                actual_edges -= 1
                            
        

    def user_provided(self, edges_list):
        for u, v in edges_list:
            self.add_edge(u, v)
            
    def table(self):
        for node, edges in self.adj_list.items():
            print(f"{node}: {edges}")   
    
    def matrix(self):
    
        matrix = [[0]*self.nodes for _ in range(self.nodes)]
        for node, edges in self.adj_list.items():
            for edge in edges:
                matrix[node-1][edge-1] = 1
        print("    " + "  ".join(str(i) for i in range(1, self.nodes+1)))  
        print("--+" + "---"*self.nodes) 
        for i, row in enumerate(matrix, start=1):
            print(f"{i} | {'  '.join(str(cell) for cell in row)}")
    # lista to wystarczy dac print("Adjacency list:", g.adj_list) to bardziej taki słownik ale no niech będzie 
    
    # ty ja nie rozumiem troche tego 3 zadania podkunt 3, wyszkuwanie krawedzi grafu 
    def find(self, start, end):
        if start in self.adj_list:
            if end in self.adj_list[start]:
                return True
        return False
    # Znajdowanie najkrótszej sciezki w grafie oparte na BFS 
    def find_path(self, start, end):
        queue = deque([[start]])
        while queue:
            path = queue.popleft()
            node = path[-1]
            if node == end:
                return path
            for adjacent in self.adj_list.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        return None

        

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
    
    # Sprawdzanie czy graf jest cykliczny, zrobione for fun wsm
    def is_cyclic(self):
        visited = set()
        for node in self.adj_list:
            if node not in visited:
                if self._is_cyclic(node, visited, -1):
                    return True
        return False
    
    def _is_cyclic(self, node, visited, parent):
        visited.add(node)
        stack = set()  # Ensure that stack is a set

        for neighbour in self.adj_list[node]:
            if neighbour not in visited:
                if self._is_cyclic(neighbour, visited, node):
                    return True
            elif parent != neighbour:
                return True

        stack.add(node)  # Now it's safe to add node to stack
        return False
        # Algorytm Khana
    # Wazne: degree sie liczy, bo powino byc tak ze zaczynasz od node który ma degree 0 i idziej rosnaco
    #def degree(self, node):
    #    return sum(1 for edges in self.adj_list.values() if node in edges)
    
    
        
    
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
        
        # mozna jeszcze sprawcic czy nie ma cyklu w grafie nizej warunek, przydaje sie jak jest user-provided, dodałem to do maina
        if len(order) != len(self.adj_list):
            return None
        
        else:
            return order
        
    
    # Algorytm Tarjana
    # Ale to jest dym brachu
    # https://www.youtube.com/watch?v=_1TDxihjtoE spoko wytłumaczone
    # Rekurencyjny
    def Tarjan_Algorithm(self):
        # Po ludzku wytłumacze bazowo kazdy wierzchołek ma index -1 
        index = {n: -1 for n in self.adj_list}
        # Jest to wartość, która będzie reprezentować najniższy numer porządkowy w komponencie strong connect dla danego wierzchołka.
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
    
    #Iteracyjny Tarjan ale nie mój tylko wzorowany na tym co napisałem wyżej
    def Tarjan_Algorithm_2(self):
        index = {n: -1 for n in self.adj_list}
        low_link = {n: -1 for n in self.adj_list}
        on_stack = {n: False for n in self.adj_list}

        stack = []
        order = []
        index_counter = [0]

        def strong_connect(node):
            nodes_stack = [(node, iter(self.adj_list[node]))]
            while nodes_stack:
                node, children = nodes_stack[-1]
                if index[node] == -1:
                    index[node] = index_counter[0]
                    low_link[node] = index_counter[0]
                    index_counter[0] += 1
                    stack.append(node)
                    on_stack[node] = True

                try:
                    child = next(children)
                    if index[child] == -1:
                        nodes_stack.append((child, iter(self.adj_list[child])))
                    elif on_stack[child]:
                        low_link[node] = min(low_link[node], index[child])
                except StopIteration:
                    nodes_stack.pop()
                    if nodes_stack:
                        parent, _ = nodes_stack[-1]
                        low_link[parent] = min(low_link[parent], low_link[node])

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
            f.write("\\end{figure}\n")
            f.write("\\end{document}\n")
            


     