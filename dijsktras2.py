

#create a grapb of all nodes and its neighbors

from concurrent.futures import process


graph= {
    'start': {
        'a': 5,
        'b': 2,
    },
    'a': {
        'c': 4,
        'd': 2
    },
    'b': {
        'a': 8,
        'd': 7
    },
    'c': {
        'd': 6,
        'fin': 3
    },
    'd': {
        'fin': 1
    },
    'fin': {}
}

costs = {
    'a': 5,
    'b': 2,
    'c': 9,
    'd': 9,
    'fin': float('inf')
}

parents = {
    'a': 'start',
    'b': 'start',
    'c': 'a',
    'd': 'b',
    'fin': None
}


processed_nodes = []
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed_nodes:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node:
    neighbors = graph[node]
    cost = costs[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    
    processed_nodes.append(node)
    node = find_lowest_cost_node(costs)


print(costs['fin'])