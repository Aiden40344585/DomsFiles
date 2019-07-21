# Kruskal's algorithm for finding Minimum Spanning Tree
# for Graphs lecture
# this working script is deliberately not PEP8 compliant
N = 7 # number of nodes
# E contains edges in the format [node, node, weight]
E = [[1, 2, 7], [1, 4, 5], [2, 3, 8], [2, 4, 9],
     [2, 5, 7], [3, 5, 5], [4, 5, 15], [4, 6, 6],
     [5, 6, 8], [5, 7, 9], [6, 6, 11] ]

# Sort the edges, shortest first
E.sort(key=lambda a: a[2])
# Set of nodes that are in the mst
included = set() # ensures nodes can only be added once
# List of edges in MST
mst = []
while len(included)<N:
  h,E = E[0],E[1:] # h is the first edge
  print(f'checking edge {h}, nodes already added: {included}')
  print(f'edges remaining {E}')
  # Ignore edges where both nodes are included
  if h[0] in included and h[1] in included:
    pass # Do nothing - this is already there
  else:
    # Add both vertices to set of nodes
    included.add(h[0])
    included.add(h[1])
    mst.append(h) # add edge to mst
print (f'MST is {mst}')