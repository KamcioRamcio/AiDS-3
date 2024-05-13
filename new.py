import random

class Grpah:
    def __init__(self):
        self.matrix = []
        self.list = []
        self.table = []
        
    def generate(self,nodes,satrurtion,type):
        if type == 'matrix':
            if 0 < satrurtion < 1:
                self.matrix = [[random.choice([0, 1]) if j > i else 0 for j in range(nodes)] for i in range(nodes)]
        elif type == 'list':
            if 0 < satrurtion < 1:
                self.list = [(i, j) for i in range(1,nodes+1) for j in range(i+1, nodes+1) if random.choice([0, 1])]
        elif type == 'table':
            if 0 < satrurtion < 1:
                self.table = []
                for i in range(1, nodes+1):
                    row = []
                    for j in range(i+1, nodes+1):
                        if random.choice([0, 1]):
                            row.append(j)
                    self.table.append(row)
                        
        else:
            print("Unknown type. Please try again.")
            self.generate(nodes,satrurtion,type)
            
            
    def user_provided(self,nodes):
                
    
        
    def print_matrix(self):
        print("    " + "  ".join(str(i) for i in range(1, len(self.matrix)+1)))
        print("--+" + "---"*len(self.matrix))
        for i, row in enumerate(self.matrix, start=1):
           print(f"{i} | {'  '.join(str(cell) for cell in row)}")
    
    def print_list(self):
        for i, j in self.list:
            print(f"{i} -> {j}")
        
        
    def print_table(self):
        for i in self.table:
            for j in i:
                print(f"{j}",end=' ')
            print()
           
                    
            
if __name__ == "__main__":
    g = Grpah()
    nodes = int(input('nodes> '))
    satrurtion = float(input('satrurtion> '))
    type = input('type> ')
    g.generate(nodes,satrurtion,type)
    #print(g.matrix)
    #print(g.list)
    #g.print_list()
    #g.print_matrix()
    print(g.table)
    g.print_table()