import random
import numpy as np
class Grpah:
    def __init__(self):
        self.matrix = []
        self.list = []
        self.table = []
        
    def generate(self,nodes,satrurtion,type):
        if 0 < satrurtion <= 1:
            if type == 'matrix':
                self.matrix = [[0]*nodes for _ in range(nodes)]
                for i in range(nodes):
                    for j in range(i+1, nodes):
                        if random.random() < satrurtion:
                            self.matrix[i][j] = 1
                return self.matrix   
                    
            elif type == 'list':
                for i in range(1, nodes+1):
                    for j in range(i+1, nodes+1):
                        if random.random() < satrurtion:
                            self.list.append((i, j))
                return self.list
            
            elif type == 'table':
                for i in range(1, nodes+1):
                    row = []
                    for j in range(i+1, nodes+1):
                        if random.random() < satrurtion:
                            row.append(j)
                    self.table.append(row)
                return self.table     
            else:
                print("Unknown type. Please try again.")
                self.generate(nodes,satrurtion,type)
        else:
            print("Saturation must be between 0 and 1.")
            
    def user_provided(self, nodes, type):
        if type == 'matrix':
            self.matrix = [[0]*nodes for _ in range(nodes)]
            i = 0
            while i < nodes:
                edges = list(map(int, input(f"{i+1}> ").split()))
                if len(edges) > nodes-1:
                    print(f"Node {i+1} has more edges than nodes or contains itself.")
                    continue
                else:
                    for edge in edges:
                        node = int(edge) - 1
                        if node == i:
                            print(f"Node {i+1} cannot have an edge with itself.")
                            break
                        if 0 <= node < nodes:
                            self.matrix[i][node] = 1
                        else:
                            print(f"Node {node+1} does not exist.")
                            break
                    else:  
                        i += 1
            return self.matrix
        elif type == 'list':
            i = 0
            while i < nodes:
                edges = list(map(int, input(f"{i+1}> ").split()))
                if len(edges) > nodes-1:
                    print(f"Node {i+1} has more edges than nodes or contains itself.")
                    continue
                else:
                    for edge in edges:
                        if edge == i+1:  
                            print(f"Node {i+1} cannot have an edge with itself.")
                            break
                        if 0 <= edge <= nodes:
                            self.list.append((i+1, edge))  
                        else:
                            print(f"Node {edge} does not exist.")
                            break
                    else:
                        i += 1
            return self.list
        elif type == 'table':
            i = 0
            while i < nodes:
                edges = list(map(int, input(f"{i+1}> ").split()))
                if len(edges) > nodes-1:
                    print(f"Node {i+1} has more edges than nodes or contains itself.")
                    continue
                else:
                    row = []
                    for edge in edges:
                        if edge == i+1:  
                            print(f"Node {i+1} cannot have an edge with itself.")
                            break
                        if 0 <= edge <= nodes:
                            row.append(edge)
                        else:
                            print(f"Node {edge} does not exist.")
                            break
                    else:
                        self.table.append(row)
                        i += 1
            return self.table
        else:
            print("Unknown type. Please try again.")
       
    def print(self,type):
        if type == 'matrix':
            self.print_matrix()
        elif type == 'list':
            self.print_list()
        elif type == 'table':
            self.print_table()
        else:
            print("Unknown type. Please try again.")
                 

    def print_matrix(self):
        print("    " + "  ".join(str(i) for i in range(1, len(self.matrix)+1)))
        print("--+" + "---"*len(self.matrix))
        for i, row in enumerate(self.matrix, start=1):
           print(f"{i} | {'  '.join(str(cell) for cell in row)}")
    
    def print_list(self):
        for i, j in self.list:
            print(f"{i} -> {j}")
        #if self.list[-1][0] == i:  
        #    print(f"{i+1} -> ")
        
        
    def print_table(self):
        for i, edges in enumerate(self.table, start=1):  
            print(f"Node {i}:", end=' ')
            for j in edges:
                print(f"{j}", end=' ')
            print()
     
    def find_edge(self,start,end):
        if self.matrix:
            if self.matrix[start-1][end-1] == 1:
                print(f"Edge {start} -> {end} exists.")
            else:
                print(f"Edge {start} -> {end} does not exists.")
        elif self.list:
            if (start,end) in self.list:
                print(f"Edge {start} -> {end} exists.")
            else:
                print(f"Edge {start} -> {end} does not exists.")
        elif self.table:
            if end in self.table[start-1]:
                print(f"Edge {start} -> {end} exists.")
            else:
                print(f"Edge {start} -> {end} does not exists.")
        else:
            print("Graph is empty.")
    def bfs(self,start):
        if self.matrix:
            visited = [False]*(len(self.matrix)+1)
            queue = []
            queue.append(start)
            visited[start] = True
            while queue:
                start = queue.pop(0)
                print(start, end = " ")
                for i in range(1,len(self.matrix)+1):
                    if self.matrix[start-1][i-1] == 1 and not visited[i]: 
                        queue.append(i)
                        visited[i] = True
        elif self.list:
            num_nodes = max(max(edge) for edge in self.list)
            visited = [False]*(num_nodes+1)
            queue = []
            queue.append(start)
            visited[start] = True
            while queue:
                start = queue.pop(0)
                print(start, end = " ")
                for i in self.list:
                    if i[0] == start and not visited[i[1]]:
                        queue.append(i[1])
                        visited[i[1]] = True
        elif self.table:
            visited = [False]*(len(self.table)+1)
            queue = []
            queue.append(start)
            visited[start] = True
            while queue:
                start = queue.pop(0)
                print(start, end = " ")
                for i in self.table[start-1]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True
        else:
            print("Graph is empty.")
    
    def dfs(self,start):
        if self.matrix:
            visited = [False]*(len(self.matrix)+1)
            stack = []
            stack.append(start)
            visited[start] = True
            while stack:
                start = stack.pop()
                print(start, end = " ")
                for i in range(1,len(self.matrix)+1):
                    if self.matrix[start-1][i-1] == 1 and not visited[i]: 
                        stack.append(i)
                        visited[i] = True
        elif self.list:
            num_nodes = max(max(edge) for edge in self.list) 
            visited = [False]*(num_nodes+1) 
            stack = []
            stack.append(start)
            visited[start] = True
            while stack:
                start = stack.pop()
                print(start, end = " ")
                for i in self.list:
                    if i[0] == start and not visited[i[1]]:
                        stack.append(i[1])
                        visited[i[1]] = True
        elif self.table:
            visited = [False]*(len(self.table)+1)
            stack = []
            stack.append(start)
            visited[start] = True
            while stack:
                start = stack.pop()
                print(start, end = " ")
                for i in self.table[start-1]:
                    if not visited[i]:
                        stack.append(i)
                        visited[i] = True
        else:
            print("Graph is empty.")             
    
    def khan(self):
        if self.matrix:
            in_degree = [0]*(len(self.matrix))
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    if self.matrix[i][j] == 1:
                        in_degree[j] += 1
            queue = []
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    queue.append(i)
            count = 0
            top_order = []
            while queue:
                u = queue.pop(0)
                top_order.append(u)
                for i in range(len(self.matrix)):
                    if self.matrix[u][i] == 1:
                        in_degree[i] -= 1
                        if in_degree[i] == 0:
                            queue.append(i)
                count += 1
            if count != len(self.matrix):
                print("Cycle in graph.")
            else:
                print("Khan: ", [node + 1 for node in top_order])
        elif self.list:
            num_nodes = max(max(edge) for edge in self.list)  # find the maximum value in self.list
            in_degree = [0] * num_nodes  # initialize in_degree with the number of nodes
            for i in range(len(self.list)):
                in_degree[self.list[i][1]-1] += 1
            queue = []
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    queue.append(i)
            count = 0
            top_order = []
            while queue:
                u = queue.pop(0)
                top_order.append(u)
                for i in range(len(self.list)):
                    if self.list[i][0]-1 == u:
                        in_degree[self.list[i][1]-1] -= 1
                        if in_degree[self.list[i][1]-1] == 0:
                            queue.append(self.list[i][1]-1)
                count += 1
            if count != num_nodes:
                print("Cycle in graph.")
            else:
                print("Khan: ", [node + 1 for node in top_order])
        elif self.table:
            in_degree = [0]*len(self.table)
            for i in range(len(self.table)):
                for j in self.table[i]:
                    in_degree[j-1] += 1
            queue = []
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    queue.append(i)
            count = 0
            top_order = []
            while queue:
                u = queue.pop(0)
                top_order.append(u)
                for i in range(len(self.table)):
                    if i == u:
                        for j in self.table[i]:
                            in_degree[j-1] -= 1
                            if in_degree[j-1] == 0:
                                queue.append(j-1)
                count += 1
            if count != len(self.table):
                print("Cycle in graph.")
            else:
                print("Khan: ", [node + 1 for node in top_order])
        else:
            print("Graph is empty.")      
    
    def tarjan_matrix(self):
        mark = ['unmarked']*len(self.matrix)
        order = []
        def visit(node):
               if mark[node] == 'temp':
                   print("Cycle in graph.")
                   return
               if mark[node] == 'unmarked':
                   mark[node] = 'temp'
                   for i in range(len(self.matrix)):
                       if self.matrix[node][i] == 1:
                           visit(i)
                   mark[node] = 'marked'
                   order.insert(0,node)
        for i in range(len(self.matrix)):
            visit(i)
        print("Tarjan: ", [node + 1 for node in order])    
    
    def tarjan_list(self):
        num_nodes = max(max(edge) for edge in self.list)
        mark = ['unmarked']*num_nodes
        order = []
        def visit(node):
            if mark[node] == 'temp':
                print("Cycle in graph.")
                return
            if mark[node] == 'unmarked':
                mark[node] = 'temp'
                for i in self.list:
                    if i[0] == node + 1:  # add 1 to node
                        visit(i[1]-1)  # subtract 1 from i[1]
                mark[node] = 'marked'
                order.insert(0,node)
        for i in range(num_nodes):
            visit(i)
        print("Tarjan: ", [node + 1 for node in order])
        
    def tarjan_table(self):
        mark = ['unmarked']*len(self.table)
        order = []
        def visit(node):
               if mark[node] == 'temp':
                   print("Cycle in graph.")
                   return
               if mark[node] == 'unmarked':
                   mark[node] = 'temp'
                   for i in self.table[node]:
                       visit(i-1)
                   mark[node] = 'marked'
                   order.insert(0,node)
        for i in range(len(self.table)):
            visit(i)
        print("Tarjan: ", [node + 1 for node in order])
    
    def tarjan(self):
        if self.matrix:
            self.tarjan_matrix()
        elif self.list:
            self.tarjan_list()
        elif self.table:
            self.tarjan_table()
        else:
            print("Graph is empty.")
    
    
           
            
                     
                    
            
if __name__ == "__main__":
    g = Grpah()
    g.user_provided(6,'list')
    g.khan()
    g.tarjan()
    g.bfs(1)
    print()
    g.dfs(1)

    
    