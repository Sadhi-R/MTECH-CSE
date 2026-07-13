# Parallel Computing (25CS233PE) — Complete Study Guide
**VCET Hyderabad | VR25 | M.Tech CSE I Year II Sem | Credits: 3**

---

## Table of Contents
1. [Syllabus Overview](#syllabus-overview)
2. [Previous Paper Analysis](#previous-paper-analysis)
3. [Unit I — Foundations of Parallel Computing](#unit-i--foundations-of-parallel-computing)
4. [Unit II — Design & Analytical Modeling](#unit-ii--design--analytical-modeling)
5. [Unit III — MPI & PThreads Programming](#unit-iii--mpi--pthreads-programming)
6. [Unit IV — Matrix & Sorting Algorithms](#unit-iv--matrix--sorting-algorithms)
7. [Unit V — Graph & Search Algorithms](#unit-v--graph--search-algorithms)
8. [Semester Preparation Checklist](#semester-preparation-checklist)

---

## Syllabus Overview

| Unit | Topics |
|------|--------|
| **I** | Introduction, Motivation, Scope, Parallel platforms, Communication operations |
| **II** | Parallel algorithm design, Task/data decomposition, Load balancing, Amdahl/Gustafson, Analytical modeling |
| **III** | MPI (Message Passing), PThreads (Shared memory), Synchronization |
| **IV** | Matrix-Vector/Matrix-Matrix multiplication, Bubble/Quick/Bucket/Enumeration/Radix Sort |
| **V** | Prim's MST, Dijkstra's SSSP, DFS, BFS |

**Textbook:** *Introduction to Parallel Computing* — Ananth Grama et al. (2nd Ed.)

---

## Previous Paper Analysis

### Mid-I Descriptive (May 2026)
| # | Question | Unit | Sem Confidence |
|---|----------|------|----------------|
| 1 | Basic communication operations | I | **95%** |
| 2 | Shared vs Distributed memory | I | **95%** |
| 3 | Flynn's classification | I | **90%** |
| 4 | Load balancing & scheduling | II | **90%** |
| 5 | Amdahl's & Gustafson's laws | II | **95%** |
| 6 | MPI communication functions | III | **90%** |

### Mid-II Descriptive (July 2025)
| # | Question | Unit | Sem Confidence |
|---|----------|------|----------------|
| 1 | PThreads synchronization | III | **90%** |
| 2 | Matrix-Vector multiplication | IV | **90%** |
| 3 | Bucket Sort & Enumeration Sort | IV | **85%** |
| 4 | Radix Sort comparison | IV | **85%** |
| 5 | Dijkstra's algorithm | V | **90%** |
| 6 | DFS vs BFS comparison | V | **95%** |

### Objective Paper Key Answers (Mid-I)
| # | Answer |
|---|--------|
| 1 | Broadcast (one-to-all) |
| 2 | Distributed Memory System |
| 3 | Bisection bandwidth = bandwidth between two equal halves |
| 4 | Amdahl: s=0.4, N=4 → Speedup = 1/(0.4+0.6/4) = **1.82x** |
| 5 | Data Decomposition |
| 6 | Scalable |
| 7 | Cost-optimal |
| 8 | Process Rank |
| 9 | MPI_Barrier |
| 10 | Global/Shared variables (PThreads) |

### Frequently Repeated Topics
1. **Communication operations** (Broadcast, Reduce, etc.) — Highest
2. **Shared vs Distributed memory** — Highest
3. **Amdahl's & Gustafson's laws** — Highest
4. **MPI functions** — Very High
5. **PThreads synchronization** — Very High
6. **DFS vs BFS** — Very High
7. **Parallel sorting** — High

---

## Unit I — Foundations of Parallel Computing

### Top 10 Expected Questions
1. Communication operations (Broadcast, Scatter, Gather, Reduce)
2. Shared vs Distributed memory architectures
3. Flynn's classification
4. Parallel programming platforms
5. Motivation and scope of parallel computing
6. UMA vs NUMA
7. Network topologies
8. Bisection bandwidth
9. Latency vs bandwidth
10. Parallel computing introduction

---

### SHORT ANSWER: Define Parallel Computing

**Definition:** **Parallel computing** is a type of computation where **many calculations are carried out simultaneously** using multiple processors working together on a large problem.

**Key Points:**
1. Goal: Solve problems faster or handle larger problems.
2. Requires parallel hardware (multicore, clusters) and parallel software (MPI, PThreads).
3. Not all problems benefit — depends on parallelism available.

**Example:** Courier company — 10 delivery agents working in different areas simultaneously instead of 1 agent delivering all packages.

**Exam Keyword:** *Simultaneous execution, Multiple processors, Speedup*

**One-line Revision:** Parallel computing = many processors solving parts of one problem at the same time.

---

### SHORT ANSWER: Flynn's Classification

**Definition:** **Flynn's Classification** (1966) categorizes computer architectures based on **Instruction streams** and **Data streams**.

| Type | Instruction | Data | Example |
|------|------------|------|---------|
| **SISD** | Single | Single | Traditional uniprocessor |
| **SIMD** | Single | Multiple | GPU, Vector processor |
| **MISD** | Multiple | Single | Fault-tolerant systems |
| **MIMD** | Multiple | Multiple | Multicore, Cluster |

**One-line Revision:** Flynn = classify by Single/Multiple Instruction × Single/Multiple Data.

---

### SHORT ANSWER: Shared vs Distributed Memory

| Feature | Shared Memory | Distributed Memory |
|---------|--------------|-------------------|
| Memory access | All processors access common memory | Each processor has private memory |
| Communication | Read/Write shared variables | Send/Receive messages (MPI) |
| Architecture | SMP, UMA, NUMA | Cluster, Supercomputer |
| Scalability | Limited (32-64 processors) | Highly scalable (1000s) |
| Programming | Easier (PThreads, OpenMP) | Harder (MPI) |
| Example | Desktop multicore | Amazon HPC cluster |

**One-line Revision:** Shared = common memory + PThreads; Distributed = private memory + MPI.

---

### LONG ANSWER: Basic Communication Operations

#### 1. Definition
**Communication operations** are collective patterns for moving data between processes in a parallel system.

#### 2. Introduction
In distributed memory systems, processes must explicitly communicate. MPI provides standard operations for common patterns.

#### 3. Why Needed
- Processors have separate memory — data must be shared explicitly
- Standard patterns avoid reinventing communication logic
- Optimized implementations use efficient network protocols

#### 4. Major Operations

| Operation | Pattern | Description | Real-Life Example |
|-----------|---------|-------------|-------------------|
| **Broadcast** | One → All | One process sends same data to all | Manager announces schedule to all workers |
| **Scatter** | One → All (different) | One process sends different data to each | Distributing different tasks to workers |
| **Gather** | All → One | Collect data from all to one process | Collecting reports from all departments |
| **All-Gather** | All → All | Every process gets everyone's data | Everyone shares their results with everyone |
| **Reduce** | All → One (computed) | Combine values (sum, max, min) | Total sales from all branches |
| **All-Reduce** | All → All (computed) | Reduce then broadcast result | Everyone gets total team score |
| **All-to-All** | All ↔ All | Every process sends to every other | Round-robin information exchange |

#### 5. Architecture Diagram
```
BROADCAST (source = P0):
  P0 ──data──→ P1
  P0 ──data──→ P2
  P0 ──data──→ P3

REDUCE (sum to P0):
  P1 ──val──→ P0
  P2 ──val──→ P0  → P0 computes sum
  P3 ──val──→ P0

GATHER (to P0):
  P1 ──block1──→ P0
  P2 ──block2──→ P0  → P0 has [block1|block2|block3]
  P3 ──block3──→ P0
```

#### 6. MPI Functions
```c
MPI_Bcast(&data, count, type, root, comm);     // Broadcast
MPI_Scatter(sendbuf, sendcnt, type, recvbuf, recvcnt, type, root, comm);
MPI_Gather(sendbuf, sendcnt, type, recvbuf, recvcnt, type, root, comm);
MPI_Reduce(sendbuf, recvbuf, count, type, MPI_SUM, root, comm);
MPI_Allreduce(sendbuf, recvbuf, count, type, MPI_SUM, comm);
MPI_Barrier(comm);  // Synchronization — wait for all
```

#### 7. Match the Following (Mid-I)
- Gather → Assembles data blocks from all tasks onto root
- Hypercube → Network diameter O(log p)
- Exploratory Decomposition → Chess engine search
- Recursive Decomposition → Merge Sort divide-and-conquer

#### 8. Exam Tips
- MCQ Q1: One-to-all communication → **Broadcast**
- MCQ Q9: Wait for all processes → **MPI_Barrier**
- Fill-in Q1: Network delay → **Latency**

#### 9. One-line Revision
Broadcast=1→All, Scatter=1→All(different), Gather=All→1, Reduce=All→1(computed), Barrier=sync all.

---

### LONG ANSWER: Parallel Programming Platforms

#### 1. Types of Platforms

| Platform | Memory Model | Programming | Example |
|----------|-------------|-------------|---------|
| **Shared Memory (SMP)** | Shared address space | PThreads, OpenMP | Multicore desktop |
| **Distributed Memory** | Separate address spaces | MPI | HPC Cluster |
| **Hybrid** | Shared within node, distributed across | MPI + OpenMP | Modern supercomputers |
| **GPU/Accelerator** | Device memory + host | CUDA, OpenCL | NVIDIA GPU |
| **Cloud** | Virtualized distributed | Spark, Hadoop | AWS, Azure |

#### 2. UMA vs NUMA
- **UMA** (Uniform Memory Access): All processors have equal memory access time
- **NUMA** (Non-Uniform Memory Access): Access time varies by memory location — MCQ Q2 fill-in

#### 3. One-line Revision
Platforms: Shared memory (PThreads/OpenMP), Distributed (MPI), Hybrid (MPI+OpenMP), GPU (CUDA).

---

## Unit II — Design & Analytical Modeling

### LONG ANSWER: Amdahl's Law and Gustafson's Law

#### 1. Amdahl's Law
```
Speedup(N) = 1 / (s + (1-s)/N)
s = serial fraction, N = processors
```

**Mid-I MCQ Example:**
```
40% sequential (s=0.4), 4 processors (N=4)
Speedup = 1 / (0.4 + 0.6/4) = 1 / (0.4 + 0.15) = 1/0.55 = 1.82x
Answer: B) 1.82x
```

#### 2. Gustafson's Law
```
Speedup(N) = s + N(1-s)
Assumes problem size grows with N
```

#### 3. Comparison Table

| Feature | Amdahl | Gustafson |
|---------|--------|-----------|
| Problem size | Fixed | Scaled |
| Serial fraction effect | Limits max speedup | Diminishes with scale |
| Optimism | Pessimistic | Optimistic |
| Use case | Fixed workload analysis | Scalable systems |

#### 4. Efficiency
```
Efficiency = Speedup / N
Fill-in Q3: Efficiency = Speedup / Number of processors
```

#### 5. Real-Life Example
**Traffic management (Amdahl):** 1 traffic controller (serial) + 4 lane managers (parallel). Controller bottleneck limits total throughput.

**Cloud computing (Gustafson):** More servers → handle more users. Serial overhead becomes tiny fraction.

#### 6. One-line Revision
Amdahl: fixed problem, speedup = 1/(s+(1-s)/N); Gustafson: scaled problem, speedup = s+N(1-s).

---

### LONG ANSWER: Load Balancing and Scheduling

#### 1. Definition
- **Load Balancing:** Distributing work evenly across processors so no processor sits idle.
- **Scheduling:** Deciding which task runs on which processor and when.

#### 2. Why Needed
Uneven load → some processors finish early and wait → wasted resources → poor speedup.

#### 3. Decomposition Strategies

| Strategy | Description | Example |
|----------|-------------|---------|
| **Data Decomposition** | Split data array into chunks | Matrix rows among processors |
| **Task Decomposition** | Split by function | One process I/O, one compute |
| **Recursive Decomposition** | Divide-and-conquer | Merge Sort, Quick Sort |
| **Exploratory Decomposition** | Search state space | Chess move exploration |
| **Speculative Decomposition** | Run branches before knowing if needed | Parallel tree search |

#### 4. Scheduling Techniques
- **Static scheduling:** Pre-assign tasks (good for uniform load)
- **Dynamic scheduling:** Assign at runtime (good for variable load)
- **Work stealing:** Idle processor takes work from busy one

#### 5. Task Dependency Graph
```
Fill-in Q4: Dependency graph maps dependencies between tasks

    Task A ──→ Task C
      ↓          ↓
    Task B ──→ Task D

C depends on A and B → must wait for both
```

#### 6. Real Example
**Restaurant kitchen:** Head chef (scheduler) assigns dishes to chefs (processors). If one chef finishes early, assign more dishes (dynamic scheduling).

#### 7. One-line Revision
Load balance = equal work per processor; Data decomposition splits arrays; Dynamic scheduling handles uneven loads.

---

### LONG ANSWER: Analytical Modeling of Parallel Programs

#### 1. Key Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| **Speedup** | T_serial / T_parallel | How much faster |
| **Efficiency** | Speedup / P | How well processors used |
| **Cost** | P × T_parallel | Total processor-time |
| **Cost-optimal** | Cost = O(T_serial) | Parallel cost equals best serial |

#### 2. Cost-Optimal (Mid-I MCQ Q7)
When total parallel cost ≈ best sequential time → **Cost-optimal**

#### 3. Isoefficiency
How problem size must grow to maintain constant efficiency as processors increase.

---

## Unit III — MPI & PThreads Programming

### LONG ANSWER: MPI Architecture and Functions

#### 1. Definition
**MPI** (Message Passing Interface) is a standard for writing parallel programs on **distributed memory** systems where processes communicate by sending/receiving messages.

#### 2. Architecture
```
Process 0 (Rank 0)          Process 1 (Rank 1)
┌──────────────┐           ┌──────────────┐
│ Private Mem  │ ←─MSG──→ │ Private Mem  │
│   Code+Data  │           │   Code+Data  │
└──────────────┘           └──────────────┘
        ↕ Network ↕
Process 2 (Rank 2)          Process 3 (Rank 3)
```

#### 3. Key Concepts
- **Process:** Independent execution unit with own memory
- **Rank:** Unique ID of process in communicator (MCQ Q8: **Process Rank**)
- **Communicator:** Group of processes (MPI_COMM_WORLD = all)
- **Tag:** Message identifier for matching sends/receives

#### 4. Essential MPI Functions
```c
#include <mpi.h>

int main(int argc, char *argv[]) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Point-to-point
    if (rank == 0)
        MPI_Send(&data, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    else if (rank == 1)
        MPI_Recv(&data, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);

    // Collective
    MPI_Bcast(&data, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Reduce(&local, &global, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
    MPI_Barrier(MPI_COMM_WORLD);

    MPI_Finalize();
    return 0;
}
```

#### 5. Function Summary Table

| Function | Type | Purpose |
|----------|------|---------|
| MPI_Init | Setup | Initialize MPI |
| MPI_Finalize | Setup | Clean up MPI |
| MPI_Comm_rank | Query | Get process rank |
| MPI_Comm_size | Query | Get total processes |
| MPI_Send | Point-to-point | Send message |
| MPI_Recv | Point-to-point | Receive message |
| MPI_Bcast | Collective | Broadcast data |
| MPI_Reduce | Collective | Reduce + send to root |
| MPI_Allreduce | Collective | Reduce + broadcast |
| MPI_Barrier | Sync | Wait for all processes |
| MPI_Gather | Collective | Collect to root |
| MPI_Scatter | Collective | Distribute from root |

#### 6. One-line Revision
MPI = message passing on distributed memory; Rank = process ID; Send/Recv for P2P; Bcast/Reduce/Barrier for collective.

---

### LONG ANSWER: PThreads Synchronization Mechanisms

#### 1. Definition
**PThreads** (POSIX Threads) provides multi-threading on **shared memory** systems where threads share the same address space.

#### 2. PThreads vs MPI

| Feature | PThreads | MPI |
|---------|----------|-----|
| Memory | Shared address space | Separate address spaces |
| Communication | Shared variables | Messages |
| Creation | pthread_create() | MPI_Init + fork processes |
| Sync | Mutex, Semaphore | MPI_Barrier, Send/Recv |
| Best for | Multicore shared memory | Clusters, distributed |

**Mid-II MCQ Q1:** PThreads = shared address space; MPI = separate address spaces → Answer **C**

#### 3. Thread Creation
```c
#include <pthread.h>

void *worker(void *arg) {
    // thread work
    return NULL;
}

int main() {
    pthread_t thread;
    pthread_create(&thread, NULL, worker, NULL);
    pthread_join(thread, NULL);  // Wait for thread
    return 0;
}
```

#### 4. Synchronization Mechanisms

**A. Mutex (Mutual Exclusion)**
```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

pthread_mutex_lock(&lock);
// CRITICAL SECTION — only one thread at a time
pthread_mutex_unlock(&lock);
```
- Only **one thread** can hold the lock at a time
- Mid-II MCQ Q2: Answer **C) Mutex Lock**

**B. Semaphore**
```c
sem_t sem;
sem_init(&sem, 0, 1);
sem_wait(&sem);   // decrement (P operation)
// critical section
sem_post(&sem);   // increment (V operation)
```
- Controls access based on counter
- Can allow N threads simultaneously

**C. Condition Variable**
```c
pthread_cond_wait(&cond, &mutex);  // wait for signal
pthread_cond_signal(&cond);        // wake one waiter
```
- Thread waits until condition becomes true

**D. Barrier**
- All threads must reach barrier before any proceed

#### 5. Critical Section Problem
When multiple threads access shared data, only one must modify at a time to prevent race conditions.

#### 6. Race Condition Example
```
Thread 1: read x (=5) → add 1 → write x (=6)
Thread 2: read x (=5) → add 1 → write x (=6)  ← Should be 7!
Both read before either writes → lost update
```

#### 7. Fill-in Q5: pthread_join — waits for thread termination

#### 8. One-line Revision
PThreads = shared memory threads; Mutex = one at a time; Semaphore = counter-based access; pthread_join = wait for thread.

---

## Unit IV — Matrix & Sorting Algorithms

### LONG ANSWER: Matrix-Vector Multiplication (Parallel)

#### 1. Problem
Compute y = A × x, where A is n×n matrix, x and y are n×1 vectors.

#### 2. Sequential
```c
for (i = 0; i < n; i++)
    y[i] = 0;
    for (j = 0; j < n; j++)
        y[i] += A[i][j] * x[j];
```
Time: O(n²)

#### 3. Parallel (Row-wise decomposition)
```
Split rows of A among p processors:
  Processor 0: rows 0 to n/p-1
  Processor 1: rows n/p to 2n/p-1
  ...

Each processor computes its rows independently → no communication needed!
```

#### 4. Architecture
```
    A (n×n)         x (n×1)
  ┌─────────┐       ┌───┐
P0│ rows 0  │──────→│   │──→ y[0..n/p-1]
P1│ rows 1  │──────→│ x │──→ y[n/p..2n/p-1]
P2│ rows 2  │──────→│   │──→ y[2n/p..3n/p-1]
  └─────────┘       └───┘
```

#### 5. One-line Revision
Parallel matrix-vector: split rows among processors, each computes independently — embarrassingly parallel.

---

### LONG ANSWER: Matrix-Matrix Multiplication (Parallel)

#### 1. Cannon's Algorithm (2D Mesh)
- Matrices mapped onto √p × √p processor grid
- Initial **circular shift** of rows (A) and columns (B)
- Each step: local multiply-add + shift
- Fill-in: block size = n/√p × n/√p

#### 2. 2D Block Decomposition
Each processor gets a block of C = A × B. Requires communication to get needed blocks of A and B.

#### 3. Mid-II MCQ Q3: Cannon's needs circular shift of rows/columns → Answer **B**

---

### LONG ANSWER: Parallel Sorting Algorithms

#### Bubble Sort (Parallel)
- **Bottleneck:** Sequential dependency between swap steps (Mid-II MCQ Q4: Answer **B**)
- Parallel version: Odd-even transposition sort — compare-swap pairs in alternating phases

#### Quick Sort (Parallel)
- Partition around pivot → recursive parallel sort on sub-arrays
- **Problem:** Bad pivot → uneven split → load imbalance (Fill-in: **pivot**)

#### Bucket Sort
1. Divide range into n buckets
2. Distribute elements to buckets
3. Sort each bucket independently (parallel!)
4. Concatenate buckets

**Example:** Sort ages 1-100 into buckets [0-20], [21-40], [41-60], [61-80], [81-100]

#### Enumeration Sort
- Count how many elements are smaller than each element
- That count = final position
- Mid-II MCQ Q8: Counts smaller elements → **Enumeration Sort**

#### Radix Sort
- Sort by individual digits from **least significant to most significant**
- Fill-in: **Radix** Sort
- Stable sort at each digit pass

#### Comparison Table

| Algorithm | Method | Parallel Friendly? | Complexity |
|-----------|--------|-------------------|------------|
| Bubble Sort | Compare adjacent | Poor (dependencies) | O(n²) |
| Quick Sort | Partition + recurse | Good (independent sub-arrays) | O(n log n) avg |
| Bucket Sort | Distribute to buckets | Excellent (independent buckets) | O(n) avg |
| Enumeration Sort | Count smaller elements | Good (independent counts) | O(n²) |
| Radix Sort | Digit-by-digit | Good (digit passes parallel) | O(d×n) |

#### One-line Revision
Bucket = divide range; Enumeration = count smaller; Radix = sort by digits LSD to MSD.

---

## Unit V — Graph & Search Algorithms

### LONG ANSWER: Dijkstra's Algorithm (Parallel)

#### 1. Definition
Finds **shortest path from single source** to all vertices in weighted graph (non-negative weights).

#### 2. Greedy Strategy
Always pick unvisited vertex with minimum distance (Fill-in: **Greedy**)

#### 3. Algorithm
```
Dijkstra(G, source):
    dist[source] = 0; all others = ∞
    S = empty set
    while S ≠ V:
        u = vertex with min dist not in S
        add u to S
        for each neighbor v of u:
            if dist[u] + w(u,v) < dist[v]:
                dist[v] = dist[u] + w(u,v)
```

#### 4. Example
```
Graph:     A --4-- B
           |       |
           2       1
           |       |
           C --3-- D

From A: dist={A:0, B:4, C:2, D:5}
Path A→D: A→C→D = 2+3 = 5
```

#### 5. Parallelization
- Inner loop (relax neighbors) can be parallelized
- Priority queue extraction is sequential bottleneck

---

### LONG ANSWER: DFS vs BFS Comparison

| Feature | DFS | BFS |
|---------|-----|-----|
| Data Structure | **Stack** | **Queue** |
| Exploration | Deep (go far first) | Level-by-level |
| Shortest Path | No (unweighted) | Yes (unweighted) |
| Memory | O(depth) | O(width) |
| Parallel overhead | Speculative search waste | Frontier synchronization |
| Implementation | Recursive or explicit stack | Queue-based |
| Time | O(V+E) | O(V+E) |

#### Graph Example
```
    A
   / \
  B   C
 /     \
D       E

DFS from A: A → B → D → C → E  (go deep: A→B→D first)
BFS from A: A → B → C → D → E  (level by level)
```

#### Parallel BFS
- **Frontier** (queue) distributed across processors (Mid-II MCQ Q10: **Queue/frontier set**)
- Each level processed in parallel

#### Parallel DFS
- Stack-based, prone to **speculative overhead** (exploring wrong paths)
- Match: DFS → Stack-based, speculative overhead

#### Match the Following (Mid-II)
- Cannon's → B (2D block shifting)
- Enumeration Sort → A (O(n²) comparisons for ranking)
- BFS → D (Level-by-level, queue frontier)
- DFS → C (Stack-based, speculative overhead)

#### One-line Revision
DFS = Stack + deep + backtrack; BFS = Queue + level-order + shortest path.

---

### LONG ANSWER: Prim's Algorithm (Parallel MST)

#### 1. Definition
**Prim's algorithm** builds Minimum Spanning Tree by growing from a starting vertex, always adding minimum-weight edge connecting tree to outside.

#### 2. Parallelization
- Partition vertices among processors
- Each finds local minimum edge to growing tree
- Global minimum selected via reduction (MPI_Allreduce)

#### 3. Mid-II MCQ Q6/Q9: Inner loop parallelizable by vertex partitioning → Answer **A**

---

## Semester Preparation Checklist

### Unit-wise Expected Questions

| Unit | Top 5 Short | Top 5 Long |
|------|------------|------------|
| I | Parallel computing, Flynn's, Shared/Distributed memory, SIMD/MIMD, Latency | Communication ops, Flynn's classification, Shared vs Distributed, Programming platforms, Motivation |
| II | Load balancing, Amdahl's Law, Gustafson's Law, Concurrency, Task scheduling | Parallel algorithm design, Decomposition strategies, Load balancing, Analytical modeling, Amdahl & Gustafson |
| III | MPI, Deadlock, Thread, Mutex, Critical section | MPI functions, PThreads sync, MPI architecture, Thread creation, Mutex vs Semaphore |
| IV | Dense matrix, Pivot, Bucket sort, Radix sort, Divide & Conquer | Matrix-vector mult, Matrix-matrix mult, Bubble & Quick sort, Bucket & Enumeration sort, Radix sort |
| V | Weighted graph, MST, Prim's, Dijkstra's, Greedy | Prim's with example, Dijkstra with example, DFS algorithm, BFS algorithm, DFS vs BFS |

### Revision Checklist
- [ ] All 7 communication operations with diagrams
- [ ] Shared vs Distributed memory table
- [ ] Flynn's 4 types with examples
- [ ] Amdahl's formula + MCQ example (s=0.4, N=4)
- [ ] Gustafson's formula + comparison
- [ ] MPI functions: Send, Recv, Bcast, Reduce, Barrier
- [ ] PThreads: create, join, mutex, semaphore
- [ ] Matrix-vector parallel decomposition
- [ ] Bucket, Enumeration, Radix sort differences
- [ ] Dijkstra step-by-step example
- [ ] DFS vs BFS comparison table

### Memory Tricks
| Topic | Mnemonic |
|-------|----------|
| MPI vs PThreads | **M**PI = **M**essages (distributed), **P**Threads = **P**rivate→Shared |
| Communication | **B**roadcast **S**catter **G**ather **R**educe → "**B**ig **S**uper **G**reen **R**obots" |
| Amdahl MCQ | s=0.4, N=4 → 1/(0.4+0.15) = **1.82** |
| Sorting | **B**ucket=**B**ins, **E**num=**E**ach count, **R**adix=**R**ight digits |
| DFS vs BFS | DFS=**D**epth=**S**tack, BFS=**B**readth=**Q**ueue |

---

*Study Guide compiled from: Official Syllabus (25CS233PE), Question Bank, Mid-I & Mid-II Question Papers — VCET Hyderabad*
