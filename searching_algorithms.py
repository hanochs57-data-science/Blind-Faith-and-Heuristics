import heapq
from collections import deque

# (Place,Distance in meters)
GRAPH = {
    'College': [('WEH', 1000), ('Chakala', 1500), ('C Cross', 3300),('Home', 6000), ('JB Nagar', 2500), ('Marol Naka', 3200), ('Gautam Nagar', 2600)],
    'WEH': [('College', 1000), ('Chakala', 500), ('C Cross', 2300),('Home', 5000), ('JB Nagar', 1500), ('Marol Naka', 1800), ('Gautam Nagar', 1600)],
    'Chakala': [('College', 1500), ('WEH', 500), ('C Cross', 1800),('Home', 4500), ('Gautam Nagar', 1100)],'C Cross': [('College', 3300), ('WEH', 2300), ('Chakala', 1800),('Home', 2700)],
    'JB Nagar': [('College', 2500), ('WEH', 1500), ('Marol Naka',300), ('Home', 1500)],'Marol Naka': [('College', 3200), ('WEH', 2200), ('JB Nagar',1700), ('Home', 700)],
    'Gautam Nagar': [('College', 2600), ('WEH', 1600), ('Chakala',1100), ('Home', 400)], 
    'Home': []
}

heuristic = {
    'College': 4000,
    'WEH': 3000,
    'Chakala': 2500,
    'Gautam Nagar': 400,
    'C Cross':2700,
    'JB Nagar': 1500,
    'Marol Naka': 700,
    'Home': 0
}

def astar(start, goal):
    queue = []
    heapq.heappush(queue, (heuristic[start], 0, start, [start]))
    visited = set()

    while queue:
        f_cost, g_cost, city, path = heapq.heappop(queue)

        if city == goal:
            return g_cost, path, len(visited)

        if city not in visited:
            visited.add(city)

            for neighbor, distance in GRAPH.get(city, []):
                if neighbor not in visited:
                    new_g = g_cost + distance
                    new_f = new_g + heuristic[neighbor]
                    heapq.heappush(queue, (new_f, new_g, neighbor,
path + [neighbor]))

    return None, [],len(visited)

def dfs(start, goal):
    stack = [(start, [start], 0)]  # (current_node, path, accumulative_cost)
    visited = set()

    while stack:
        node, path, cost = stack.pop()

        if node == goal:
            return cost, path, len(visited)+1

        if node not in visited:
            visited.add(node)
            for neighbor, distance in GRAPH.get(node, []):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor], cost + distance))
    return None, [],len(visited)

def bfs(start, goal):
    queue = deque([(start, [start], 0)])  # (current_node, path,accumulative_cost)
    visited = set()

    while queue:
        node, path, cost = queue.popleft()

        if node == goal:
            return cost, path, len(visited)+1

        if node not in visited:
            visited.add(node)
            for neighbor, distance in GRAPH.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor], cost + distance))
    return None, [],len(visited)

def ucs(start, goal):
    queue = [(0, start, [start])]  # (accumulative_cost, current_node, path)
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return cost, path, len(visited)+1

        if node not in visited:
            visited.add(node)
            for neighbor, distance in GRAPH.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + distance, neighbor,
path + [neighbor]))
    return None, [],len(visited)+1

def greedy_best_first(start, goal):
    queue = [(heuristic[start], start, [start], 0)]  # (heuristic,current_node, path, accumulative_cost)
    visited = set()

    while queue:
        _, node, path, cost = heapq.heappop(queue)

        if node == goal:
            return cost, path, len(visited)+1

        if node not in visited:
            visited.add(node)
            for neighbor, distance in GRAPH.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(queue, (heuristic[neighbor],neighbor, path + [neighbor], cost + distance))
    return None, [],len(visited)+1

# Execute and view execution output
cost, path,nodes_visited = astar('College', 'Home')
print("Shortest Path using A* Search: ")
print("Path: ", " -> ".join(path))
print("Total Cost: ", cost)
print("Nodes Explored: ",nodes_visited)
print()

cost, path, nodes_visited = dfs('College', 'Home')
print("Shortest Path using DFS: ")
print("Path: ", " -> ".join(path))
print("Total Cost: ", cost)
print("Nodes Explored: ",nodes_visited)
print()

cost, path,nodes_visited = bfs('College', 'Home')
print("Shortest Path using BFS: ")
print("Path: ", " -> ".join(path))
print("Total Cost: ", cost)
print("Nodes Explored: ",nodes_visited)
print()

cost, path,nodes_visited = ucs('College', 'Home')
print("Shortest Path using UCS: ")
print("Path: ", " -> ".join(path))
print("Total Cost: ", cost)
print("Nodes Explored: ",nodes_visited)
print()

cost, path,nodes_visited = greedy_best_first('College', 'Home')
print("Shortest Path using Greedy Best First Search: ")
print("Path: ", " -> ".join(path))
print("Total Cost: ", cost)
print("Nodes Explored: ",nodes_visited)
print()
