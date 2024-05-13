import graph
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--user-provided', action='store_true')
parser.add_argument('--generate', action='store_true')
args = parser.parse_args()

def main():
    g = None
    if args.user_provided:
        g = graph.Graph()
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
            g.print(type)
        except:
            print("Invalid input")
    g = graph.Graph()
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
                g.print(type)
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
            start, end = get_start_end()
            g.find_edge(start, end)
        elif command in ["bfs", "breadth first search"]:
            print(g.bfs())
        elif command == "print":
            g.print()
        elif command in ["dfs", "depth first search"]:
            print(g.dfs())
        elif command == "khan":
            g.khan()
        elif command == "tarjan":
            g.tarjan()
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