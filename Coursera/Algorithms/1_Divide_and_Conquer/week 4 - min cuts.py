# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 08:30:21 2021

@author: Taran
"""

'''
Quiz answers

1. n - 1

2. 

3. 2*alpha - 1

4. log(n)/-log(alpha)

5. 


Pset:
    

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
    print(simul_list)
    return min(simul_list)



## Function to load network data
def load_array(file_name="kargerMinCut.txt"):
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
        # for idx, edge in enumerate(network[node_keep]):
        #     if edge == node_keep:
        #         network[node_keep].pop(idx)
        while node_keep in network[node_keep]:
            network[node_keep].remove(node_keep)
        
    
    # remove all nodes that are not either of the remaining two
    # print(network)
    # for node in network:
    #     for edge in network[node]:
    #         if edge not in network.keys():
    #             network[node].pop(network[node].index(edge))
    
    # return cut represented by final 2 vertices
    # print(network)
    return len(network[list(network.keys())[0]])