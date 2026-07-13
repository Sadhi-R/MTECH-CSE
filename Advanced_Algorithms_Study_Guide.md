# Advanced Algorithms (25CS21PC) — Complete Study Guide
**VCET Hyderabad | VR25 | M.Tech CSE I Year II Sem | Credits: 3**

---

## Table of Contents
1. [Syllabus Overview](#syllabus-overview)
2. [Previous Paper Analysis](#previous-paper-analysis)
3. [Unit I — Sorting & Graphs](#unit-i--sorting--graphs)
4. [Unit II — Matroids & Graph Matching](#unit-ii--matroids--graph-matching)
5. [Unit III — Flow Networks & Matrix Computations](#unit-iii--flow-networks--matrix-computations)
6. [Unit IV — Dynamic Programming, CRT & FFT](#unit-iv--dynamic-programming-crt--fft)
7. [Unit V — Linear Programming & NP-Completeness](#unit-v--linear-programming--np-completeness)
8. [Semester Preparation Checklist](#semester-preparation-checklist)

---

## Syllabus Overview

| Unit | Topics |
|------|--------|
| **I** | Sorting review, Topological sort, Graph definitions, BFS shortest path, Dijkstra, DFS, Strongly Connected Components, Amortized analysis |
| **II** | Matroids, Greedy paradigm, MST, Graph matching, Augmenting paths, Edmond's Blossom algorithm |
| **III** | Max-flow min-cut, Ford-Fulkerson, Edmond-Karp, Strassen's algorithm, LUP decomposition |
| **IV** | Floyd-Warshall, Dynamic programming, CRT, DFT/FFT, Schonhage-Strassen multiplication |
| **V** | Linear programming, Simplex algorithm, NP-completeness, NP-hardness proofs |

**Textbook:** *Introduction to Algorithms* (CLRS), *Algorithm Design* (Kleinberg & Tardos)

---

## Previous Paper Analysis

### Mid-I (May 2026) — Descriptive Questions Asked
| # | Question | Unit | Confidence for Sem |
|---|----------|------|-------------------|
| 1 | BFS & DFS with algorithms | I | **Very High (95%)** |
| 2 | DAG + Topological Sort | I | **Very High (95%)** |
| 3 | Shortest Path + Warshall's technique | I/IV | **High (85%)** |
| 4 | Amortized Analysis with example | I | **High (80%)** |
| 5 | Matroids + MST application | II | **Very High (90%)** |
| 6 | Ford-Fulkerson & Edmonds-Karp | III | **Very High (90%)** |

### Mid-II (July 2025) — Descriptive Questions Asked
| # | Question | Unit | Confidence for Sem |
|---|----------|------|-------------------|
| 1 | Matrix operation time complexities | III | **High (85%)** |
| 2 | LUP decomposition | III | **Very High (90%)** |
| 3 | Floyd-Warshall + DP + limitations | IV | **Very High (95%)** |
| 4 | CRT + polynomial interpolation | IV | **High (80%)** |
| 5 | Simplex limitations | V | **High (85%)** |
| 6 | NP-complete definition + challenges | V | **Very High (95%)** |

### Frequently Repeated Concepts (All Papers Combined)
- BFS/DFS traversal — **Highest weightage**
- Dijkstra's algorithm — **Highest weightage**
- Topological Sort / DAG — **Very High**
- Ford-Fulkerson / Edmonds-Karp — **Very High**
- Floyd-Warshall — **Very High**
- Matroids & MST — **High**
- NP-completeness — **High**
- Strassen / LUP — **Medium-High**

### Likely Semester Exam Questions (Predictions)
| Question | Confidence |
|----------|-----------|
| BFS/DFS with graph example | 95% |
| Dijkstra step-by-step | 90% |
| Ford-Fulkerson max flow | 90% |
| Floyd-Warshall all-pairs shortest path | 90% |
| NP-completeness proof (SAT or Vertex Cover reduction) | 85% |
| Edmond's Blossom / Matching | 75% |
| FFT / CRT | 70% |
| Simplex algorithm geometry | 75% |

---

## Unit I — Sorting & Graphs

### Unit I — Top Expected Questions
**Top 10:** BFS, DFS, Dijkstra, Topological Sort, DAG, Amortized Analysis, Sorting comparison, SCC, Negative weights, MST preview  
**Top 5 Short:** Why BFS gives shortest path?, Negative weights in Dijkstra, SCC definition, Amortized vs worst-case, DFS complexity  
**Top 5 Long:** BFS/DFS algorithms, DAG + Topological Sort, Dijkstra with example, Sorting comparison, Amortized analysis  
**Must Read:** BFS, DFS, Dijkstra, Topological Sort, Amortized Analysis

---

### SHORT ANSWER 1: Why does BFS give the shortest path in an unweighted graph?

**Definition:** BFS (Breadth-First Search) explores a graph **level by level** — first all nodes 1 step away, then 2 steps, and so on.

**Key Points:**
1. BFS uses a **Queue** (FIFO — First In First Out) — nodes discovered first are processed first.
2. In an unweighted graph, every edge has cost = 1. BFS always reaches a node via the **minimum number of edges**.
3. When BFS first visits a node, that path is guaranteed to be the shortest because no shorter path exists (all shorter paths would have been explored in earlier levels).

**Example:** Google Maps finding shortest route when all roads are equal distance — BFS explores ring-by-ring from source.

**Exam Keyword:** *Level-order traversal, Queue, O(V+E)*

**One-line Revision:** BFS uses Queue → explores level-by-level → first visit = shortest path in unweighted graphs.

---

### SHORT ANSWER 2: Why is Dijkstra's algorithm not suitable for negative edge weights?

**Definition:** Dijkstra's algorithm finds the **shortest path from one source** to all other nodes in a graph with **non-negative** edge weights.

**Key Points:**
1. Dijkstra assumes once a node is marked "done" (shortest distance found), that distance never changes.
2. With **negative edges**, a later path through a negative edge could make a previously "done" node's distance smaller — breaking the algorithm.
3. Use **Bellman-Ford** algorithm for graphs with negative weights.

**Example:** Flight with a "discount coupon" edge (negative cost) can make a longer-looking route actually cheaper — Dijkstra would miss this.

**Exam Keyword:** *Greedy choice fails with negative weights, use Bellman-Ford*

**One-line Revision:** Negative edges break Dijkstra's "finalized node" assumption → use Bellman-Ford instead.

---

### SHORT ANSWER 3: What is a Strongly Connected Component (SCC)?

**Definition:** In a **directed graph**, an SCC is a maximal set of vertices where **every vertex can reach every other vertex** in that set.

**Key Points:**
1. "Maximal" means you cannot add any more vertices while keeping full reachability.
2. Found using **Kosaraju's** or **Tarjan's** algorithm (both use DFS).
3. A directed graph may have multiple SCCs.

**Example:** Social network "follow" graph — each SCC is a group where everyone follows everyone (directly or indirectly).

**Exam Keyword:** *Directed graph, mutual reachability, DFS-based*

**One-line Revision:** SCC = maximal group in directed graph where every node reaches every other node.

---

### SHORT ANSWER 4: How does Amortized Analysis differ from Worst-Case Analysis?

**Definition:** **Amortized analysis** gives the **average cost per operation** over a sequence of operations, even if some individual operations are expensive.

**Key Points:**
1. **Worst-case:** Cost of ONE operation in the worst scenario (e.g., O(n) for one insert).
2. **Amortized:** Total cost of n operations divided by n (e.g., Dynamic array insert = O(1) amortized).
3. Methods: Aggregate, Accounting, Potential method.

**Example:** Warehouse adding boxes — sometimes the entire shelf must be rebuilt (expensive), but on average each addition is cheap.

**Exam Keyword:** *Average over sequence, Dynamic array, Aggregate method*

**One-line Revision:** Worst-case = single operation cost; Amortized = average cost over many operations.

---

### SHORT ANSWER 5: Time Complexity of DFS

**Definition:** DFS (Depth-First Search) visits every vertex and explores every edge once using a **Stack** (or recursion).

**Key Points:**
1. Time: **O(V + E)** where V = vertices, E = edges.
2. Each vertex visited once, each edge examined once.
3. Space: O(V) for recursion stack/visited array.

**Example:** Maze solving — DFS goes deep into one path before backtracking.

**Exam Keyword:** *O(V+E), Stack/Recursion, Backtracking*

**One-line Revision:** DFS time = O(V+E) — visit each vertex and edge exactly once.

---

### LONG ANSWER: BFS and DFS with Algorithms

#### 1. Definition
- **BFS:** Explores graph level-by-level using a Queue.
- **DFS:** Explores as deep as possible before backtracking, using Stack/Recursion.

#### 2. Introduction
Graph traversal means visiting every node in a graph systematically. BFS and DFS are the two fundamental traversal techniques used in routing, social networks, and scheduling.

#### 3. Why Needed
- Find shortest paths (BFS in unweighted graphs)
- Detect cycles, connected components
- Topological sorting (DFS)
- Solve puzzles (maze, Sudoku)

#### 4. Working Principle
- **BFS:** Start at source → enqueue → dequeue → visit unvisited neighbors → repeat.
- **DFS:** Start at source → mark visited → recursively visit unvisited neighbors → backtrack.

#### 5. Step-by-Step Explanation

**BFS Steps:**
1. Create Queue, Visited array
2. Enqueue source, mark visited
3. While queue not empty: dequeue front node, enqueue all unvisited neighbors
4. Repeat until all reachable nodes visited

**DFS Steps:**
1. Create Visited array
2. Call DFS(source): mark visited, for each unvisited neighbor call DFS(neighbor)
3. Backtrack when no unvisited neighbors remain

#### 6. Architecture
```
Graph:     A --- B --- D
            \         /
             C --- E

BFS from A:  Level 0: A
             Level 1: B, C
             Level 2: D, E
             Order: A → B → C → D → E

DFS from A:  A → B → D → E → C  (goes deep first)
```

#### 7. Algorithm (Pseudocode)

```
BFS(G, source):
    queue ← empty queue
    visited[source] ← true
    enqueue(queue, source)
    while queue is not empty:
        u ← dequeue(queue)
        for each neighbor v of u:
            if not visited[v]:
                visited[v] ← true
                enqueue(queue, v)

DFS(G, u):
    visited[u] ← true
    for each neighbor v of u:
        if not visited[v]:
            DFS(G, v)
```

#### 8. Flowchart (Text)
```
BFS: START → Init Queue → Enqueue Source → Queue empty? 
  → YES: END | NO: Dequeue → Visit Neighbors → Enqueue Unvisited → Loop

DFS: START → Visit Node → Any unvisited neighbor? 
  → YES: DFS(neighbor) → Loop | NO: Backtrack → END
```

#### 9. Real-Time Example
**Google Maps (BFS):** Finding shortest route when all roads equal — explore all roads 1 hop away, then 2 hops, etc.

**Social Network (DFS):** Finding all friends-of-friends chain — go deep into one friend's network before exploring another.

#### 10. Advantages
| BFS | DFS |
|-----|-----|
| Shortest path in unweighted graph | Less memory in some cases |
| Finds nearest nodes first | Good for cycle detection |
| Used in level-order problems | Used in topological sort |

#### 11. Disadvantages
| BFS | DFS |
|-----|-----|
| More memory (Queue stores entire level) | May not find shortest path |
| Not ideal for deep graphs | Can get stuck in deep paths |

#### 12. Applications
- BFS: Shortest path, GPS navigation, network broadcasting
- DFS: Cycle detection, topological sort, maze solving, SCC

#### 13. Exam Tips
- Always draw the graph and show visited order
- Mention data structure: Queue for BFS, Stack for DFS
- Write time complexity O(V+E) for both

#### 14. Common Mistakes
- Using Stack for BFS (wrong — must use Queue)
- Not marking nodes as visited (infinite loop)
- Confusing BFS order with DFS order

#### 15. Difference Table

| Feature | BFS | DFS |
|---------|-----|-----|
| Data Structure | Queue | Stack/Recursion |
| Exploration | Level-by-level | Depth-first |
| Shortest Path (unweighted) | Yes | No |
| Memory | O(width of graph) | O(depth of graph) |
| Time Complexity | O(V+E) | O(V+E) |

#### 16. Time Complexity: **O(V + E)** for both

#### 17. Space Complexity: **O(V)** for visited array + Queue/Stack

#### 18. Interview Questions
- When would you choose BFS over DFS?
- How does BFS work for shortest path?
- How to detect cycle using DFS?

#### 19. One-line Revision
BFS = Queue + level-order + shortest path; DFS = Stack + depth-first + backtracking.

#### 20. 5-Mark Summary
Define BFS and DFS. Write pseudocode for both. Draw graph example showing traversal order. State data structures used. Give time complexity O(V+E).

#### 21. 10-Mark Answer
Full definitions, both algorithms with pseudocode, worked graph example with step-by-step traversal and visited nodes, comparison table, applications, complexity analysis.

#### 22. Semester Exam Version
Illustrate BFS and DFS with algorithms on a given graph. Show queue/stack contents at each step, final traversal order, and explain why BFS finds shortest paths in unweighted graphs.

**Memory Trick:** **B**FS = **B**readth = **B**ig Queue | **D**FS = **D**epth = **D**ive (Stack)

---

### LONG ANSWER: DAG and Topological Sorting

#### 1. Definition
- **DAG:** Directed Acyclic Graph — a directed graph with **no cycles**.
- **Topological Sort:** Linear ordering of vertices such that for every edge u→v, u comes before v.

#### 2. Introduction
Used when tasks have dependencies — you must complete prerequisites before dependent tasks.

#### 3. Why Needed
- Course prerequisite scheduling
- Build systems (compile order)
- Task scheduling in projects
- Detecting cycles in dependencies

#### 4. Working Principle
Use DFS or Kahn's algorithm (BFS with in-degree). Process nodes with no incoming edges first.

#### 5. Step-by-Step (Kahn's Algorithm)
1. Compute in-degree of all vertices
2. Enqueue all vertices with in-degree 0
3. While queue not empty: dequeue u, add to result, reduce in-degree of neighbors, enqueue if in-degree becomes 0
4. If result size < V, graph has a cycle (not a DAG)

#### 6. Example Graph
```
Courses:  OS → Networks → Cloud
          OS → DB → Cloud
          Math → OS

In-degrees: Math=0, OS=1, DB=1, Networks=1, Cloud=2
Topological Order: Math → OS → DB → Networks → Cloud
```

#### 7. Algorithm
```
TopologicalSort(G):
    compute in-degree[v] for all v
    queue ← all v with in-degree 0
    result ← empty
    while queue not empty:
        u ← dequeue(queue)
        append result, u
        for each neighbor v of u:
            in-degree[v] ← in-degree[v] - 1
            if in-degree[v] == 0:
                enqueue(queue, v)
    if |result| < |V|: return "Cycle exists"
    return result
```

#### 8. Time Complexity: **O(V + E)**

#### 9. Applications
Course scheduling, software build dependencies, spreadsheet formula evaluation

#### 10. Exam Tips
- Topological sort ONLY works on DAGs
- Mid-I MCQ answer: Directed Acyclic Graphs (option d)
- Match the following: DAGs ↔ topological sort applicable

#### 11. One-line Revision
DAG = no cycles; Topological Sort = linear order respecting all edge directions.

#### 12. 5-Mark Summary
Define DAG. Explain topological sort. Give Kahn's algorithm. Show example. State O(V+E) complexity.

---

### LONG ANSWER: Dijkstra's Algorithm (Step-by-Step with Example)

#### 1. Definition
Dijkstra's algorithm finds the **shortest path from a single source** to all other vertices in a graph with **non-negative edge weights**.

#### 2. Introduction
Named after Edsger Dijkstra (1959). Used in GPS, network routing, and game AI pathfinding.

#### 3. Why Needed
When edges have different costs (distances, times), BFS fails — we need a greedy approach that always picks the closest unvisited node.

#### 4. Working Principle
Maintain distance array. Always pick the unvisited node with minimum distance (using Min-Heap). Relax all its neighbors.

#### 5. Step-by-Step
1. Initialize dist[source] = 0, all others = ∞
2. Use Min-Priority Queue (Heap)
3. Extract minimum distance node u
4. For each neighbor v of u: if dist[u] + weight(u,v) < dist[v], update dist[v]
5. Repeat until all nodes processed

#### 6. Example
```
Graph:  A --4-- B
        |       |
        2       1
        |       |
        C --3-- D

Find shortest from A:
Step 1: dist={A:0, B:∞, C:∞, D:∞}, visit A
Step 2: Update B=4, C=2, dist={A:0, B:4, C:2, D:∞}
Step 3: Pick C (min=2), update D=5
Step 4: Pick B (min=4), update D=5 (no improvement)
Step 5: Pick D (min=5)
Final: A→C=2, A→B=4, A→D=5 (via C: A→C→D = 2+3=5)
```

#### 7. Algorithm (Pseudocode)
```
Dijkstra(G, source):
    dist[v] ← ∞ for all v; dist[source] ← 0
    PQ ← min-heap with (0, source)
    while PQ not empty:
        (d, u) ← extract-min(PQ)
        if d > dist[u]: continue
        for each edge (u,v,w):
            if dist[u] + w < dist[v]:
                dist[v] ← dist[u] + w
                insert (dist[v], v) into PQ
    return dist
```

#### 8. Time Complexity
- With Binary Heap: **O((V+E) log V)**
- With Fibonacci Heap: **O(E + V log V)**

#### 9. Space Complexity: **O(V)**

#### 10. Exam Tips (Mid-I Fill-in-blanks)
- Dijkstra solves **Single-Source Shortest Path** problems
- Data structure: **Heap** (Priority Queue)
- Cannot use **negative** weights

#### 11. One-line Revision
Dijkstra = Greedy + Min-Heap + relax edges → single-source shortest path, no negative weights.

#### 12. 5-Mark Summary
Define, explain greedy choice, write algorithm, solve small example, state O((V+E)log V) with heap.

---

### LONG ANSWER: Sorting Algorithms Comparison (5 Algorithms)

| Algorithm | Best | Average | Worst | Space | Stable? | Method |
|-----------|------|---------|-------|-------|---------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Compare & swap adjacent |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Insert into sorted portion |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Find min, swap to front |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | Divide & Conquer |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Partition around pivot |

**Exam MCQ Answers (Mid-I):**
1. Adjacent compare & swap → **Bubble Sort**
2. Quick sort on sorted array C1 < C2 (fewer comparisons on sorted) → **C1 < C2**
3. Bubble sort best case → **Already sorted ascending**
4. Selection sort comparisons → **n(n-1)/2 ≈ n²/2**

**One-line Revision:** Merge/Quick = O(n log n) best general; Bubble/Insertion/Selection = O(n²) simple but slow.

---

## Unit II — Matroids & Graph Matching

### Unit II — Top Expected Questions
**Must Read:** Matroids, Greedy + MST, Dijkstra (again), Augmenting paths, Edmond's Blossom, Hungarian algorithm

---

### SHORT ANSWER: Define Matroids and Greedy Paradigm

**Definition:** A **Matroid** is a mathematical structure (E, I) where E is a ground set and I is a collection of **independent sets** satisfying: hereditary property, augmentation property, and maximality.

**Key Points:**
1. Greedy algorithm on matroids always gives **optimal solution**.
2. **MST problem** is a matroid — greedy (Kruskal/Prim) works optimally.
3. Greedy paradigm: make locally best choice at each step hoping for global optimum.

**Example:** Selecting maximum-weight independent set in a matroid = like picking best non-conflicting tasks.

**Exam Keyword:** *Independent sets, Greedy optimality, MST application*

**One-line Revision:** Matroid = structure where Greedy always works; MST is a classic matroid example.

---

### SHORT ANSWER: What is an Augmenting Path?

**Definition:** In matching problems, an **augmenting path** is a path that alternates between non-matching and matching edges, starting and ending at **unmatched (free) vertices**.

**Key Points:**
1. Flipping edges along an augmenting path **increases matching size by 1**.
2. A matching is **maximum** iff no augmenting path exists.
3. Edmond's Blossom algorithm handles augmenting paths in general graphs.

**Example:** Assigning workers to jobs — augmenting path finds a way to reassign to include one more worker.

**Exam Keyword:** *Free vertices, alternating path, maximum matching*

**One-line Revision:** Augmenting path = alternating path between free vertices → increases matching by 1.

---

### LONG ANSWER: Matroids and Application to MST

#### 1. Definition
Matroid M = (E, I): E = finite set, I = independent subsets. Greedy selection of max-weight independent set is optimal.

#### 2. MST as Matroid
- Ground set E = all edges
- Independent set = edges forming a **forest** (no cycles)
- Greedy (Kruskal): sort edges by weight, add if doesn't create cycle

#### 3. Kruskal's Algorithm
```
Kruskal(G):
    sort edges by weight ascending
    MST ← empty
    for each edge (u,v,w) in sorted order:
        if adding (u,v) doesn't create cycle:
            add to MST
    return MST
```
**Time:** O(E log E)

#### 4. Prim's Algorithm
Grow tree from source, always add minimum-weight edge connecting tree to outside.
**Time:** O(E log V) with heap

#### 5. Comparison: Kruskal vs Prim

| Feature | Kruskal | Prim |
|---------|---------|------|
| Approach | Sort all edges | Grow from source |
| Data Structure | Union-Find | Priority Queue |
| Best for | Sparse graphs | Dense graphs |
| Time | O(E log E) | O(E log V) |

#### 6. Real Example
**Warehouse delivery network:** Connect all warehouses with minimum total cable length — MST gives optimal network.

#### 7. Exam Tips
- Mid-I MCQ: Greedy for max-weight independent set in matroid → **Greedy algorithm**
- MST greedy algorithm → **Kruskal** (or Prim)

#### 8. One-line Revision
Matroid guarantees greedy optimality; MST = graphic matroid; Kruskal/Prim = greedy MST algorithms.

---

### LONG ANSWER: Ford-Fulkerson and Edmonds-Karp Algorithm

#### 1. Definition
**Max Flow:** Maximum amount of "flow" from source s to sink t in a flow network.  
**Min Cut:** Minimum capacity edges whose removal disconnects s from t.  
**Max-Flow Min-Cut Theorem:** Maximum flow = minimum cut capacity.

#### 2. Ford-Fulkerson Method
1. Start with flow = 0
2. While augmenting path exists in **residual graph**:
   - Find path from s to t with available capacity
   - Push maximum possible flow along path
   - Update residual graph
3. Stop when no augmenting path → maximum flow found

#### 3. Residual Graph
For each edge (u,v) with capacity c and flow f:
- Forward residual capacity = c - f
- Backward edge (v,u) with capacity f (to allow undoing flow)

#### 4. Edmonds-Karp Algorithm
Ford-Fulkerson + **BFS** to find shortest augmenting path (fewest edges).
**Time Complexity:** O(V × E²)

#### 5. Example
```
Network: s → A (cap 10) → t (cap 10)
         s → B (cap 5)  → t (cap 5)
Max Flow = 15
Min Cut = {edges from s} with total capacity 15
```

#### 6. Algorithm (Edmonds-Karp)
```
EdmondsKarp(G, s, t):
    while BFS finds augmenting path p in residual graph:
        bottleneck ← min residual capacity on p
        augment flow along p by bottleneck
        update residual graph
    return total flow
```

#### 7. Applications
- Network routing, airline scheduling, bipartite matching, image segmentation

#### 8. Exam Tips
- **Residual graph** significance: allows flow redistribution
- Mid-I descriptive Q6: Explain both Ford-Fulkerson AND Edmonds-Karp
- Difference: Edmonds-Karp uses BFS → polynomial time guarantee

#### 9. One-line Revision
Ford-Fulkerson = augmenting paths in residual graph; Edmonds-Karp = Ford-Fulkerson + BFS → O(VE²).

#### 10. 5-Mark Summary
Define max-flow min-cut theorem. Explain residual graph. Write Edmonds-Karp steps. Show small example. State O(VE²).

---

## Unit III — Flow Networks & Matrix Computations

### LONG ANSWER: Strassen's Matrix Multiplication

#### 1. Definition
Strassen's algorithm multiplies two n×n matrices in **O(n^log₂7) ≈ O(n^2.81)** time using Divide and Conquer.

#### 2. Standard vs Strassen

| Operation | Standard | Strassen |
|-----------|----------|----------|
| Multiplication | O(n³) | O(n^2.81) |
| Addition | O(n²) | O(n²) |

#### 3. Working Principle
Split each matrix into 4 sub-matrices (n/2 × n/2). Compute 7 special products (M1-M7) instead of 8, then combine.

#### 4. The 7 Products
```
M1 = (A11 + A22)(B11 + B22)
M2 = (A21 + A22)B11
M3 = A11(B12 - B22)
M4 = A22(B21 - B11)
M5 = (A11 + A12)B22
M6 = (A21 - A11)(B11 + B12)
M7 = (A12 - A22)(B21 + B22)
```

#### 5. Mid-II MCQ Answers
- Paradigm: **Divide and Conquer**
- Used for: **Multiplication**
- Time complexity match: **O(n^log₂7)**

#### 6. One-line Revision
Strassen = Divide & Conquer + 7 recursive multiplies → O(n^2.81) matrix multiplication.

---

### LONG ANSWER: LUP Decomposition

#### 1. Definition
**LUP decomposition** factors matrix A into **A = L × U × P** where:
- **L** = Lower triangular (1s on diagonal)
- **U** = Upper triangular
- **P** = Permutation matrix (row swaps)

#### 2. Why Needed
- Solve system Ax = b efficiently
- Compute matrix inverse
- Compute determinant

#### 3. Working
Gaussian elimination with partial pivoting → store multipliers in L, result in U, swaps in P.

#### 4. Solving Ax = b
1. Decompose A = LUP
2. Solve Ly = Pb (forward substitution)
3. Solve Ux = y (backward substitution)

#### 5. Mid-II MCQ
- LU decomposition: **A = L × U** (without pivoting)
- LUP: **A = L × U × P**
- Inverse of triangular matrix: **Triangular**
- Matrix inversion via Gaussian elimination: **O(n³)**

#### 6. One-line Revision
LUP = A = L×U×P → solve linear systems in O(n²) after O(n³) decomposition.

---

### SHORT ANSWER: Relation Between Matrix Operation Complexities

| Operation | Time Complexity |
|-----------|----------------|
| Addition/Subtraction | O(n²) |
| Multiplication (standard) | O(n³) |
| Multiplication (Strassen) | O(n^2.81) |
| Inversion (Gaussian) | O(n³) |
| LUP Decomposition | O(n³) |

**Key Relation:** Multiplication is the "hardest" basic operation. Many operations (inversion, determinant) can be reduced to multiplication.

---

## Unit IV — Dynamic Programming, CRT & FFT

### LONG ANSWER: Floyd-Warshall Algorithm

#### 1. Definition
Finds **all-pairs shortest paths** in a weighted graph (can handle negative weights, but NOT negative cycles).

#### 2. Dynamic Programming Approach
Subproblem: dist[i][j][k] = shortest path from i to j using only vertices {1..k} as intermediates.

#### 3. Recurrence
```
dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
for each intermediate k from 1 to V
```

#### 4. Algorithm
```
FloydWarshall(dist):
    for k = 1 to V:
        for i = 1 to V:
            for j = 1 to V:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
```

#### 5. Example (4-node graph)
```
Initial distance matrix → iterate k=1,2,3,4 → final all-pairs matrix
Show each update step in exam for partial marks
```

#### 6. Limitations
- Does NOT work with **negative cycles**
- O(V³) time — slow for very large graphs
- No path reconstruction by default (need predecessor matrix)

#### 7. Mid-II Match Answers
- Time complexity: **O(V³)**
- Space complexity: **O(V²)**
- Paradigm: **Dynamic Programming**

#### 8. One-line Revision
Floyd-Warshall = DP + try all intermediates → all-pairs shortest paths in O(V³).

---

### LONG ANSWER: Chinese Remainder Theorem (CRT)

#### 1. Definition
If moduli m₁, m₂, ..., mₖ are **pairwise coprime**, then the system:
x ≡ a₁ (mod m₁), x ≡ a₂ (mod m₂), ... has a **unique solution modulo M = m₁×m₂×...×mₖ**.

#### 2. Formula
x = Σ (aᵢ × Mᵢ × yᵢ) mod M, where Mᵢ = M/mᵢ and yᵢ = Mᵢ⁻¹ mod mᵢ

#### 3. Numerical Example
```
x ≡ 2 (mod 3)
x ≡ 3 (mod 5)
x ≡ 2 (mod 7)

M = 3×5×7 = 105
M1=35, M2=21, M3=15
y1=2, y2=1, y3=1 (modular inverses)
x = (2×35×2 + 3×21×1 + 2×15×1) mod 105
x = (140 + 63 + 30) mod 105 = 23
```

#### 4. Application to Polynomial Interpolation
- Represent polynomial values at different points using different moduli
- Compute interpolation in each modulus separately (faster with small numbers)
- Combine using CRT to get exact integer result

#### 5. One-line Revision
CRT = combine modular equations with coprime moduli → unique solution; used in fast polynomial interpolation.

---

### LONG ANSWER: FFT (Fast Fourier Transform)

#### 1. Definition
FFT computes the **Discrete Fourier Transform (DFT)** of a sequence in **O(n log n)** instead of O(n²).

#### 2. DFT Formula
X[k] = Σ x[n] × e^(-2πikn/N) for n = 0 to N-1

#### 3. Why FFT
Polynomial multiplication of degree n takes O(n²) normally. Using FFT: O(n log n).

#### 4. Schonhage-Strassen
Multiplies two n-bit integers in O(n log n log log n) using FFT over rings.

#### 5. Mid-II Fill-in-blanks
- DFT used in: **Fast** multiplication algorithms
- IDFT full form: **Inverse Discrete Fourier Transform**
- TSP is: **NP-complete**

---

## Unit V — Linear Programming & NP-Completeness

### LONG ANSWER: Simplex Algorithm

#### 1. Definition
Simplex solves **linear programming** problems: optimize a linear objective subject to linear constraints.

#### 2. Feasible Region
Set of all points satisfying all constraints (forms a convex polygon/polyhedron).

#### 3. Working Principle
Start at a vertex (basic feasible solution). Move to adjacent vertex that improves objective. Stop when no improvement possible → optimal.

#### 4. Limitations
- Worst-case exponential time (though usually fast in practice)
- Only for linear objectives and constraints
- Cannot directly solve integer programming
- Degenerate cases cause cycling (need Bland's rule)

#### 5. Mid-II MCQ
- Simplex useful for: **Convex feasible sets / Linear inequalities**
- Based on: **Geometric manipulations**
- Cook-Levin: SAT is **NP-complete**
- NP-hard: **At least as hard as hardest problems in NP**

---

### LONG ANSWER: NP-Completeness

#### 1. Definition
A problem is **NP-complete** if:
1. It is in **NP** (solution verifiable in polynomial time)
2. It is **NP-hard** (every NP problem reduces to it in polynomial time)

#### 2. NP-Hard
At least as hard as the hardest NP problems. May not be in NP (e.g., Halting Problem).

#### 3. Proof Technique (Reduction)
To prove X is NP-complete:
1. Show X ∈ NP (give verifier)
2. Reduce known NP-complete problem Y to X in polynomial time

#### 4. Classic NP-Complete Problems
- SAT (Boolean Satisfiability) — first proven (Cook-Levin)
- 3-SAT, Vertex Cover, Clique, TSP, Hamiltonian Cycle, Graph Coloring

#### 5. Limitations & Challenges
- No known polynomial algorithm for any NP-complete problem
- P vs NP is unsolved (Clay Millennium Prize)
- Approximation algorithms used in practice
- Heuristics for TSP, scheduling, etc.

#### 6. One-line Revision
NP-complete = in NP + NP-hard; prove by reduction; no efficient exact algorithm known.

#### 7. 5-Mark Summary
Define NP, NP-hard, NP-complete. Give examples. Explain reduction proof idea. Discuss P vs NP open problem.

---

## Semester Preparation Checklist

### Revision Checklist
- [ ] BFS & DFS — algorithms + graph example
- [ ] Dijkstra — step-by-step with heap
- [ ] Topological Sort — Kahn's algorithm
- [ ] Ford-Fulkerson & Edmonds-Karp
- [ ] Matroids & MST (Kruskal/Prim)
- [ ] Strassen's & LUP decomposition
- [ ] Floyd-Warshall with DP explanation
- [ ] CRT with numerical example
- [ ] Simplex — feasible region + limitations
- [ ] NP-completeness definition + reduction

### Memory Tricks Summary
| Topic | Mnemonic |
|-------|----------|
| BFS | **B**readth = **B**ig **Q**ueue |
| DFS | **D**epth = **D**ive with **S**tack |
| Dijkstra | **D**istance + **H**eap, **N**o negatives |
| Floyd-Warshall | **F**or **A**ll pairs, **3** nested loops = O(V³) |
| Ford-Fulkerson | **F**low through **R**esidual graph |
| NP-complete | **N**eed **P**olynomial verifier + **H**ard reduction |

---

*Study Guide compiled from: Official Syllabus (25CS21PC), Question Bank, Mid-I & Mid-II Question Papers, VR25 Academic Regulations — VCET Hyderabad*
