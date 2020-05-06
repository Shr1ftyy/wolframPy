import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

'''

This is an example of the very first relation that Wolfram presents as an example:
{(x, y), (x, z)} -> {(x, z), (x, w), (y, w), (z, w)}

Currently tweaking script to make it more general - general.py

'''

# Maximum iterations
ITERATIONS = 100

# Initializes graph
G = nx.Graph()

G.add_edge(1, 2) 
G.add_edge(2, 3) 
G.add_edge(3, 4) 
G.add_edge(2, 4) 

c = 0 
run = True

print(G.edges)
edges = list(G.edges)
print(edges[0])

# Cleans up input of relations
def clean():
    global x
    global y
    global z
    global edges
    global G

    edges = list(G.edges)

    # for relation in edges:
    #     if relation == (x,y) or relation == (x,z):
    #         G.remove_edge(*relation)

    for relation in edges:

#Bruteforce search lmao
while run:
    for relation in edges:
        foundy=False
        foundz=False
        x = relation[0]
        for search in edges:
            if foundy:
                # print('x: {x}\nsearch[0]: {search[0]}')
                # exit()

                if search[0] == x:
                    if search[1] != y:
                        z = search[1]
                        foundz = True

            else:
                if search[0] == x:
                    y = search[1]
                    foundy = True

        if foundy and foundz:
            clean()
            G.add_edge(x,z)
            G.add_edge(x,str(c))
            G.add_edge(y,str(c))
            G.add_edge(z,str(c))
            edges = list(G.edges)
            c += 1

        if c >= ITERATIONS: 
            print(c)
            run = False
            # print(edges)
            fig, ax = plt.subplots()
            ax.set_facecolor('black')
            nx.draw(G, with_labels=False, node_shape='.',node_color='w', edge_color='w', node_size=20)
            ax.set_facecolor('black')
            ax.axis('off')
            fig.set_facecolor('black')

            # Shows graph
            plt.show()
            exit()
