from graphviz import Digraph

g= Digraph()
# g.edge('new order', 'pending new')
# g.edge('pending new', 'engine ack')

g.node('A', 'new order')
g.node('B', 'pending new')
g.node('C', 'engine ack')
g.node('D', 'engine reject')

g.edges(['AB', 'BC', 'BD'])

g.render('graph.gv', view=True)
