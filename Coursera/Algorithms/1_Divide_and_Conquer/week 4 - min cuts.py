# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 08:30:21 2021

@author: Taran
"""

'''
Quiz answers

1. n - 1 (true for any tree - greatest num of min cuts is n choose 2)

2. All options where pr (output) for a min cut >= p (2 of 5)

3. 2*alpha - 1

4. log(n)/-log(alpha)

5. nC2 (for a graph with exactly one min cut, there's a 1/nC2 chance that the two vertices 
        s and t are on opp sides, so need to run nC2 times)

 
    
HW:
min cuts = 17


Final exam:

1. 4, 5, 9 (only smaller on left, only bigger on right)
2. 2 (2nd array should be [0,2,4,6,7])
3. theta(nlogn)
4. theta (nlogn) expected and theta(n^2) worst case
5. True only if f <= g for all n (otherwise depends on f and g - try f=5x, g=2x)
6. 1 - 2*alpha (check for 25%, 10% - think continuous, not discrete)
7. eps = (1-p)^n, since eps is prob of all failures, ie: 1-p, so log(eps)/log(1-p)
8. theta(nklog(k)) (run time = work per steps * steps = n elements * k arrays * logk steps)
9. theta(n^log(7))
10. Rate at which work-per-subproblem is shrinking (per level of recursion)

'''

## Visualize network of data
# import networkx as nx
import pandas as pd
import random
import itertools as it


# test network
x = {1: [2,3], 2: [1, 3, 4], 3: [1,2,4], 4: [2,3]}


def week_4(simuls=100):
    
    simul_list = []
    for i in range(simuls):
        simul_list.append(random_contractions(load_array(file_name="kargerMinCut.txt")))
    
    # x = pd.DataFrame.from_dict(data=load_array(), orient='index')
    # print(simul_list)
    return simul_list, min(simul_list)



## Function to load network data
def load_array(file_name="kargerMinCut.txt"):
    '''

    Parameters
    ----------
    file_name : txt file of network as adjcency matrix, optional
        Contains a representation of a graph. The default is "kargerMinCut.txt".

    Returns
    -------
    myDict : dictionary
        Contains linked list representation of network as a dictionary.

    '''
    # create dict for storing network
    myDict = {}
    
    # open file and make each element of dict a vertex with edges as list
    with open(file_name,"r") as txt_file:
        for line in txt_file.readlines():
            edges = [int(x) for x in line.split()]
            vertex = edges.pop(0)
            myDict[vertex] = edges
    
    return myDict


## Create one function to run the random contraction algorithm once
def random_contractions(network):
    '''

    Parameters
    ----------
    network : dictionary
        Representation of graph to compute min cut for.

    Returns
    -------
    TYPE
        Computes minimum cut of network (single iteration).

    '''
    # While there are more than 2 vertices
    while len(network.keys()) > 2:
    
        ## Pick a remaining edge (u, v) uniformly at random
        # Get list of every edge in network dict
        edge_list = []
        for node in network:
            edge_list += [(node, edge) for edge in network[node]]
        
        # Pick a random edge in list
        edge_to_merge = random.choice(edge_list)      
        # print(edge_list, edge_to_merge)

        
        ## Merge (u, v) into a single vertex
        # append all elements of network[u] to network[v]
        node_keep, node_remove = edge_to_merge
        network[node_keep] += network[node_remove]
                
        # remove network[v] from dict
        network.pop(node_remove, None)
        
        # Change node being removed to node keep for other nodes
        for node in network:
            for idx, edge in enumerate(network[node]):
                if edge == node_remove:
                     network[node][idx] = node_keep
        
        # Remove self-loops (any elements of u that equal u)
        while node_keep in network[node_keep]:
            network[node_keep].remove(node_keep)
        
    
    ## return cut represented by final 2 vertices
    # print(network)
    return len(network[list(network.keys())[0]])