graph = {}
graph["you"] = ["alice","bob","claire"]

graph["start"] = {}
graph["A"] = {}
graph["B"] = {}
graph["end"] = {}

graph["start"]["A"] = 6
graph["start"]["B"] = 2

graph["A"]["end"] = 1

graph["B"]["A"] = 3
graph["B"]["end"] = 5

inf = float("inf")

costs = {}
costs["A"] = 6
costs["B"] = 2
costs["end"] = inf

edges = {}
edges["A"] = "start"
edges["B"] = "start"
edges["end"] = None

process = []

print(graph["start"].keys())
print(graph["start"]["A"])
print(graph["start"]["B"])


def find_smallest_cost(costs):
    smallest_cost = float("inf")
    smallest_nodo_cost = None

    for nodo in costs:
        cost = costs[nodo]
        if cost < smallest_cost and nodo not in process:
            smallest_cost = cost
            smallest_nodo_cost = nodo
    return smallest_nodo_cost


nodo = find_smallest_cost(costs)

while nodo is not None:
    cost = costs[nodo]
    neighbors = graph[nodo]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            edges[n] = nodo
    process.append(nodo)
    nodo = find_smallest_cost(costs)
