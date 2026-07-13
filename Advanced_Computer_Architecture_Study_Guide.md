# Advanced Computer Architecture (25CS22PC) — Complete Study Guide
**VCET Hyderabad | VR25 | M.Tech CSE I Year II Sem | Credits: 3**

---

## Table of Contents
1. [Syllabus Overview](#syllabus-overview)
2. [Previous Paper Analysis](#previous-paper-analysis)
3. [Unit I — Theory of Parallelism](#unit-i--theory-of-parallelism)
4. [Unit II — Scalable Performance](#unit-ii--scalable-performance)
5. [Unit III — Pipelining & Memory Organizations](#unit-iii--pipelining--memory-organizations)
6. [Unit IV — Parallel Architectures](#unit-iv--parallel-architectures)
7. [Unit V — Vector & SIMD Processing](#unit-v--vector--simd-processing)
8. [Semester Preparation Checklist](#semester-preparation-checklist)

---

## Syllabus Overview

| Unit | Topics |
|------|--------|
| **I** | Parallel models, Multiprocessors/Multicomputers, PRAM, VLSI, Program partitioning, Conditions of parallelism, Interconnects |
| **II** | Performance metrics, Amdahl's & Gustafson's laws, Memory hierarchy, Superscalar & Vector processors |
| **III** | Shared memory, Consistency models, Linear/Non-linear pipelines, Instruction & Arithmetic pipelines, Superscalar design |
| **IV** | Multiprocessor interconnects, Cache coherence, Synchronization, Multicomputer generations, Message passing, SIMD |
| **V** | Vector processing, Multivector, Compound vector, SIMD organizations, Connection Machine CM-5 |

**Textbook:** *Advanced Computer Architecture* — Kai Hwang (2nd Ed.)

---

## Previous Paper Analysis

### Mid-I Descriptive (June 2026)
| # | Question | Unit | Sem Confidence |
|---|----------|------|----------------|
| Q1 | Parallel computer models with diagrams | I | **95%** |
| Q2 | SIMD vs Multivector comparison | I/V | **90%** |
| Q3 | Memory hierarchy & performance impact | II | **95%** |
| Q4 | Instruction pipeline design with example | III | **90%** |
| Q5 | Conditions of parallelism & program flow | I | **85%** |
| Q6 | Amdahl's & Gustafson's laws with examples | II | **95%** |

### Objective Paper Key Answers
| # | Answer |
|---|--------|
| 1 | PRAM (shared memory, synchronous) |
| 2 | Supports multiple vector pipelines (Multivector) |
| 3 | Program dependency |
| 4 | Amdahl's Law |
| 5 | Systolic flow (NOT valid — answer D) |
| 6 | Utilization |
| 7 | Execute multiple instructions per clock |
| 8 | Registers and caches for faster access |
| 9 | Arithmetic pipeline |
| 10 | Stage by stage in sequence (Linear pipeline) |

### Frequently Repeated Topics
1. **Parallel computer models** — Highest
2. **Amdahl's & Gustafson's laws** — Highest
3. **Memory hierarchy** — Very High
4. **Instruction pipeline** — Very High
5. **SIMD vs Multivector** — High
6. **Cache coherence** — High (Question Bank)
7. **Superscalar vs Vector** — High

---

## Unit I — Theory of Parallelism

### Top 10 Expected Questions
1. Parallel computer models with diagrams
2. SIMD vs MIMD vs Multivector
3. Flynn's classification
4. PRAM model
5. Multiprocessors vs Multicomputers
6. Conditions of parallelism
7. Program flow mechanisms
8. System interconnect architectures
9. Program partitioning & scheduling
10. VLSI model

---

### SHORT ANSWER: Define Parallelism

**Definition:** **Parallelism** means performing **multiple tasks simultaneously** using multiple processing units to reduce total execution time.

**Key Points:**
1. Increases throughput and speed for large problems.
2. Requires hardware support (multiple cores/CPUs) and parallel software.
3. Limited by sequential portions (Amdahl's Law).

**Example:** Restaurant kitchen — multiple chefs cooking different dishes at the same time instead of one chef doing everything.

**Exam Keyword:** *Concurrent execution, Multiple processors, Speedup*

**One-line Revision:** Parallelism = doing many tasks at the same time using multiple processors.

---

### SHORT ANSWER: Multiprocessors vs Multicomputers

**Definition:**
- **Multiprocessor:** Multiple CPUs sharing **one common memory** (Shared Memory System).
- **Multicomputer:** Multiple computers, each with **own memory**, connected by network (Distributed Memory).

| Feature | Multiprocessor | Multicomputer |
|---------|---------------|---------------|
| Memory | Shared | Private per node |
| Communication | Load/Store | Message Passing |
| Example | SMP, NUMA | Cluster, Supercomputer |
| Scalability | Limited | Highly scalable |
| Programming | Easier (shared vars) | Harder (MPI) |

**One-line Revision:** Multiprocessor = shared memory; Multicomputer = separate memory + message passing.

---

### SHORT ANSWER: PRAM Model

**Definition:** **PRAM** (Parallel Random Access Machine) is a theoretical model where **multiple processors** access a **shared memory** synchronously in parallel steps.

**Key Points:**
1. All processors execute same instruction simultaneously (SIMD-like synchronization).
2. Variants based on concurrent memory access rules: EREW, CREW, CRCW.
3. Used for theoretical analysis, not built directly in hardware.

**Example:** Like a classroom where all students read from the same whiteboard at the same time.

**Exam Keyword:** *Shared memory, Synchronous, Theoretical model*

**One-line Revision:** PRAM = many processors + shared memory + synchronous parallel steps.

---

### LONG ANSWER: Parallel Computer Models with Diagrams

#### 1. Definition
Parallel computer models are abstract frameworks describing how multiple processors, memory, and interconnections work together.

#### 2. Introduction
Understanding models helps classify real systems and design parallel algorithms.

#### 3. Why Needed
- Compare different architectures
- Analyze algorithm performance
- Guide hardware design decisions

#### 4. Major Models

**A. Flynn's Classification (1966)**
```
                    Single Data Stream    Multiple Data Streams
Single Instruction   SISD                  SIMD
Multiple Instruction MISD                  MIMD
```

| Type | Meaning | Example |
|------|---------|---------|
| SISD | Single CPU, single data | Old desktop PC |
| SIMD | One instruction, many data | GPU, Vector processor |
| MISD | Multiple instructions, one data | Rare (fault tolerance) |
| MIMD | Multiple instructions, many data | Multicore, Cluster |

**B. PRAM Model**
```
    P1  P2  P3  P4     ← Processors
     \  |  /  /
      Shared Memory
```
- Synchronous lockstep execution
- EREW: Exclusive Read, Exclusive Write
- CREW: Concurrent Read, Exclusive Write
- CRCW: Concurrent Read, Concurrent Write

**C. Multiprocessor Model**
```
  CPU1 ──┐
  CPU2 ──┼── Shared Memory Bus ── Main Memory
  CPU3 ──┘
```

**D. Multicomputer Model**
```
  Node1 (CPU+Mem) ←──Network──→ Node2 (CPU+Mem)
                      ↕
                  Node3 (CPU+Mem)
```

**E. VLSI Model**
- Processors arranged on a chip grid
- Communication cost = wire length
- Used for layout optimization

#### 5. Architecture Diagram (Combined)
```
┌─────────────────────────────────────────┐
│           PARALLEL SYSTEM               │
│  ┌─────┐  ┌─────┐  ┌─────┐            │
│  │ PE0 │  │ PE1 │  │ PE2 │  PE = Processing Element
│  └──┬──┘  └──┬──┘  └──┬──┘            │
│     └────────┼────────┘                │
│         Interconnection Network         │
│     ┌────────┴────────┐                │
│     │  Shared Memory   │  (Multiprocessor)
│     └─────────────────┘                │
└─────────────────────────────────────────┘
```

#### 6. Real-Time Example
- **SISD:** Calculator doing one operation
- **SIMD:** Image filter applying same operation to all pixels
- **MIMD:** Cloud server running web, database, and email simultaneously

#### 7. Exam Tips
- Mid-I Q1: Draw at least 3 models with labels
- MCQ: PRAM = shared memory + synchronous → Answer **B**

#### 8. One-line Revision
Flynn: SISD/SIMD/MISD/MIMD; PRAM = shared memory theory; Multiprocessor vs Multicomputer = shared vs distributed memory.

#### 9. 5-Mark Summary
Explain Flynn's 4 categories with examples. Draw PRAM and multiprocessor diagrams. Compare multiprocessor vs multicomputer.

---

### LONG ANSWER: Conditions of Parallelism & Program Flow Mechanisms

#### 1. Conditions of Parallelism
For a program to run in parallel, these must be satisfied:

| Condition | Meaning |
|-----------|---------|
| **Independence** | Tasks must not depend on each other's incomplete results |
| **Granularity** | Tasks must be large enough to offset overhead |
| **Balance** | Work should be evenly distributed |
| **Locality** | Data accessed should be nearby (cache-friendly) |
| **Pipelining** | Tasks can overlap in stages |

#### 2. Program Flow Mechanisms

| Mechanism | Description | Example |
|-----------|-------------|---------|
| **Control Flow** | Traditional sequential: PC determines next instruction | Standard CPU |
| **Data Flow** | Execute when operands ready | Dataflow machines |
| **Demand Flow** | Execute when result is needed | Lazy evaluation |
| **Systolic Flow** | Data flows through array of PEs rhythmically | Systolic arrays (NOT a program flow mechanism in exam — MCQ answer) |

**Note:** Mid-I MCQ Q5 — Systolic flow is listed as NOT a valid program flow mechanism. Valid: Control flow, Data flow, Demand flow.

#### 3. Program Partitioning
- **Domain decomposition:** Split data (matrix rows among processors)
- **Functional decomposition:** Split by function (one handles I/O, one computes)

#### 4. One-line Revision
Parallelism needs independent, balanced, coarse-grain tasks; Control/Data/Demand flow are valid mechanisms.

---

### LONG ANSWER: SIMD vs Multivector Computers

| Feature | SIMD | Multivector |
|---------|------|-------------|
| Instruction streams | **Single** (one controller) | **Multiple** (each pipeline independent) |
| Data streams | Multiple (all PEs same op) | Multiple (different vector ops) |
| Pipelines | One vector pipeline | **Multiple vector pipelines** |
| Flexibility | Low (lockstep) | Higher (independent pipelines) |
| Example | Connection Machine CM-2 | Cray X-MP, NEC SX |
| Best for | Regular data-parallel | Multiple vector operations simultaneously |

**Mid-I Q2 / MCQ Q2:** Multivector characteristic = **Supports multiple vector pipelines**

#### Architecture Diagrams

**SIMD:**
```
    Control Unit (1 instruction)
         |
    ┌────┼────┬────┐
   PE0  PE1  PE2  PE3   (all do SAME operation)
```

**Multivector:**
```
   Pipeline 1: Vector Op A ──→ Result 1
   Pipeline 2: Vector Op B ──→ Result 2
   Pipeline 3: Vector Op C ──→ Result 3
   (Independent vector pipelines)
```

#### One-line Revision
SIMD = 1 instruction controls all PEs; Multivector = multiple independent vector pipelines.

---

## Unit II — Scalable Performance

### LONG ANSWER: Amdahl's Law and Gustafson's Law

#### 1. Definition
- **Amdahl's Law:** Speedup limited by **sequential (serial) portion** of program.
- **Gustafson's Law:** Speedup increases when **problem size grows** with processors.

#### 2. Amdahl's Law Formula
```
Speedup = 1 / (s + (1-s)/N)

s = serial fraction (0 to 1)
N = number of processors
```

**Explanation of symbols:**
- s = part that CANNOT be parallelized
- (1-s) = part that CAN be parallelized
- N = number of processors

#### 3. Amdahl's Numerical Example
```
s = 0.1 (10% serial), N = 10 processors
Speedup = 1 / (0.1 + 0.9/10) = 1 / (0.1 + 0.09) = 1/0.19 = 5.26x

Even with 10 processors, max speedup is only 5.26x!
With infinite processors: max speedup = 1/0.1 = 10x
```

#### 4. Gustafson's Law Formula
```
Speedup = s + N(1-s)

Assumes problem size increases with N (scaled problem)
```

#### 5. Gustafson's Numerical Example
```
s = 0.1, N = 100
Speedup = 0.1 + 100(0.9) = 0.1 + 90 = 90.1x
Much more optimistic than Amdahl!
```

#### 6. Comparison Table

| Feature | Amdahl's Law | Gustafson's Law |
|---------|-------------|-----------------|
| Assumption | Fixed problem size | Scaled problem size |
| View | Parallel portion shrinks | Serial portion shrinks |
| Optimism | Pessimistic | Optimistic |
| Use | Hardware design limits | Scalable computing |
| Key insight | Serial part limits speedup | More processors → bigger problems |

#### 7. Real-Life Example
**Restaurant (Amdahl):** 1 cashier (serial) + 9 chefs (parallel). No matter how many chefs, customers still wait at cashier → bottleneck.

**Factory (Gustafson):** More workers → process larger orders. Serial setup time becomes smaller fraction of total work.

#### 8. When NOT to Use
- Amdahl: Don't use when problem size scales with processors
- Gustafson: Don't use when problem size is fixed

#### 9. Exam Tips
- Mid-I Q6: Give BOTH laws with formulas AND numerical examples
- MCQ Q4: Sequential part limitation → **Amdahl's Law**
- Fill-in: Scalable system → **Scalable**

#### 10. One-line Revision
Amdahl = fixed problem, serial part limits speedup; Gustafson = scaled problem, more optimistic speedup.

---

### LONG ANSWER: Memory Hierarchy and Performance Impact

#### 1. Definition
**Memory hierarchy** organizes storage in levels from **fastest/smallest** (registers) to **slowest/largest** (disk).

#### 2. Memory Pyramid
```
        ┌─────────┐
        │Registers│  ~1 cycle, KB
        ├─────────┤
        │  L1 Cache│  ~4 cycles, 32-64 KB
        ├─────────┤
        │  L2 Cache│  ~10 cycles, 256KB-1MB
        ├─────────┤
        │  L3 Cache│  ~40 cycles, 8-32 MB
        ├─────────┤
        │   RAM    │  ~100 cycles, GB
        ├─────────┤
        │   Disk   │  ~10ms, TB
        └─────────┘
```

#### 3. Why Needed
- Fast memory is expensive → small amount
- Slow memory is cheap → large amount
- Hierarchy gives **speed of fast memory** with **capacity of slow memory**

#### 4. Performance Impact
- **Cache hit:** Data found in cache → fast access
- **Cache miss:** Must fetch from lower level → stall (100+ cycles)
- **Locality:** Programs accessing nearby data get better performance
  - Temporal locality: reuse same data
  - Spatial locality: access nearby addresses

#### 5. Example
```
CPU needs data:
1. Check Register → Miss
2. Check L1 → Miss
3. Check L2 → Hit! (10 cycles instead of 100 for RAM)
```

#### 6. Exam Tips
- MCQ Q8: Memory hierarchy → **Using registers and caches for faster access**
- Fill-in Q14: Between processor and main memory → **Cache**
- Draw pyramid diagram in exam

#### 7. One-line Revision
Memory hierarchy = Registers → Cache → RAM → Disk; caches reduce latency, locality improves hit rate.

---

### SHORT ANSWER: Superscalar vs Vector Processors

| Feature | Superscalar | Vector |
|---------|------------|--------|
| Idea | Multiple **different** instructions per cycle | One instruction on **many data elements** |
| Pipeline | Multiple instruction pipelines | Long vector pipeline |
| Best for | General-purpose, varied code | Scientific, regular arrays |
| Example | Intel Core i7 | Cray supercomputer |
| Speedup from | Instruction-level parallelism (ILP) | Data-level parallelism (DLP) |

**One-line Revision:** Superscalar = many instructions at once; Vector = one instruction on many data items.

---

## Unit III — Pipelining & Memory Organizations

### LONG ANSWER: Instruction Pipeline Design

#### 1. Definition
**Instruction pipeline** divides instruction execution into **overlapping stages** so multiple instructions execute simultaneously in different stages.

#### 2. Why Needed
Without pipeline: 1 instruction takes 5 cycles → 5 instructions = 25 cycles.  
With 5-stage pipeline: 5 instructions ≈ 9 cycles (near 5x speedup).

#### 3. Classic 5-Stage Pipeline (RISC)
```
Stage 1: IF  — Instruction Fetch
Stage 2: ID  — Instruction Decode
Stage 3: EX  — Execute
Stage 4: MEM — Memory Access
Stage 5: WB  — Write Back
```

#### 4. Pipeline Diagram (Time →)
```
Cycle:  1   2   3   4   5   6   7
Inst1: IF  ID  EX  MEM WB
Inst2:     IF  ID  EX  MEM WB
Inst3:         IF  ID  EX  MEM WB
Inst4:             IF  ID  EX  MEM WB
Inst5:                 IF  ID  EX  MEM WB
```

#### 5. Pipeline Hazards

| Hazard | Cause | Solution |
|--------|-------|----------|
| **Structural** | Hardware conflict (one ALU) | Duplicate hardware |
| **Data** | Instruction needs result not yet ready | Forwarding, stall |
| **Control** | Branch changes PC | Branch prediction, delay slot |

#### 6. Linear vs Non-Linear Pipeline

| Feature | Linear | Non-Linear |
|---------|--------|------------|
| Flow | Sequential stages only | Feedback loops, branches |
| Example | Simple RISC pipeline | Pipeline with loops |
| Complexity | Simple | Complex |
| MCQ Q10 | Stage by stage in sequence | Out of order possible |

#### 7. Real Example
**Assembly line (factory):** Car body, paint, engine, test — each stage works on different car simultaneously.

#### 8. Exam Tips
- Mid-I Q4: Draw 5-stage pipeline timing diagram
- Fill-in Q15: Pipeline stages determine **latency** of pipeline
- MCQ Q9: Arithmetic operations in stages → **Arithmetic pipeline**

#### 9. One-line Revision
Pipeline = divide instruction into stages → overlap execution → higher throughput; watch for hazards.

---

### LONG ANSWER: Memory Consistency Models

#### 1. Definition
**Memory consistency model** defines what values reads can return when multiple processors access shared memory.

#### 2. Sequential Consistency
- Result appears as if all processors executed in some sequential order
- All processors see same order of operations
- **Strongest** and easiest to reason about
- **Slowest** (more synchronization needed)

#### 3. Weak Consistency
- Writes may not be immediately visible to other processors
- Requires explicit **memory barriers/sync** instructions
- **Faster** but harder to program

| Feature | Sequential | Weak |
|---------|-----------|------|
| Ordering | Strict program order | Reordered for performance |
| Visibility | Immediate | Delayed until sync |
| Performance | Lower | Higher |
| Programming | Easy | Difficult |

#### 4. One-line Revision
Sequential = strict ordering (easy, slow); Weak = relaxed ordering (fast, needs sync).

---

### LONG ANSWER: Superscalar Pipeline Design

#### 1. Definition
**Superscalar** processor issues and executes **more than one instruction per clock cycle** using multiple functional units.

#### 2. Architecture
```
         Instruction Fetch (multiple)
              ↓
         Decode & Dispatch
         ↙    ↓    ↘
      ALU1  ALU2  FPU    ← Multiple execution units
         ↓    ↓    ↓
         Write Back
```

#### 3. Challenges (Exam Short Answer)
1. **Instruction dependency** — can't issue dependent instructions together
2. **Resource conflicts** — limited functional units
3. **Branch prediction errors** — misprediction flushes pipeline
4. **Register renaming** complexity

#### 4. MCQ Q7: Superscalar improves by → **Executing multiple instructions per clock cycle**

#### 5. Fill-in Q13: Superscalar issues **multiple** instructions per cycle

---

## Unit IV — Parallel Architectures

### LONG ANSWER: Cache Coherence Protocols

#### 1. Definition
**Cache coherence** ensures all copies of shared data in different caches remain **consistent** (same value).

#### 2. The Problem
```
CPU1 cache: x = 5    CPU2 cache: x = 5
CPU1 writes x = 10   CPU2 still has x = 5  ← INCONSISTENT!
```

#### 3. MSI Protocol (3 States)

| State | Meaning |
|-------|---------|
| **M** Modified | Only this cache has it, different from memory |
| **S** Shared | Multiple caches have clean copy |
| **I** Invalid | Cache line not valid |

#### 4. MESI Protocol (4 States — adds Exclusive)
- **E** Exclusive: Only one cache has it, matches memory

#### 5. Snooping
Each cache monitors (snoops) the shared bus for memory transactions.

#### 6. Example
```
CPU1 reads x → Shared
CPU2 reads x → Shared (both have copy)
CPU1 writes x → Invalidates CPU2's copy → Modified in CPU1
CPU2 reads x → Must fetch from CPU1 or memory
```

#### 7. One-line Revision
Cache coherence = all caches show same data; MSI/MESI protocols track Modified/Shared/Invalid states.

---

### SHORT ANSWER: Three Generations of Multicomputers

| Generation | Era | Characteristics |
|------------|-----|-----------------|
| **1st** | 1980s | Few nodes, slow network, custom OS |
| **2nd** | 1990s | Massively parallel (1000s nodes), mesh/torus network |
| **3rd** | 2000s+ | Commodity clusters, high-speed interconnect (InfiniBand) |

**One-line Revision:** Gen1 = few custom nodes; Gen2 = massively parallel; Gen3 = commodity clusters.

---

## Unit V — Vector & SIMD Processing

### LONG ANSWER: Vector Processing Principles

#### 1. Definition
**Vector processing** applies one instruction to a **vector (array) of operands** simultaneously using pipelined functional units.

#### 2. Architecture
```
Vector Registers:  V1 = [a1, a2, a3, ..., an]
                   V2 = [b1, b2, b3, ..., bn]
                        ↓ Vector ALU (pipelined)
                   V3 = [a1+b1, a2+b2, ..., an+bn]
```

#### 3. Vector vs Scalar

| Feature | Scalar | Vector |
|---------|--------|--------|
| Operations | One at a time | Many simultaneously |
| Loop overhead | High (n iterations) | Low (1 vector instruction) |
| Best for | General code | Array/matrix operations |
| Speedup | 1x | Up to vector length |

#### 4. Compound Vector Processing
Multiple vector operations **chained** together without storing intermediate results to memory.

#### 5. Connection Machine CM-5
- MIMD + SIMD hybrid supercomputer
- Thousands of SPARC processors + vector units
- Used for scientific computing, climate simulation

#### 6. Applications
Weather forecasting, CFD (Computational Fluid Dynamics), matrix operations, image processing

#### 7. One-line Revision
Vector = one instruction on entire array; pipelined units; ideal for scientific computing.

---

## Semester Preparation Checklist

### Unit-wise Top Questions

| Unit | Top 5 Short | Top 5 Long |
|------|------------|------------|
| I | Parallelism, PRAM, Multiprocessor vs Multicomputer, Flynn's, Conditions | Parallel models, SIMD vs Multivector, Interconnects, Program flow, Partitioning |
| II | Amdahl's Law, Speedup, Superscalar vs Vector, Memory hierarchy, Metrics | Amdahl & Gustafson, Memory hierarchy, Scalable performance, Superscalar vs Vector, Advanced processors |
| III | Sequential consistency, Linear pipeline, Pipeline stages, Shared memory, Hazards | Instruction pipeline, Linear vs Non-linear, Superscalar, Arithmetic pipeline, Consistency models |
| IV | Cache coherence, Synchronization, Message passing, Multicomputer gens, Interconnects | Cache coherence protocols, Multiprocessor interconnects, Synchronization, SIMD architecture, Multicomputer comparison |
| V | SIMD, Vector processing, Compound vector, CM-5, Multivector | Vector principles, SIMD organizations, CM-5 architecture, Scalar vs Vector, Compound vector processing |

### Revision Checklist
- [ ] Flynn's SISD/SIMD/MISD/MIMD with examples
- [ ] Draw PRAM, Multiprocessor, Multicomputer diagrams
- [ ] Amdahl's & Gustafson's formulas + numerical examples
- [ ] Memory hierarchy pyramid diagram
- [ ] 5-stage instruction pipeline timing diagram
- [ ] Pipeline hazards (Structural, Data, Control)
- [ ] Sequential vs Weak consistency
- [ ] Cache coherence MSI/MESI
- [ ] SIMD vs Multivector comparison table
- [ ] Superscalar vs Vector comparison

### Memory Tricks
| Topic | Mnemonic |
|-------|----------|
| Flynn | **S**ingle/**M**ultiple × **I**nstruction × **D**ata |
| Amdahl | "**A**mdahl says serial part **A**lways limits" |
| Gustafson | "**G**ustafson **G**rows problem with processors" |
| Pipeline stages | **F**etch **D**ecode **E**xecute **M**emory **W**rite → "**F**ine **D**ogs **E**at **M**y **W**affles" |
| Cache states MESI | **M**odified **E**xclusive **S**hared **I**nvalid |

---

*Study Guide compiled from: Official Syllabus (25CS22PC), Question Bank, Mid-I Question Paper & Objectives — VCET Hyderabad*
