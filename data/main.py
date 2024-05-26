import graph
import argparse
from timeit import default_timer as timer
import sys
sys.setrecursionlimit(30000)  # Increase the recursion depth limit to 3000
parser = argparse.ArgumentParser()
parser.add_argument('--user-provided', action='store_true')
parser.add_argument('--generate', action='store_true')
args = parser.parse_args()

def main():
    g = graph.Graph()
    if args.user_provided:
        
        type = get_type()
        nodes = get_nodes()
        try:
            g.user_provided(nodes, type)
            g.print(type)
        except:
            print("Invalid input")
        
    if args.generate:
        g = graph.Graph()
        type = get_type()
        nodes = get_nodes()
        saturation = get_saturation()
        try:
            g.generate(nodes, saturation, type)
            #g.print(type)
        except:
            print("Invalid input")
    
    while True:
        
        command = get_command()
        if command == "help":
            print_help()
        elif command == "exit":
            break
        elif command == "generate":
            type = get_type()
            nodes = get_nodes()
            saturation = get_saturation()
            try:
                g.generate(nodes, saturation, type)
                #g.print(type)
            except:
                print("Invalid input")
        elif command == "user-provided":
            type = get_type()
            nodes = get_nodes()
            try:
                g.user_provided(nodes, type)
                g.print(type)
            except:
                print("Invalid input")
        elif command == "find":
            start1 = timer()
            g.find_edge(1,nodes)
            end1 = timer()
            print(f"Time taken to find edge: {end1 - start1}")
        elif command in ["bfs", "breadth first search"]:
            print(g.bfs())
        elif command == "print":
            g.print(type)
        elif command in ["dfs", "depth first search"]:
            print(g.dfs())
        elif command == "khan":
            start2 = timer()
            g.khan()
            end2 = timer()
            print(f"Time taken khan {end2 - start2}")
        elif command == "tarjan":
            start3 = timer()
            g.tarjan()
            end3 = timer()
            print(f"Time taken tarjan {end3 - start3}")
        elif command == "draw":
            g.to_tikz()
        else:
            print("Invalid command. Type 'help' for a list of commands.")
            

def print_help():
    print('--- Help ---')
    print('Generate - generate a graph')
    print('User-provided - provide a graph')
    print('Print - print the graph')
    print('Find - finding edges of a graph ')
    print('BFS or Breadth First Search - graph breadth traversal ')
    print('DFS or Depth First Search - graph depth traversal ')
    print('Khan - Kahns algorithm (BFS-based)')
    print('Tarjan - Tarjans algorithm (DFS-based)')
    print('Draw - draw the graph in LaTeX')
    print('Exit - exit the program')

def get_command():
    return input('command> ').lower()
       
def get_nodes():
    while True:
        nodes_input = input('nodes> ')
        if nodes_input.isdigit():
            nodes = int(nodes_input)
            if nodes < 1:
                print("Invalid input. Please enter a positive integer.")
            else:
                return nodes
        else:
            print("Invalid input. Please enter a positive integer.")
            
def get_type():
    while True:
        type = input('type> ').lower()
        if type == 'matrix' or type == 'table' or type == 'list':
            return type
        else:
            print("Invalid type. Please enter 'matrix' , 'list' or 'table'.")
            
def get_saturation():
    return float(input('saturation> '))

def get_start_end():
    start = int(input('from> '))
    end = int(input('to> '))
    return start, end



if __name__ == "__main__":
    main()
    
    
    