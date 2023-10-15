import pydot
i = 0
graph = pydot.Dot(graph_type="digraph")
parent = dict()

def fib(n, node_num):
    global i
    current_node = (n, node_num)
    if node_num == 0:
        u = pydot.Node(str((n, node_num)), label=f"fib({n})")
        graph.add_node(u)
    else:
        u = pydot.Node(str(parent[current_node]), label=f"fib({parent[current_node][0]})",style='filled',fillcolor='gold')
        graph.add_node(u)
        v = pydot.Node(str(current_node),label=f"fib({n})")
        graph.add_node(v)
        edge = pydot.Edge(str(parent[current_node]),str(current_node))
        graph.add_edge(edge)

    if n <= 1:
        u = pydot.Node(str(current_node), label = f'fib({n})')
        graph.add_node(u)
        i+=1
        v = pydot.Node(str((n,i)),label=f"{n}")
        graph.add_node(v)
        edge = pydot.Edge(str(current_node),str((n,i)), dir='backward')
        graph.add_edge(edge)
        return n
    i += 1
    left_child =(n-1 , i)
    parent[left_child] = current_node
    i += 1
    right_child =(n-2, i)
    parent[right_child] = current_node
    return fib(*left_child) + fib(*right_child)
# n = 6
memo = dict()
parent[(7,0)] = None
fib(7,0)
graph.write_png('out.png')

