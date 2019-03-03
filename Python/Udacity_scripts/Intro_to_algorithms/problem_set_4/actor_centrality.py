# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:08:20 2019

@author: roush

Calculating top 20 central actors from a given imdb file.

Here, centrality is the average distance from an actor to all other actors 
they have been in a movie with.
"""
import csv

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    #return G

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
    
graph = make_graph(read_graph_data('imdb-1.tsv'))