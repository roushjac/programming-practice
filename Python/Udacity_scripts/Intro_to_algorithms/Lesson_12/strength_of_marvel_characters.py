# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:46:31 2019

@author: roush

Creates a graph of marvel characters and the comics they appear in,
then puts a "strength" value on each link to find which two characters
have the strongest connection (appear in the same comics the most)
"""
import csv

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1

def make_graph(filename):
    actor_data = [row for row in csv.reader(open(filename), delimiter='\t')]
    # also find list of characters only
    character_list = set([row[0] for row in actor_data])
    G = {}
    for a, b in actor_data: make_link(G, a, b)
    return G, character_list # returns entire graph AND set of characters

def find_strongest_conn_strength(graph, characters):
    'Finds the two characters that share the most number of books/comics'
    strength_graph = {}
    for character in characters:
        strength_graph[character] = {}
        for book in graph[character]:
            for char_attached in graph[book]:
                if char_attached == character:
                    continue # dont find strength of character to itself
                if char_attached not in strength_graph[character]:
                    strength_graph[character][char_attached] = 1
                else:
                    strength_graph[character][char_attached] += 1
    strongest_conn_value = 1
    for char1 in strength_graph.keys():
        for char2 in strength_graph[char1]:
            if strength_graph[char1][char2] > strongest_conn_value:
                strongest_conn_value = strength_graph[char1][char2]
                strongest_conn_chars = [char1, char2]
    return strongest_conn_chars, strongest_conn_value
                    


graph, characters = make_graph(r'C:\Users\roush\Documents\Learning_Programming\Python\Udacity_scripts\Intro_to_algorithms\Lesson_12\marvel_graph.tsv')
print(find_strongest_conn_strength(graph, characters))