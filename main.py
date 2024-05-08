import graph
import argparse

#EOF
parser = argparse.ArgumentParser()
parser.add_argument('--user-provided', action='store_true')
args = parser.parse_args()

def main():
    g = None
    while True:
        command = get_command()
        if command == 'help':
            print_help()
        elif command == 'exit':
            break
        elif command == 'generate':
            nodes = get_nodes()
            saturation = get_saturation()
            print()
            g = graph.Graph(nodes)
            g.generate(saturation)
            #print()
            #g.table()
            #print()
            #g.matrix()
            #print()
            #print(g.adj_list)
            print('end of generate')
        elif command == 'user-provided':
            nodes = get_nodes()
            g = graph.Graph(nodes)
            for i in range(1, nodes+1):
                edges = get_edges(i, nodes)
                for edge in edges:
                    g.add_edge(i, edge)
            g.table()
        elif command == 'print':
            type = get_type()
            print_graph(g, type)
        elif command == 'find':
            start, end = get_start_end()
            print(g.find(start, end))
        elif command == 'find path':
            start, end = get_start_end()
            #print(g.find_path(start, end))
            print('end of find path')
            benchmark_find_path(g, start, end)
        elif command == 'cycle':
            if g.is_cyclic() == True:
                print("Graph has a cycle")
            else:
                print("Graph has no cycle")
            
        elif command in ['dfs', 'bfs']:
            dfs_bfs(g, command)
        elif command in ['khan', 'tarjan']:
            khan_tarjan(g, command)
        elif command == 'draw':
            g.to_latex('graph.tex')
        else:
            print("Unknown command. Please try again. Type help for more information.")

def print_help():
    print('--- Help ---')
    print('Generate - generate a graph')
    print('User-provided - provide a graph')
    print('Matrix - show the matrix of the graph')
    print('List - show the list of the graph')
    print('Table - show the table of the graph')
    print('Print - print the graph in the selected representation')
    print('Find - finding edges of a graph ')
    print('Find path - finding a path between two nodes in a graph')
    print('BFS or Breadth First Search - graph breadth traversal ')
    print('DFS or Depth First Search - graph depth traversal ')
    print('Khan - Kahns algorithm (BFS-based)')
    print('Tarjan - Tarjans algorithm (DFS-based)')
    print('Draw - draw the graph in LaTeX')
    print('Exit - exit the program')
    print('Cycle - check if the graph has a cycle')

def get_command():
    return input('command> ').lower()

def get_nodes():
    return int(input('nodes> '))

def get_saturation():
    return float(input('saturation> '))


def get_edges(node, total_nodes):
    while True:
        edges = list(map(int, input(f"    {node}> ").split()))
        if node in edges:
            print("Self-cycles are not allowed. Please enter the edges again.")
        elif 0 in edges:
            print("0 is not a valid edge. Please enter the edges again.")
        elif len(edges) > total_nodes:
            print("Too many edges. Please enter the edges again.")
        else:
            return edges

def get_start_end():
    start = int(input('from> '))
    end = int(input('to> '))
    return start, end
def get_type():
    return input('type> ')


def print_graph(g, type):
    if type == 'matrix':
        g.matrix()
    elif type == 'list':
       print(g.adj_list)
    else:
        g.table()


def dfs_bfs(g, command):
    for start_node in range(1, g.nodes + 1):
        if command == "bfs":
            visited = g.BFS(start_node)
        else:
            visited = g.DFS(start_node)
        
        if len(visited) == g.nodes:
            print(f"Starting from node {start_node}")
            print('inline:  ','  '.join(map(str, visited)))
            break
        else:
            print('Graph is not connected, cant be traversed from any node')
            break
def khan_tarjan(g, command):
    if command == "khan":
        if g.Khan_Algorithm() == None:
            print("Graph has a cycle")
        else:  
            #print('inline:  ','  '.join(map(str, g.Khan_Algorithm())))
            benchmark_khan_algorithm(g)
            print('end of khan')
    else:
        #print('inline:  ','  '.join(map(str, g.Tarjan_Algorithm())))
        benchmark_tarjan_algorithm(g)
        print('end of tarjan')




#benchmark
import time
import sys
import numpy as np
sys.setrecursionlimit(10**9)

def benchmark_find_path(g, start, end):
    start_time = time.time()
    g.find_path(start, end)
    end_time = time.time()
    print(f"Time taken to find edges: {end_time - start_time} seconds")

def benchmark_khan_algorithm(g):
    start_time = time.time()
    g.Khan_Algorithm()
    end_time = time.time()
    print(f"Time taken for Khan's algorithm: {end_time - start_time} seconds")

def benchmark_tarjan_algorithm(g):
    start_time = time.time()
    g.Tarjan_Algorithm_2()
    end_time = time.time()
    print(f"Time taken for Tarjan's algorithm: {end_time - start_time} seconds")








if __name__ == "__main__":
    main()