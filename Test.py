import pydot

graph = pydot.Dot(graph_type='digraph',strict = True)
# graph.add_edge(pydot.Edge("1","2"))
# graph.add_edge(pydot.Edge("1","2"))
# graph.add_edge(pydot.Edge("1","3"))

# print(graph)

graph.add_node(pydot.Node(name='1'))
graph.add_node(pydot.Node(name="2"))
graph.add_node(pydot.Node(name="3"))
graph.add_node(pydot.Node(name="4"))
graph.add_edge(pydot.Edge("1","2"))
graph.add_edge(pydot.Edge("1","3"))
graph.add_edge(pydot.Edge("1","4"))
graph.write_png("1.png")