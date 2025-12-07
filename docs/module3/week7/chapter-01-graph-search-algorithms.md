import PrerequisiteDisplay from '@site/src/components/PrerequisiteDisplay';

---
title: "Graph Search Algorithms"
description: "Finding paths in complex environments."
slug: "chapter-01-graph-search-algorithms"
week: 7
module: "Module 3: Autonomous Navigation and Manipulation"
prerequisites: []
learningObjectives:
  - Understand the role of graph search algorithms in robot motion planning.
  - Differentiate between uninformed search (BFS, DFS) and informed search (Dijkstra, A*).
  - Grasp the principles, advantages, and disadvantages of BFS, DFS, Dijkstra's, and A* algorithms.
  - Implement basic versions of these algorithms in Python.
  - Recognize the importance of heuristic functions in informed search.
estimatedTime: 180
difficultyLevel: "Intermediate"
sidebar_label: "1. Graph Search Algorithms"
position: 1
---

<PrerequisiteDisplay prerequisites={frontMatter.prerequisites} />

# 🔍 Graph Search Algorithms: Navigating Robot Paths

In the journey of autonomous robotics, simply knowing where a robot is (localization) and what its environment looks like (mapping) isn't enough. The robot also needs to figure out **how to get from its current location to a desired destination**. This is the fundamental problem of **motion planning**, and at its heart lies the power of **graph search algorithms**. These algorithms provide the computational intelligence for robots to find collision-free paths in complex, often dynamic, environments. 🗺️

This chapter delves into the core principles of graph search algorithms, which are indispensable tools for robot motion planning. We will begin by understanding how environments can be abstracted into graphs – collections of nodes (representing states or locations) and edges (representing possible transitions or movements). We'll then explore fundamental, **uninformed search algorithms** like Breadth-First Search (BFS) and Depth-First Search (DFS) for basic graph traversal. Building on this, we'll advance to **informed search algorithms** such as Dijkstra's algorithm, which finds the shortest path in weighted graphs, and the highly efficient A* (A-star) algorithm, which intelligently guides its search using heuristic functions. For each algorithm, we will discuss its underlying principles, analyze its computational complexity, and illustrate its practical applications in diverse robotic scenarios, from warehouse automation and autonomous driving to intricate planetary exploration. This foundational understanding will pave the way for tackling more advanced and complex motion planning techniques. ✨

---

## What is Motion Planning? The Role of Graphs 🤔

**Motion planning** is the process of finding a sequence of valid configurations that moves a robot from a start configuration to a goal configuration while satisfying certain constraints (e.g., avoiding obstacles, respecting joint limits).

The complexity of motion planning arises from:
*   **High Dimensionality:** Robots often have many degrees of freedom.
*   **Obstacles:** The environment is cluttered with static and dynamic obstacles.
*   **Dynamic Constraints:** Robot kinematics and dynamics impose limitations on how it can move.

### Representing the Environment as a Graph:
A common strategy in motion planning is to discretize the robot's environment or its configuration space into a **graph**.
*   **Nodes (Vertices):** Represent discrete states, locations, or configurations the robot can be in (e.g., free cells in an occupancy grid, specific joint angles, waypoints).
*   **Edges (Arcs):** Represent valid transitions or movements between nodes. These transitions must be collision-free and kinematically feasible. Edges can have associated **weights** representing the cost of traversing them (e.g., distance, time, energy consumption).

---

## Uninformed Search Algorithms: Exploring Systematically 🧠

Uninformed search algorithms operate without specific knowledge about the goal's location. They explore the search space systematically until the goal is found.

### 1. Breadth-First Search (BFS) 🌊
*   **Principle:** Explores all neighbor nodes at the current depth level before moving on to nodes at the next depth level. It effectively explores the graph "layer by layer."
*   **How it Works:** Uses a **queue** (FIFO - First-In, First-Out) to manage nodes to visit.
*   **Advantages:**
    *   **Completeness:** Guarantees to find a solution if one exists.
    *   **Optimality:** Guarantees to find the shortest path (in terms of number of edges) in an unweighted graph.
*   **Disadvantages:**
    *   **Memory Intensive:** Can consume a lot of memory, especially for wide graphs, as it needs to store all nodes at the current level.
    *   **Inefficient for Deep Goals:** Can be very slow if the goal is very deep in the graph.

```python
# Python Pseudo-code Example: Breadth-First Search (BFS) for pathfinding
from collections import deque

def bfs(graph, start, goal):
    """
    Finds the shortest path in an unweighted graph using BFS.
    Args:
        graph (dict): Adjacency list representation of the graph.
                      e.g., {'A': ['B', 'C'], 'B': ['D'], ...}
        start: Starting node.
        goal: Goal node.
    Returns:
        list: The shortest path from start to goal, or None if no path exists.
    """
    queue = deque([(start, [start])])  # (current_node, path_to_current_node)
    visited = {start}

    print(f"Starting BFS from {start} to {goal}...")

    while queue:
        current_node, path = queue.popleft()
        print(f"  Exploring node: {current_node}, Path so far: {path}")

        if current_node == goal:
            print(f"🎉 Goal reached! Path: {path}")
            return path

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
    
    print(f"❌ No path found from {start} to {goal}.")
    return None

if __name__ == "__main__":
    # Example Robot Environment (simplified grid as a graph)
    # Nodes could be free cells in an occupancy grid
    robot_grid_graph = {
        'S': ['A', 'B'],
        'A': ['S', 'C', 'D'],
        'B': ['S', 'E'],
        'C': ['A', 'F'],
        'D': ['A', 'G'],
        'E': ['B', 'H'],
        'F': ['C', 'G'],
        'G': ['D', 'F', 'goal'],
        'H': ['E']
    }
    
    start_node = 'S'
    goal_node = 'goal'
    path_bfs = bfs(robot_grid_graph, start_node, goal_node)
    if path_bfs:
        print(f"BFS found path: {path_bfs}")
    else:
        print("BFS could not find a path.")
```

### 2. Depth-First Search (DFS) 🌲
*   **Principle:** Explores as far as possible along each branch before backtracking. It goes "deep" down one path before exploring other options.
*   **How it Works:** Uses a **stack** (LIFO - Last-In, First-Out) or recursion to manage nodes.
*   **Advantages:**
    *   **Memory Efficient:** Much less memory-intensive than BFS for deep graphs, as it only needs to store the current path.
*   **Disadvantages:**
    *   **No Optimality Guarantee:** Does not guarantee finding the shortest path (can find a long path first).
    *   **Incompleteness (for infinite graphs):** Can get stuck in infinite loops or very deep branches if not carefully managed (e.g., with visited tracking).
*   **Applications:** Topological sorting, detecting cycles in graphs.

```python
# Python Pseudo-code Example: Depth-First Search (DFS) for pathfinding
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    print(f"  Exploring node: {start}, Path so far: {path}")

    if start == goal:
        print(f"🎉 Goal reached! Path: {path}")
        return path

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path)
            if result:
                return result
    
    return None

if __name__ == "__main__":
    robot_grid_graph = {
        'S': ['A', 'B'],
        'A': ['S', 'C', 'D'],
        'B': ['S', 'E'],
        'C': ['A', 'F'],
        'D': ['A', 'G'],
        'E': ['B', 'H'],
        'F': ['C', 'G'],
        'G': ['D', 'F', 'goal'],
        'H': ['E']
    }

    print("\nStarting DFS...")
    path_dfs = dfs(robot_grid_graph, 'S', 'goal')
    if path_dfs:
        print(f"DFS found path: {path_dfs}")
    else:
        print("DFS could not find a path.")
```

---

## Informed Search Algorithms: Guiding the Way with Heuristics 🌟

Informed search algorithms use additional information (a heuristic) to guide their search, prioritizing paths that appear more promising towards the goal. This makes them significantly more efficient than uninformed search for many problems.

### 1. Dijkstra's Algorithm 🛣️
*   **Principle:** Finds the shortest path from a single source node to all other nodes in a graph with non-negative edge weights. It explores the graph by always visiting the unvisited node with the smallest known distance from the start node.
*   **How it Works:** Uses a **priority queue** to efficiently retrieve the node with the minimum tentative distance.
*   **Advantages:**
    *   **Optimality:** Guarantees to find the shortest path in weighted graphs (if edge weights are non-negative).
    *   **Completeness:** Finds a path if one exists.
*   **Disadvantages:**
    *   **Explores All Directions:** Can explore many unpromising paths, making it slower than A* for finding a single destination.
    *   **Doesn't Use Heuristics:** No "goal-directed" guidance.
*   **Applications:** Network routing, finding shortest paths in road networks, resource allocation.

```python
# Python Pseudo-code Example: Dijkstra's Algorithm for shortest path
import heapq # Priority queue implementation

def dijkstra(graph, start, goal):
    """
    Finds the shortest path in a weighted graph using Dijkstra's algorithm.
    Args:
        graph (dict): Adjacency list with weights.
                      e.g., {'A': {'B': 1, 'C': 5}, 'B': {'D': 2}, ...}
        start: Starting node.
        goal: Goal node.
    Returns:
        list: The shortest path from start to goal, or None.
    """
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)] # (distance, node)

    print(f"Starting Dijkstra from {start} to {goal}...")

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we found a shorter path to current_node already, skip
        if current_distance > distances[current_node]:
            continue

        print(f"  Visiting node: {current_node}, current_distance: {current_distance}")

        if current_node == goal:
            break # Goal found!

        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    
    if path and path[0] == start: # Check if a path was actually found
        print(f"🎉 Goal reached! Path: {path}, Total Cost: {distances[goal]}")
        return path
    else:
        print(f"❌ No path found from {start} to {goal}.")
        return None

if __name__ == "__main__":
    weighted_graph = {
        'S': {'A': 1, 'B': 5},
        'A': {'S': 1, 'C': 2, 'D': 4},
        'B': {'S': 5, 'E': 1},
        'C': {'A': 2, 'F': 1},
        'D': {'A': 4, 'G': 1},
        'E': {'B': 1, 'H': 3},
        'F': {'C': 1, 'G': 1},
        'G': {'D': 1, 'F': 1, 'goal': 1},
        'H': {'E': 3}
    }
    
    start_node_dijkstra = 'S'
    goal_node_dijkstra = 'goal'
    path_dijkstra = dijkstra(weighted_graph, start_node_dijkstra, goal_node_dijkstra)
    if path_dijkstra:
        print(f"Dijkstra found path: {path_dijkstra}")
```

### 2. A* (A-star) Algorithm ⭐
The A* algorithm is one of the most popular and efficient pathfinding algorithms. It combines the advantages of Dijkstra's algorithm (guarantees shortest path) with a heuristic approach to guide the search, making it much faster.

*   **Principle:** It evaluates each node `n` using a cost function `f(n)`:
    `f(n) = g(n) + h(n)`
    *   `g(n)`: The actual cost from the start node to node `n`.
    *   `h(n)`: The estimated cost (heuristic) from node `n` to the goal node.
*   A* expands the node with the lowest `f(n)` value, prioritizing nodes that are both cheap to reach from the start and appear promising towards the goal.
*   **Heuristic Function `h(n)`:**
    *   **Admissibility:** A heuristic is **admissible** if it never overestimates the actual cost to reach the goal (i.e., `h(n) <= h*(n)` where `h*(n)` is the true cost). Admissible heuristics guarantee finding the optimal (shortest) path.
    *   **Consistency:** A heuristic is **consistent** if `h(n) <= cost(n, successor) + h(successor)`. Consistent heuristics are also admissible and ensure that `g(n)` is monotonically non-decreasing.
*   **Advantages:**
    *   **Optimality:** Guarantees the shortest path if the heuristic is admissible.
    *   **Optimally Efficient:** Explores the fewest nodes necessary to find the optimal path (given an admissible heuristic).
    *   **Goal-Directed:** The heuristic guides the search directly towards the goal.
*   **Disadvantages:**
    *   Heuristic design can be challenging and greatly impacts performance.
    *   Still memory intensive for large graphs like BFS.
*   **Applications:** Robot motion planning, game AI pathfinding, network routing.

```python
# Python Pseudo-code Example: A* Algorithm for shortest path
import heapq
import math # Needed for euclidean_distance_heuristic

def a_star(graph, start, goal, heuristic):
    """
    Finds the shortest path in a weighted graph using A* algorithm.
    Args:
        graph (dict): Adjacency list with weights.
                      e.g., {'A': {'B': 1, 'C': 5}, 'B': {'D': 2}, ...}
        start: Starting node.
        goal: Goal node.
        heuristic (func): A function that estimates the cost from a node to the goal.
                          heuristic(node, goal) -> estimated_cost
    Returns:
        list: The shortest path from start to goal, or None.
    """
    # g_score: cost from start to current node
    g_score = {node: float('infinity') for node in graph}
    g_score[start] = 0

    # f_score: estimated total cost from start to goal through current node
    f_score = {node: float('infinity') for node in graph}
    f_score[start] = heuristic(start, goal)

    previous_nodes = {node: None for node in graph}
    
    # Priority queue stores (f_score, node)
    priority_queue = [(f_score[start], start)]

    print(f"Starting A* from {start} to {goal}...")

    while priority_queue:
        current_f_score, current_node = heapq.heappop(priority_queue)

        # If we already found a better path to current_node, skip
        if current_f_score > f_score[current_node]:
            continue
        
        print(f"  Visiting node: {current_node}, f_score: {current_f_score}")

        if current_node == goal:
            break # Goal found!

        for neighbor, weight in graph.get(current_node, {}).items():
            tentative_g_score = g_score[current_node] + weight

            if tentative_g_score < g_score[neighbor]:
                previous_nodes[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(priority_queue, (f_score[neighbor], neighbor))
    
    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    
    if path and path[0] == start: # Check if a path was actually found
        print(f"🎉 Goal reached! Path: {path}, Total Cost: {g_score[goal]}")
        return path
    else:
        print(f"❌ No path found from {start} to {goal}.")
        return None

def euclidean_distance_heuristic(node, goal):
    """Example heuristic: Euclidean distance (assuming nodes are (x, y) tuples)."""
    # For this graph example, let's just make it a simple lookup.
    # In a real grid, this would be sqrt((x1-x2)^2 + (y1-y2)^2)
    # For now, let's create a dummy heuristic that guides towards the goal
    # Higher value for nodes further from goal for illustration.
    # This assumes we have coordinate info for each node.
    coords = {
        'S': (0,0), 'A': (1,0), 'B': (0,1),
        'C': (2,0), 'D': (1,1), 'E': (0,2),
        'F': (3,0), 'G': (2,1), 'H': (1,2),
        'goal': (3,1)
    }
    
    x1, y1 = coords.get(node, (0,0))
    x2, y2 = coords.get(goal, (0,0))
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


if __name__ == "__main__":
    weighted_graph_a_star = {
        'S': {'A': 1, 'B': 5},
        'A': {'S': 1, 'C': 2, 'D': 4},
        'B': {'S': 5, 'E': 1},
        'C': {'A': 2, 'F': 1},
        'D': {'A': 4, 'G': 1},
        'E': {'B': 1, 'H': 3},
        'F': {'C': 1, 'G': 1},
        'G': {'D': 1, 'F': 1, 'goal': 1},
        'H': {'E': 3}
    }
    
    start_node_a_star = 'S'
    goal_node_a_star = 'goal'
    path_a_star = a_star(weighted_graph_a_star, start_node_a_star, goal_node_a_star, euclidean_distance_heuristic)
    if path_a_star:
        print(f"A* found path: {path_a_star}")
```

---

## 🚀 Applications of Graph Search Algorithms in Robotics

These algorithms are not abstract concepts; they form the operational core of many autonomous systems:

*   **Warehouse Automation:** Automated Guided Vehicles (AGVs) and mobile robots use these algorithms to navigate aisles, find the shortest routes to pick-up and drop-off points, and avoid other robots or obstacles.
*   **Autonomous Driving:** While high-level planning, these algorithms are used for route selection (e.g., shortest route on a city map), and in more localized planning (e.g., finding a path through a parking lot).
*   **Robotic Arm Motion Planning:** Finding collision-free paths for multi-joint robot arms in cluttered workspaces. Here, nodes can represent joint configurations.
*   **Planetary Exploration:** Rovers (e.g., Mars Rovers) use graph-based planning to navigate challenging terrains, avoiding rocks and craters, with paths optimized for distance or energy.
*   **Game AI Pathfinding:** NPCs (Non-Player Characters) often use A* to find efficient paths in virtual environments.

---

## Path Smoothing: Making Robot Motion Natural 🛤️

Paths generated by grid-based graph search algorithms like A* are often jagged, consisting of straight lines along grid edges. While optimal in terms of grid cells, such paths are unnatural and inefficient for real robots (e.g., require frequent stops and sharp turns).

**Path smoothing techniques** are applied as a post-processing step to convert these piecewise-linear paths into smoother, more continuous, and kinematically feasible trajectories. Common methods include:
*   **Cubic Splines:** Fitting smooth curves through waypoints.
*   **Bezier Curves:** Generating smooth curves using control points.
*   **Elastic Band / CHOMP:** Optimization-based methods that "pull" the path taut while avoiding obstacles.

---

## Algorithm Comparison: Choosing the Right Tool 📊

| Algorithm      | Type       | Optimality (Shortest Path) | Completeness | Memory Usage  | Heuristic Used | Common Use Cases                        |
| :------------- | :--------- | :------------------------- | :----------- | :------------ | :------------- | :-------------------------------------- |
| **BFS**        | Uninformed | Yes (unweighted graphs)    | Yes          | High          | No             | Shortest path (unweighted), graph traversal |
| **DFS**        | Uninformed | No                         | No (infinite) | Low           | No             | Topological sort, cycle detection       |
| **Dijkstra's** | Informed   | Yes (non-negative weights) | Yes          | Medium/High   | No             | Shortest path (weighted), network routing |
| **A* **        | Informed   | Yes (admissible heuristic) | Yes          | Medium/High   | Yes            | Robot motion planning, game AI pathfinding |

---

## Conclusion: The Planner's Blueprint 📝

Graph search algorithms are fundamental to enabling robots to autonomously navigate and operate in complex environments. By providing efficient and often optimal methods for finding paths, they transform a robot's abstract understanding of space into concrete, actionable movement commands. From simple traversals to sophisticated goal-directed navigation, these algorithms serve as the planner's blueprint, guiding robots safely and effectively through their tasks. The journey to intelligent autonomy is indeed paved with well-planned paths! 🌟