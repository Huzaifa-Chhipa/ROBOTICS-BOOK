import PrerequisiteDisplay from '@site/src/components/PrerequisiteDisplay';

---
title: "Sampling-Based Motion Planning"
description: "Efficiently exploring high-dimensional spaces."
slug: "chapter-02-sampling-based-motion-planning"
week: 7
module: "Module 3: Autonomous Navigation and Manipulation"
prerequisites: ["chapter-01-graph-search-algorithms"]
learningObjectives:
  - Understand the limitations of traditional graph search in high-dimensional spaces.
  - Grasp the fundamental principles of sampling-based motion planning.
  - Explore the Probabilistic RoadMap (PRM) algorithm and its construction phases.
  - Learn about the Rapidly-exploring Random Tree (RRT) algorithm for efficient space exploration.
  - Differentiate between RRT and RRT* and understand the concept of asymptotic optimality.
  - Recognize applications of sampling-based planners in various robotic scenarios.
estimatedTime: 120
difficultyLevel: "Intermediate"
sidebar_label: "2. Sampling-Based Motion Planning"
position: 2
---

<PrerequisiteDisplay prerequisites={frontMatter.prerequisites} />

# 🎲 Sampling-Based Motion Planning: Navigating High-Dimensional Worlds

In the previous chapter, we explored graph search algorithms like A\* for motion planning. While incredibly powerful for discrete and relatively low-dimensional environments (like 2D grids), these algorithms face a significant hurdle when dealing with robots that have many degrees of freedom (DoF) or operate in continuous, complex spaces. This challenge is known as the **curse of dimensionality**. As the number of dimensions increases, the size of the configuration space grows exponentially, making explicit graph construction (like an occupancy grid) computationally intractable. 🤯

This is where **sampling-based motion planning techniques** emerge as a powerful alternative. Instead of exhaustively searching a discretized space, these methods work by intelligently "sampling" points (configurations) in the robot's configuration space and building a representation of the free space on the fly. They are particularly effective when the explicit representation of the free configuration space (C-space) is too complex or impossible to compute. This chapter will introduce these efficient approaches, focusing on two cornerstone algorithms: the **Probabilistic RoadMap (PRM)**, which constructs a reusable roadmap of the environment, and the **Rapidly-exploring Random Tree (RRT)**, designed for rapid exploration towards a goal. We will also delve into RRT\* (RRT-Star), an optimal variant of RRT. Understanding these planners is crucial for enabling robots to find paths in cluttered and high-dimensional spaces, which is a common and critical challenge in advanced robotic manipulation and navigation. ✨

---

## The Curse of Dimensionality and Configuration Space (C-Space) 🌌

Before diving into sampling-based methods, let's revisit the concept of **Configuration Space (C-Space)**. For any robot, its configuration describes the precise state of all its joints and links. The C-space is the set of all possible configurations a robot can attain.

*   **Free C-Space (C_free):** All configurations where the robot does not collide with obstacles or itself.
*   **Obstacle C-Space (C_obstacle):** All configurations where the robot is in collision.

For a robot with `n` degrees of freedom, its C-space is `n`-dimensional.
*   A mobile robot moving on a 2D plane has 3 DoF (`x, y, θ`).
*   A 6-DoF robotic arm has 6 joint angles.

The **curse of dimensionality** states that the volume of the search space grows exponentially with the number of dimensions. For a high-DoF robot, explicitly discretizing the C-space (as a grid) to find collision-free paths becomes impossible due to:
*   **Memory:** Storing an `n`-dimensional grid.
*   **Computation:** Checking collisions for every cell in the grid.

Sampling-based planners overcome this by implicitly exploring the C-space.

---

## 🛣️ Probabilistic RoadMap (PRM): Building a Reusable Map

The **Probabilistic RoadMap (PRM)** algorithm is a multi-query planner. This means it builds a roadmap (a graph) of the environment once, and then this roadmap can be used to find paths for many different start and goal configurations. PRM is particularly effective for robots operating in static or slowly changing environments where multiple path queries are expected.

### PRM Algorithm Phases:

#### 1. Learning Phase (Roadmap Construction) 🛠️
This phase is performed offline or when the environment is known.

*   **Sampling:**
    *   Randomly generate a large number of `N` configurations (nodes) `q_i` within the C-space.
    *   For each sampled configuration, check if it's collision-free (i.e., `q_i ∈ C_free`). Discard collision states.
*   **Connection:**
    *   For each valid `q_i`, find its `k` nearest neighbors (or all neighbors within a certain radius).
    *   Attempt to connect `q_i` to these neighbors with a straight-line path (or simple local planner) in C-space.
    *   For each potential connection, perform a **local collision check** (e.g., discretize the path into small steps and check each step for collision). If the path is collision-free, add an edge to the roadmap graph.
    *   The edge can be weighted by its length (Euclidean distance in C-space).

#### 2. Query Phase (Pathfinding) 🔎
This phase is performed online whenever a path is needed.

*   **Connect Start and Goal:**
    *   Attempt to connect the start configuration `q_start` to the roadmap by finding its nearest neighbors in the roadmap and connecting it with collision-free paths.
    *   Do the same for the goal configuration `q_goal`.
*   **Search:**
    *   Once `q_start` and `q_goal` are connected to the roadmap, a standard graph search algorithm (like Dijkstra's or A\*, as discussed in the previous chapter) is used to find the shortest path between `q_start` and `q_goal` through the roadmap.

### Properties of PRM:
*   **Probabilistic Completeness:** Given enough samples and connections, PRM is guaranteed to find a path if one exists.
*   **Good for Multi-Query:** Once the roadmap is built, querying for new paths is fast.
*   **Difficulty with Narrow Passages:** If the free C-space contains narrow passages, many random samples might be needed to "discover" these passages, making it inefficient.

```python
# Python Pseudo-code Example: PRM Construction (Conceptual)
import numpy as np
import random
import matplotlib.pyplot as plt

class ConfigurationSpace:
    """Represents a simplified 2D configuration space with rectangular obstacles."""
    def __init__(self, x_min, x_max, y_min, y_max, obstacles):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.obstacles = obstacles # List of (x, y, width, height) tuples

    def is_collision_free(self, q):
        """Checks if configuration q = (x, y) is collision-free."""
        x, y = q
        # Check bounds
        if not (self.x_min <= x <= self.x_max and self.y_min <= y <= self.y_max):
            return False
        # Check against obstacles (simple rectangle collision)
        for ox, oy, ow, oh in self.obstacles:
            if ox < x < ox + ow and oy < y < oy + oh:
                return False
        return True

    def get_random_config(self):
        """Generates a random configuration."""
        x = random.uniform(self.x_min, self.x_max)
        y = random.uniform(self.y_min, self.y_max)
        return (x, y)

    def is_path_collision_free(self, q1, q2, steps=10):
        """Checks if a straight-line path between q1 and q2 is collision-free."""
        for i in range(steps + 1):
            t = i / steps
            q_intermediate = (q1[0] * (1 - t) + q2[0] * t, q1[1] * (1 - t) + q2[1] * t)
            if not self.is_collision_free(q_intermediate):
                return False
        return True

def prm_construction_conceptual(c_space, num_samples, num_neighbors):
    """
    Constructs a Probabilistic Roadmap (PRM).
    Args:
        c_space (ConfigurationSpace): The configuration space object.
        num_samples (int): Number of random configurations to sample.
        num_neighbors (int): Number of nearest neighbors to attempt connections.
    Returns:
        tuple: (nodes, edges) representing the roadmap graph.
    """
    nodes = []
    # 1. Sampling Phase
    print(f"Sampling {num_samples} configurations...")
    while len(nodes) < num_samples:
        q = c_space.get_random_config()
        if c_space.is_collision_free(q):
            nodes.append(q)
    
    edges = {} # Adjacency list representation
    for q in nodes:
        edges[q] = []

    # 2. Connection Phase
    print(f"Connecting sampled configurations (num_nodes={len(nodes)})...")
    for i, q1 in enumerate(nodes):
        # Find nearest neighbors
        distances = []
        for j, q2 in enumerate(nodes):
            if i == j: continue
            dist = np.linalg.norm(np.array(q1) - np.array(q2))
            distances.append((dist, q2))
        
        distances.sort()
        
        for k_neighbor_dist, q2 in distances[:num_neighbors]:
            if c_space.is_path_collision_free(q1, q2):
                edges[q1].append((q2, k_neighbor_dist)) # Store neighbor and distance (weight)
                edges[q2].append((q1, k_neighbor_dist)) # Bidirectional edge

    print("PRM construction complete. 🗺️")
    return nodes, edges

if __name__ == "__main__":
    # Define a simple 2D C-Space with obstacles
    obstacles = [
        (2.0, 2.0, 1.0, 4.0), # (x, y, width, height)
        (6.0, 4.0, 2.0, 1.0)
    ]
    c_space_2d = ConfigurationSpace(0, 10, 0, 10, obstacles)

    # Build PRM
    num_samples = 100
    num_neighbors = 5
    nodes_prm, edges_prm = prm_construction_conceptual(c_space_2d, num_samples, num_neighbors)

    # Plotting the PRM
    plt.figure(figsize=(8, 8))
    plt.xlim(c_space_2d.x_min, c_space_2d.x_max)
    plt.ylim(c_space_2d.y_min, c_space_2d.y_max)
    
    # Draw obstacles
    for ox, oy, ow, oh in c_space_2d.obstacles:
        plt.gca().add_patch(plt.Rectangle((ox, oy), ow, oh, fc='gray', ec='black'))

    # Draw nodes
    for q in nodes_prm:
        plt.plot(q[0], q[1], 'o', color='blue', markersize=3)
    
    # Draw edges
    for q1, neighbors in edges_prm.items():
        for q2, _ in neighbors:
            plt.plot([q1[0], q2[0]], [q1[1], q2[1]], 'k-', linewidth=0.5, alpha=0.5)

    plt.title('Probabilistic Roadmap (PRM) Construction')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.grid(True)
    plt.show()
    print("PRM visualization conceptual example finished. ✅")
```

---

## 🌳 Rapidly-exploring Random Tree (RRT): Efficient Exploration

The **Rapidly-exploring Random Tree (RRT)** algorithm is a single-query planner, meaning it builds a tree to find a path between a given start and goal for a specific query. RRT is designed for efficient exploration of high-dimensional C-spaces and is particularly good for finding *any* path quickly, even if it's not optimal.

### RRT Algorithm Steps:

1.  **Initialize Tree:** Start with the initial configuration `q_start` as the root of a tree `T`.
2.  **Sample Random Configuration:** Generate a random configuration `q_rand` from `C_space`.
3.  **Find Nearest Node:** Find the node `q_nearest` in `T` that is closest to `q_rand` (e.g., using Euclidean distance in C-space).
4.  **Extend Tree:** Attempt to extend the tree from `q_nearest` towards `q_rand` by a fixed step size `Δq`. This results in a new configuration `q_new`.
    *   Perform a **local collision check** along the path from `q_nearest` to `q_new`.
    *   If `q_new` is collision-free and the path is collision-free, add `q_new` to the tree `T` as a child of `q_nearest`.
5.  **Repeat:** Continue steps 2-4 until `q_new` is sufficiently close to `q_goal`.
6.  **Path Extraction:** Once the tree reaches `q_goal`, trace back from `q_goal` to `q_start` through the parent pointers to find the path.

### Properties of RRT:
*   **Probabilistic Completeness:** RRT is probabilistically complete.
*   **Rapid Exploration:** The random sampling and extension process naturally biases the tree to explore unvisited regions of the C-space, making it efficient for finding *a* path quickly.
*   **Non-Optimal Paths:** Paths found by basic RRT are generally not optimal (often jagged and longer than necessary).
*   **Single-Query:** Typically re-builds the tree for each new path query.
*   **Handles Constraints:** Can incorporate non-holonomic and kinodynamic constraints into the `Extend` step.

```python
# Python Pseudo-code Example: RRT Extension Step (Conceptual)
import numpy as np
import random
import matplotlib.pyplot as plt

class RRT_Node:
    def __init__(self, config, parent=None):
        self.config = config # (x, y)
        self.parent = parent

def rrt_extend_conceptual(c_space, tree, q_rand, step_size):
    """
    Performs one extension step of the RRT algorithm.
    Args:
        c_space (ConfigurationSpace): The configuration space object.
        tree (list): List of RRT_Node objects representing the tree.
        q_rand (tuple): The randomly sampled configuration.
        step_size (float): The maximum step size for extension.
    Returns:
        RRT_Node or None: The newly added node if extension is successful, else None.
    """
    # 1. Find q_nearest
    q_nearest = min(tree, key=lambda node: np.linalg.norm(np.array(node.config) - np.array(q_rand)))

    # 2. Extend from q_nearest towards q_rand
    vector_to_rand = np.array(q_rand) - np.array(q_nearest.config)
    distance = np.linalg.norm(vector_to_rand)
    
    if distance < step_size:
        q_new_config = q_rand
    else:
        q_new_config = tuple(np.array(q_nearest.config) + (vector_to_rand / distance) * step_size)
    
    # 3. Check for collision
    if c_space.is_path_collision_free(q_nearest.config, q_new_config):
        q_new_node = RRT_Node(q_new_config, parent=q_nearest)
        tree.append(q_new_node)
        return q_new_node
    else:
        return None

if __name__ == "__main__":
    # Re-use C_space from PRM example
    obstacles = [
        (2.0, 2.0, 1.0, 4.0), # (x, y, width, height)
        (6.0, 4.0, 2.0, 1.0)
    ]
    c_space_2d = ConfigurationSpace(0, 10, 0, 10, obstacles)

    q_start = (1.0, 1.0)
    tree_rrt = [RRT_Node(q_start)]
    
    step_size = 0.5
    num_iterations = 200

    print("Starting RRT expansion demo. 🌳")
    for _ in range(num_iterations):
        q_rand = c_space_2d.get_random_config()
        rrt_new_node = rrt_extend_conceptual(c_space_2d, tree_rrt, q_rand, step_size)
        
    # Plotting the RRT
    plt.figure(figsize=(8, 8))
    plt.xlim(c_space_2d.x_min, c_space_2d.x_max)
    plt.ylim(c_space_2d.y_min, c_space_2d.y_max)
    
    # Draw obstacles
    for ox, oy, ow, oh in c_space_2d.obstacles:
        plt.gca().add_patch(plt.Rectangle((ox, oy), ow, oh, fc='gray', ec='black'))

    # Draw tree nodes and edges
    for node in tree_rrt:
        plt.plot(node.config[0], node.config[1], 'o', color='blue', markersize=2)
        if node.parent:
            plt.plot([node.config[0], node.parent.config[0]], 
                     [node.config[1], node.parent.config[1]], 'k-', linewidth=0.5, alpha=0.5)

    plt.plot(q_start[0], q_start[1], 'o', color='green', markersize=8, label='Start')
    plt.title('RRT Tree Expansion')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.grid(True)
    plt.show()
    print("RRT visualization conceptual example finished. ✅")
```

---

## RRT\* (RRT-Star): Towards Optimal Paths 🌟

A major drawback of basic RRT is that the paths it finds are generally suboptimal. **RRT\* (RRT-Star)** is an extension of RRT that addresses this by guaranteeing **asymptotic optimality**: given enough samples and time, the path found by RRT\* will converge to the shortest possible path.

### Key Additions in RRT\*:

1.  **Choose Parent (Rewire from existing):** When a new node `q_new` is generated, instead of simply connecting it to `q_nearest`, RRT\* considers all nodes in its vicinity (`q_near`). It then chooses the parent from `q_near` that results in the lowest cost path from `q_start` to `q_new`.
2.  **Rewire:** After `q_new` is added to the tree, RRT\* checks if connecting `q_new` to any other node `q_in_near` from `q_near` would provide a *shorter path from `q_start` to `q_in_near`* than its current path. If so, `q_in_near` is rewired to become a child of `q_new`.

These two steps allow RRT\* to continuously optimize the tree by finding better paths as more samples are added, leading to smoother and shorter paths over time.

### Properties of RRT\*:
*   **Asymptotic Optimality:** The path cost converges to the optimal path cost as the number of samples approaches infinity.
*   **Probabilistic Completeness:** Like RRT, it will find a path if one exists.
*   **Slower than RRT:** The `ChooseParent` and `Rewire` steps add computational overhead, making each iteration slower than basic RRT.

---

## Comparison of Sampling-Based Planners 📊

| Feature                    | Probabilistic Roadmap (PRM)                     | Rapidly-exploring Random Tree (RRT)             | RRT\* (RRT-Star)                                |
| :------------------------- | :---------------------------------------------- | :---------------------------------------------- | :---------------------------------------------- |
| **Approach**               | Builds a graph (roadmap) in C-space             | Grows a single tree from start                  | Grows a single tree, continuously optimizes     |
| **Completeness**           | Probabilistic Complete                          | Probabilistic Complete                          | Probabilistic Complete                          |
| **Optimality**             | Optimal (if underlying graph search is optimal, e.g., A\*) | Not Optimal (finds any path)                    | Asymptotically Optimal                          |
| **Multi-Query**            | Yes (roadmap reusable)                          | No (single query)                               | No (single query)                               |
| **Computational Cost**     | High offline phase, fast online query           | Fast for single query                           | Slower than RRT per iteration (due to optimization) |
| **Handling Narrow Passages** | Can struggle (requires dense sampling)          | Explores well                                   | Explores well, improves paths in narrow passages |
| **Good For**               | Static environments, multiple path requests     | Dynamic environments, quick path finding        | Dynamic environments, optimal path finding (given time) |

---

## 🚀 Applications of Sampling-Based Motion Planning in Robotics

Sampling-based planners are essential for enabling complex robot behaviors:

*   **Robotic Manipulation:** Planning collision-free movements for high-DoF robotic arms in cluttered workspaces (e.g., manufacturing, service robotics, surgical robots).
*   **Autonomous Driving:** Used for local path planning in complex scenarios like parking, lane changes, or navigating through construction zones.
*   **Humanoid Robot Locomotion:** Planning stable and collision-free whole-body movements for complex humanoid robots.
*   **Aerial Vehicles (Drones):** Planning paths for drones through complex 3D environments, avoiding obstacles while reaching a target.
*   **Robotics in Hazardous Environments:** Exploring and navigating in disaster zones or space, where an explicit map may not be available or too complex.

---

## Conclusion: Mastering the Art of Robot Navigation 🌟

Sampling-based motion planning algorithms represent a powerful paradigm shift from traditional grid-based approaches, offering elegant solutions to the curse of dimensionality in high-DoF robotic systems. PRM provides a robust framework for multi-query scenarios in static environments, while RRT and its optimal variant, RRT\*, excel at rapidly exploring complex spaces to find paths, and eventually optimal paths. By understanding and applying these techniques, roboticists can empower autonomous systems to navigate intricate environments, perform complex manipulations, and achieve their goals with unprecedented efficiency and adaptability. The path to intelligent robot navigation is indeed a well-sampled one! ✨