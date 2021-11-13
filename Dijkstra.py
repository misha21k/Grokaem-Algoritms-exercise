def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

while True:
    node = find_lowest_cost_node(costs, processed)
    if not node:
        break
    cost = costs[node]
    neighbors = graph[node]
    for neighbor in neighbors:
        new_cost = cost + neighbors[neighbor]
        if new_cost < costs[neighbor]:
            costs[neighbor] = new_cost
            parents[neighbor] = node
    processed.append(node)

print(costs)
print(parents)
