'''
Finds the fastest path from start to finish.
We nees three graphs for this: Graph of all nodes, Costs and Parents
'''


#This is a graph of all nodes and its neighbors.
graph = {
    #Node
    'start': {
        #Neighbors and the corresponding distance.
        'a': 6,
        'b': 2
    },
    'a': {
        'fin': 1
    },
    'b': {
        'a': 3,
        'fin': 5
    },
    'fin': {}
}

#Costs graph
costs = {
    'a': 6,
    'b': 2,
    'fin': float('inf')
}

#Parents graph
parents = {
    'a': 'start',
    'b': 'start',
    'fin': None
}

#A list to keep track of processed nodes
processed_nodes = []


#A function to find the an unprocessed node with the cheapest cost
def node_with_cheapest_cost(costs):
    cheapest_cost = float('inf')
    cheapest_node = None

    for node in costs:
        if costs[node] < cheapest_cost and node not in processed_nodes:
            cheapest_cost = costs[node]
            cheapest_node = node
    
    return cheapest_node


node = node_with_cheapest_cost(costs)
while node is not None:
    print('loop')
    cost = costs[node]
    #update the cost of its neighbors
    neighbors = graph[node]
    for n in neighbors.keys():
        #update the costs and parents
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    #add node to processed nodes
    processed_nodes.append(node)
    #find the next cheapest node
    node = node_with_cheapest_cost(costs)


print(costs['fin'])