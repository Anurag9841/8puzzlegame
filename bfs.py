from queue import Queue
from Nodes import Node
import pydot
import numpy as np

def breadthfirstsearch(initial_state):
    graph = pydot.Dot(graph_type='digraph',fontsize="20", color="red",fontcolor="black",  style="filled")
    start_node = Node(initial_state, None, None,0)
    if start_node.goal_test():
        return start_node.solution()
    q = Queue()
    q.put(start_node)
    explored=[]
    killed=[]
    print("The starting node is \ndepth=%d" % start_node.depth)
    print(str(start_node.state))
    while not(q.empty()):
        node=q.get()
        print('\nthe node selected to expand is\ndepth='+str(node.depth)+"\n"+str(node.state))
        explored.append(node.state)
        graph.add_node(node.graph_node)
        if node.parent:
            diff=np.subtract(node.parent.state,node.state)
            if node.parent.state[2]==0:
                diff[0],diff[1]=-diff[0],-diff[1]
            graph.add_edge(pydot.Edge(node.parent.graph_node, node.graph_node,label=str([diff[0],diff[1]])))
        children=node.generate_child()
        if not node.is_killed():
            for child in children:
                if child.state not in explored:
                    if child.goal_test():
                        graph.add_node(child.graph_node)
                        diff = np.subtract(node.parent.state, node.state)
                        if node.parent.state[2] == 0:
                            diff[0], diff[1] = -diff[0], -diff[1]
                        graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node,label=str([diff[0],diff[1]])))
                        graph.write_png(f'Final_solution{node.depth}.png')
                        return child.solution()
                    if child.is_valid():
                        q.put(child)
                        explored.append(child.state)
            graph.write_png(f'Final_solution{node.depth}.png')
        else:
            killed.append("\""+str(node.state)+"\"")

    return
