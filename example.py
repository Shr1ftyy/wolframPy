import networkx as nx
import matplotlib.pyplot as plt

'''

This is an example of the very first relation that Wolfram presents as an example:
{{x, y}, {x, z}} → {{x, z}, {x, w}, {y, w}, {z, w}}

'''

# Maximum iterations
ITERATIONS = 10

# Initializes graph
G = nx.Graph()

G.add_edge(1, 2) 
G.add_edge(2, 3) 
G.add_edge(3, 4) 
G.add_edge(2, 4) 

#Bruteforce search lmao
c = 0 
run = True
while run:
    print(c)
    foundy=False
    foundz=False
    for relation in G.edges:
        x = relation[0]
        for search in G.edges:
            if foundy == False:
                if search[0] == x:
                    y = search[1]
                    foundy == True
                    print('FOUND Y')
                else:
                    pass
            else:
                if search[0] == x:
                    if search[1] != y:
                        z = search[1]
                        foundz = True
                    print('FOUND Z')

        if foundy and foundz:
            G.add_edge(x,z)
            G.add_edge(x,9)
            G.add_edge(y,9)
            G.add_edge(z,9)
            c += 1
            break

        if c == ITERATIONS or (not foundy and not foundz):
            run == False


plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
# plt.subplot(122)

# nx.draw_shell(G, with_labels=True, font_weight='bold')

print(G.edges)

# Shows graph
plt.show()

