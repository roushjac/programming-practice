# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:08:20 2019

@author: roush

Calculating top 20 central actors from a given imdb file.

Here, centrality is the average distance from an actor to all other actors 
they have been in a movie with.
"""
import csv
import random

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1

def read_graph_data(filename):
    actor_data = [row for row in csv.reader(open(filename), delimiter='\t')]
    # make unique entries for movies with the same name but different years
    for row in range(len(actor_data)):
        actor_data[row][1] = actor_data[row][1] + ' ' + actor_data[row][2]
        del actor_data[row][2]
    return actor_data

def make_graph(data):
    G = {}
    for a, b in data: make_link(G, a, b)
    return G

def find_centrality(G, node):
    # finds centrality for one node - also returns the name of the node
    dist_from_start = {} # dictionary with distances to any node connected to input node
    todo_list = [node] # nodes to check for neighbors
    dist_from_start[node] = 0 # input node is 0 away from itself
    while len(todo_list) > 0:
        current_node = todo_list[0] # node currently having neighbors looked for
        del todo_list[0]
        for neighbor in G[current_node].keys():
            if neighbor not in dist_from_start:
                dist_from_start[neighbor] = dist_from_start[current_node] + 1
                todo_list.append(neighbor)
    return [node, sum(dist_from_start.values())/len(dist_from_start)]

def find_kth_centrality(actor_list, k):
    # finds the actor with the kth highest centrality and their centrality value
    pivot_element = actor_list[random.randint(0, len(actor_list)-1)]
    smaller = [x for x in actor_list if x[1] < pivot_element[1]]
    same = [x for x in actor_list if x[1] == pivot_element[1]]
    bigger = [x for x in actor_list if x[1] > pivot_element[1]]
    if len(smaller) == k or len(smaller) + len(same) == k: return pivot_element
    if len(smaller) < k and len(smaller) + len(same) > k: return pivot_element # k is in the middle of same + smaller
    if len(smaller) > k: return find_kth_centrality(smaller, k)
    if len(smaller) < k: return find_kth_centrality(bigger, k-len(smaller)-len(same))
    
    
actor_data = read_graph_data('imdb-1.tsv')
unique_actor_names = set([x[0] for x in actor_data]) # we are ultimately only interested in the 'actor' nodes

graph = make_graph(read_graph_data('imdb-1.tsv'))

actor_centralities = []
for actor in unique_actor_names:
    actor_centralities.append(find_centrality(graph, actor))

print(find_kth_centrality(actor_centralities, 20))
