# Make eulerian tour out of a list of nodes

def create_tour(nodes):
    tour = []
    if len(nodes) % 2 == 1: # if number of nodes is odd
        # Every node is connected to every other node
        # iterate through nodes and create tuple out of every combination
        node_starting_pos = 0
        while node_starting_pos < len(nodes):
            node_current_pos = node_starting_pos # reset current position in nodes after incrementing up 1
            for incrementer in range(1, len(nodes) - node_current_pos):
                one_edge = (nodes[node_current_pos], nodes[node_current_pos + incrementer])
                tour.append(one_edge)
            node_starting_pos += 1
    else:
        # every node is connected except for the second to last node, which is only connected to adjacent nodes
        node_starting_pos = 0
        while node_starting_pos < len(nodes)-3: # stopping before last 2 nodes - special cases
            node_current_pos = node_starting_pos # reset current position in nodes after incrementing up 1
            for incrementer in range(1, len(nodes) - node_current_pos):
                one_edge = (nodes[node_current_pos], nodes[node_current_pos + incrementer])
                if one_edge[1] != nodes[-2]:
                    tour.append(one_edge)
            node_starting_pos += 1
        tour.append((nodes[-3], nodes[-2]))
        tour.append((nodes[-2], nodes[-1]))
    return tour