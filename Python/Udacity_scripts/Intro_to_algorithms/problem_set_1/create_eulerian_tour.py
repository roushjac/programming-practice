# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:42:25 2019

@author: roush
"""
import random

def find_eulerian_tour(graph):
    final_tour = []
    final_tour.append(graph[0][0]) # add first node into tour
    remaining_paths = graph # initialize possible remaining paths
    while len(remaining_paths) > 0: # while first and last nodes aren't equal
        current_node = final_tour[-1] # most recently added node in tour
        final_tour.append(find_new_node(remaining_paths, current_node))
        remaining_paths = update_graph(remaining_paths, final_tour)
    return final_tour
    
def find_new_node(graph, current_node):
    # given a node and all connections, randomly pick a new node that's connected
    bool_graph = [current_node in x for x in graph] # list of true/false for possible nodes
    subset_graph = [i for i,v in zip(graph, bool_graph) if v] # boolean of possible nodes
    possible_nodes = set([x for one_conn in subset_graph for x in one_conn]) # set of possible nodes
    possible_nodes.remove(current_node)
    return random.choice(list(possible_nodes))
    
def update_graph(graph, nodes_visited):
    #return a graph that does not include paths already visited
    # only needs to remove combination of most recent element added plus one before
    #nodes_visited is a list - both possible combinations
    recently_visited = [[nodes_visited[-1], nodes_visited[-2]],[nodes_visited[-2], nodes_visited[-1]]]
    updated_graph = [x not in recently_visited for x in [list(y) for y in graph]] # boolean of remaining paths
    updated_graph = [i for i,v in zip(graph, updated_graph) if v]
    return updated_graph

a_graph = [(1,2),(1,3),(1,4),(1,6),(2,3),(2,4),(2,6),(3,4),(3,6),(4,5),(5,6)]
print(find_eulerian_tour(a_graph))