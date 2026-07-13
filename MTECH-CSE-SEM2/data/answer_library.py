# -*- coding: utf-8 -*-
"""Topic-specific clear answers for every Question Bank item."""

from data.answer_overrides import OVERRIDES
from data.visual_library import attach_visual

# Each entry: overrides for short or long question dict fields


def match(question: str, *keywords) -> bool:
    q = question.lower()
    return all(k.lower() in q for k in keywords)


def enrich(q: dict) -> dict:
    """Apply topic-specific clear answers based on question text."""
    text = q.get("question", "")
    t = q.get("type", "short")
    o = ANSWERS.get(q.get("id", ""))
    if o:
        result = {**q, **o}
    else:
        matched = False
        result = q
        for rule in RULES:
            if rule["type"] == t and rule["match"](text):
                result = {**q, **rule["data"]}
                matched = True
                break
        if not matched:
            result = _improve_generic(q)
    return attach_visual(result)


def _improve_generic(q: dict) -> dict:
    """Upgrade auto-template answers with clearer question-specific text."""
    question = q.get("question", "").rstrip(".")
    unit = q.get("unit", "")
    if q.get("type") == "short":
        if "exam-focused concept" not in q.get("definition", ""):
            return q
        return {
            **q,
            "definition": f"<strong>{question}</strong> — explained simply for {unit} exams.",
            "key_points": [
                f"State a clear one-line definition of the concept asked in: {question}.",
                "Add the main rule, formula, or property examiners expect.",
                "Mention one contrast or limitation if applicable.",
            ],
            "example": f"Real-life link: relate '{question[:40]}...' to maps, banks, CPU, or kitchen-team analogy.",
            "exam_keyword": "Definition · Key rule · Example · Complexity (if any)",
            "one_liner": f"{question} → define, 2 facts, 1 example, done.",
        }
    if "exam-focused concept" not in q.get("definition", ""):
        return q
    return {
        **q,
        "definition": f"<strong>{question}</strong> — core idea in simple words.",
        "introduction": f"This topic from {unit} is commonly asked in 5-mark and 10-mark papers.",
        "why": "Examiners test whether you can explain concept + steps + example + complexity.",
        "working": f"Break '{question[:50]}' into definition, mechanism, and outcome.",
        "steps": [
            "Write definition in 1-2 lines.",
            "Explain working principle in plain English.",
            "Draw diagram / write algorithm if applicable.",
            "Give one numerical or real-world example.",
            "State time/space complexity and applications.",
        ],
        "example": "Use Google Maps, bank automation, CPU pipeline, or restaurant kitchen as analogy.",
        "exam_tips": "Always start with definition; end with complexity or comparison.",
        "mark5": f"Define + 3 key points + 1 example for: {question[:60]}.",
        "mark10": f"Full structure with diagram/algorithm, example, complexity, applications for: {question[:60]}.",
        "one_liner": f"{question[:70]} — define, explain, example, complexity.",
    }


# ---- Per-ID overrides (highest priority) ----
ANSWERS = dict(OVERRIDES)

# ---- Rule-based overrides ----
RULES = []

def rule(type_, *keywords, **data):
    RULES.append({"type": type_, "match": lambda t, kw=keywords: match(t, *kw), "data": data})

# ==================== ADVANCED ALGORITHMS ====================

# Unit I Short
rule("short", "bfs", "shortest",
     definition="<strong>BFS</strong> (Breadth-First Search) visits a graph <em>level by level</em> using a <span class='kw'>Queue</span>.",
     key_points=["BFS explores nodes in increasing distance (number of edges) from the source.", "The first time BFS reaches a node, that path uses the minimum number of edges.", "Therefore in an <strong>unweighted</strong> graph (all edges cost 1), BFS gives the shortest path."],
     example="Google Maps treating all roads as equal distance — BFS finds the route with fewest turns/hops.",
     exam_keyword="Queue · Level-order · O(V+E) · Unweighted graph",
     one_liner="BFS = Queue + level-by-level → first visit = shortest path in unweighted graphs.")

rule("short", "dijkstra", "negative",
     definition="<strong>Dijkstra's algorithm</strong> finds shortest paths from one source using a <span class='kw'>Min-Heap</span> and assumes edge weights are <strong>non-negative</strong>.",
     key_points=["Dijkstra marks a node's distance as final once extracted from the heap.", "A negative edge could later create a cheaper path to an already-finalized node.", "That breaks correctness — use <strong>Bellman-Ford</strong> for negative weights."],
     example="A flight with a discount coupon (negative cost) can make a longer route cheaper — Dijkstra would miss it.",
     exam_keyword="Non-negative weights · Greedy · Use Bellman-Ford if negative",
     one_liner="Negative edges break Dijkstra's finalized-distance rule → use Bellman-Ford.")

rule("short", "strongly connected",
     definition="A <strong>Strongly Connected Component (SCC)</strong> in a <em>directed</em> graph is a maximal set of vertices where every vertex can reach every other vertex in the set.",
     key_points=["Maximal = cannot add more vertices while keeping full reachability.", "Found using Kosaraju's or Tarjan's algorithm (DFS-based).", "A directed graph may have multiple SCCs."],
     example="Social 'follow' network — each SCC is a group with mutual reachability.",
     exam_keyword="Directed graph · Mutual reachability · DFS",
     one_liner="SCC = maximal group in directed graph where every node reaches every other.")

rule("short", "amortized", "worst",
     definition="<strong>Amortized analysis</strong> gives the <em>average cost per operation</em> over a sequence, even if some single operations are expensive.",
     key_points=["Worst-case = cost of ONE operation in the worst scenario.", "Amortized = total cost of n operations divided by n.", "Example: dynamic array insert is O(1) amortized though occasional resize is O(n)."],
     example="Warehouse: sometimes the whole shelf is rebuilt (expensive), but average cost per box added is low.",
     exam_keyword="Average over sequence · Dynamic array · Aggregate method",
     one_liner="Worst-case = single op cost; Amortized = average cost over many operations.")

rule("short", "time complexity", "dfs",
     definition="<strong>DFS</strong> (Depth-First Search) visits every vertex and explores every edge once using a <span class='kw'>Stack</span> or recursion.",
     key_points=["Each vertex visited once → O(V).", "Each edge examined once → O(E).", "Total time = <strong>O(V + E)</strong>. Space O(V) for stack/visited."],
     example="Maze solving — go deep into one path before backtracking.",
     exam_keyword="O(V+E) · Stack/Recursion · Backtracking",
     one_liner="DFS time = O(V+E) — visit each vertex and edge exactly once.")

# Unit I Long
rule("long", "sorting",
     definition="<strong>Sorting</strong> arranges elements in order. Different algorithms trade speed, memory, and stability.",
     introduction="Comparison sorts are fundamental to databases, search, and scheduling.",
     why="Choosing the right sort affects performance on large datasets (Amazon orders, exam roll lists).",
     working="Compare/swap or divide-and-conquer to place elements correctly.",
     steps=["State purpose of sorting.", "Tabulate Bubble, Insertion, Selection, Merge, Quick.", "Give best/avg/worst time and space.", "Note stability.", "Give one advantage and disadvantage each."],
     diagram="Bubble: adjacent swaps | Merge: split-merge | Quick: partition around pivot",
     algorithm="Merge Sort: divide array, sort halves, merge. Quick Sort: pick pivot, partition, recurse.",
     flowchart="Choose sort → Compare n and data pattern → Pick Merge/Quick for large n",
     example="Sorting delivery packages by pin code before dispatch.",
     advantages=["Merge/Quick O(n log n) average", "Insertion good for nearly sorted"],
     disadvantages=["Bubble/Selection O(n²)", "Quick worst case O(n²) bad pivot"],
     applications=["Database indexing", "Finding median", "Preprocessing for binary search"],
     exam_tips="Always include comparison table with stability column.",
     mistakes="Saying Quick is always O(n log n); forgetting Merge needs O(n) extra space.",
     comparison="<tr><td>Bubble</td><td>O(n²)</td><td>O(1)</td><td>Yes</td></tr><tr><td>Merge</td><td>O(n log n)</td><td>O(n)</td><td>Yes</td></tr><tr><td>Quick</td><td>O(n log n) avg</td><td>O(log n)</td><td>No</td></tr>",
     time="Bubble O(n²), Merge/Quick O(n log n) average",
     space="Merge O(n), others mostly O(1) or O(log n)",
     interview="When to use stable sort? When is Insertion Sort preferred?",
     memory="Bubble = Buddy swaps; Merge = Memory needed; Quick = Quick if good pivot",
     mark5="Define sorting. Tabulate 5 algorithms with time/space/stability. One line each advantage.",
     mark10="Full table + explain Merge and Quick with small example dry-run + when to use which.",
     one_liner="Merge/Quick for large data; Bubble/Insertion for teaching and tiny/nearly-sorted data.")

rule("long", "bfs", "dfs",
     definition="<strong>BFS</strong> uses a Queue (level-by-level). <strong>DFS</strong> uses a Stack/recursion (depth-first, backtrack).",
     introduction="Graph traversal visits all reachable nodes systematically.",
     why="Needed for shortest paths, cycle detection, connectivity, topological sort.",
     working="BFS: enqueue source, dequeue, enqueue unvisited neighbors. DFS: mark visited, recurse on neighbors, backtrack.",
     steps=["Draw graph.", "Show BFS order with queue contents.", "Show DFS order with stack.", "Write pseudocode for both.", "State O(V+E) complexity."],
     diagram="""  A---B---D
   \\     /
    C---E
BFS from A: A→B,C→D,E
DFS from A: A→B→D→E→C""",
     algorithm="BFS: queue-based. DFS: recursive or explicit stack.",
     flowchart="Start → mark source → BFS: enqueue loop | DFS: recurse unvisited → done",
     example="BFS = Google Maps equal roads. DFS = maze / friend-chain exploration.",
     advantages=["BFS: shortest path unweighted", "DFS: less memory on deep graphs, topo sort"],
     disadvantages=["BFS: more memory on wide graphs", "DFS: may not find shortest path"],
     applications=["BFS: GPS hops, broadcasting", "DFS: cycle detect, topo sort, SCC"],
     exam_tips="Always state data structure: Queue vs Stack. Time O(V+E) for both.",
     mistakes="Using Stack for BFS; forgetting visited array.",
     comparison="BFS=Queue+levels+shortest | DFS=Stack+depth+backtrack",
     time="O(V+E) both",
     space="O(V) visited + queue/stack",
     interview="When BFS over DFS? How detect cycle with DFS?",
     memory="BFS=Big Queue, DFS=Dive Stack",
     mark5="Define both, data structures, pseudocode, small graph order, O(V+E).",
     mark10="Full algorithms, worked graph with queue/stack snapshots, comparison table, applications.",
     one_liner="BFS=Queue+shortest hops; DFS=Stack+backtrack; both O(V+E).")

rule("long", "dag", "topological",
     definition="A <strong>DAG</strong> is a Directed Acyclic Graph (no cycles). <strong>Topological sort</strong> orders vertices so every edge u→v has u before v.",
     introduction="Used when tasks have prerequisites.",
     why="Course scheduling, build systems, project planning need valid execution order.",
     working="Kahn's algorithm: repeatedly pick vertices with in-degree 0.",
     steps=["Compute in-degrees.", "Enqueue all in-degree 0.", "Dequeue u, append to result, reduce neighbor in-degrees.", "If result size < V, cycle exists."],
     diagram="Courses: Math→OS→Networks→Cloud",
     algorithm="Kahn's BFS on in-degrees. Time O(V+E).",
     flowchart="Compute in-degree → queue zeros → process → cycle check",
     example="Prerequisite chain: Math before OS before Cloud computing.",
     advantages=["Detects cycles", "Linear time", "Simple to implement"],
     disadvantages=["Only works on DAGs", "Order may not be unique"],
     applications=["Course scheduling", "Makefile builds", "Spreadsheet recalc"],
     exam_tips="Topological sort ONLY on DAGs. MCQ answer: Directed Acyclic Graphs.",
     mistakes="Trying topological sort on cyclic graph.",
     comparison="DAG=no cycles; Topo sort=linear order respecting edges",
     time="O(V+E)",
     space="O(V)",
     interview="How detect cycle during topo sort?",
     memory="In-degree zero = ready to take course",
     mark5="Define DAG and topo sort. Kahn's algorithm. Small example. O(V+E).",
     mark10="Definition, algorithm steps, example graph, cycle detection, applications.",
     one_liner="DAG=no cycles; Topological sort=valid prerequisite order in O(V+E).")

rule("long", "dijkstra",
     definition="<strong>Dijkstra's algorithm</strong> finds single-source shortest paths in graphs with <strong>non-negative</strong> edge weights using a greedy Min-Heap.",
     introduction="Standard algorithm for weighted shortest path (GPS, routing).",
     why="BFS fails when edges have different costs.",
     working="Always settle the unvisited node with minimum tentative distance; relax its neighbors.",
     steps=["dist[source]=0, others=∞.", "Insert (0,source) in min-heap.", "Extract min (d,u); skip if stale.", "For each edge (u,v,w): if dist[u]+w < dist[v], update and insert.", "Repeat until heap empty."],
     diagram="A--4--B\n|     |\n2     1\n|     |\nC--3--D\nFrom A: D=5 via C",
     algorithm="Priority queue + relaxation: dist[v]=min(dist[v], dist[u]+w)",
     flowchart="Init → extract min → relax neighbors → repeat",
     example="Food delivery: find fastest route when roads have different travel times.",
     advantages=["Efficient with heap", "Greedy and intuitive", "Works on sparse graphs"],
     disadvantages=["No negative weights", "Heap operations add log factor"],
     applications=["Google Maps routing", "Network routing", "Game AI pathfinding"],
     exam_tips="State heap as data structure. Fill-in: single-source shortest path.",
     mistakes="Using with negative edges; not marking stale heap entries.",
     comparison="Dijkstra=non-negative+heap | Bellman-Ford=handles negatives, slower",
     time="O((V+E) log V) with binary heap",
     space="O(V)",
     interview="Why greedy works? When Bellman-Ford instead?",
     memory="Dijkstra = Distance + Heap, No Negatives",
     mark5="Define, greedy idea, algorithm steps, small example, complexity.",
     mark10="Full algorithm, dry-run on 4-node graph, proof sketch, limitations, applications.",
     one_liner="Dijkstra = greedy + min-heap → single-source shortest path, no negative weights.")

rule("long", "mst", "kruskal", "prim",
     definition="<strong>MST</strong> (Minimum Spanning Tree) connects all vertices with minimum total edge weight and no cycles.",
     introduction="Greedy algorithms Kruskal and Prim both find MST optimally.",
     why="Network design: minimum cable/pipeline cost connecting all sites.",
     working="Kruskal: sort edges, add if no cycle. Prim: grow tree from source, always add cheapest edge to outside.",
     steps=["Kruskal: sort edges, Union-Find, add safe edges.", "Prim: start vertex, priority queue of border edges, pick min."],
     diagram="Warehouses as nodes; MST = minimum total road length connecting all",
     algorithm="Kruskal O(E log E). Prim O(E log V) with heap.",
     flowchart="Kruskal: sort→add safe | Prim: grow with min edge",
     example="Connect 5 bank branches with minimum fiber cable length.",
     advantages=["Kruskal good for sparse graphs", "Prim good for dense graphs", "Both greedy-optimal"],
     disadvantages=["Kruskal needs Union-Find", "Prim needs heap and good for dense"],
     applications=["Network design", "Cluster analysis", "Approximation algorithms"],
     exam_tips="Draw small graph and show edges chosen by each algorithm.",
     mistakes="Confusing MST with shortest path tree.",
     comparison="<tr><th></th><th>Kruskal</th><th>Prim</th></tr><tr><td>Method</td><td>Sort all edges</td><td>Grow from source</td></tr><tr><td>DS</td><td>Union-Find</td><td>Priority Queue</td></tr>",
     time="Kruskal O(E log E), Prim O(E log V)",
     space="O(V) for both",
     interview="Why greedy works for MST? Matroid connection.",
     memory="Kruskal=Sort edges; Prim=Grow tree",
     mark5="Define MST. Kruskal vs Prim table. One small example.",
     mark10="Definitions, both algorithms, worked example, complexity, matroid/greedy note.",
     one_liner="MST = min-cost connect-all; Kruskal sorts edges, Prim grows tree.")

# Unit II
rule("short", "matroid",
     definition="A <strong>matroid</strong> is a set system where the <span class='kw'>greedy algorithm</span> always finds the optimal independent set.",
     key_points=["Independent sets satisfy hereditary and exchange properties.", "MST edge-set forms a matroid (forests are independent).", "Greedy on matroids is provably optimal."],
     example="Picking maximum-weight non-conflicting tasks — greedy works because of matroid structure.",
     exam_keyword="Greedy optimality · Independent sets · MST application",
     one_liner="Matroid = structure where Greedy always works; MST is classic example.")

rule("short", "augmenting path",
     definition="An <strong>augmenting path</strong> alternates non-matching and matching edges between two free (unmatched) vertices.",
     key_points=["Flipping edges along it increases matching size by 1.", "Maximum matching ⇔ no augmenting path exists.", "Edmond's Blossom handles augmenting paths in general graphs."],
     example="Reassign workers to jobs to include one more worker in the matching.",
     exam_keyword="Free vertices · Alternating path · Maximum matching",
     one_liner="Augmenting path increases matching by 1; none exists iff matching is maximum.")

rule("long", "ford", "fulkerson",
     definition="<strong>Max-flow</strong> = maximum flow from source s to sink t. <strong>Min-cut</strong> = minimum capacity edges disconnecting s from t. <strong>Theorem:</strong> max flow = min cut.",
     introduction="Flow networks model pipelines, networks, and matching.",
     why="Optimize throughput in networks; solve matching via reduction.",
     working="Repeatedly find augmenting paths in the residual graph and push bottleneck flow.",
     steps=["Start flow=0.", "Build residual graph (forward cap c-f, backward cap f).", "Find s-t path with positive residual capacity (BFS in Edmonds-Karp).", "Push bottleneck flow, update residual.", "Stop when no path; flow is maximum."],
     diagram="s→A(cap10)→t\ns→B(cap5)→t\nMax flow = 15",
     algorithm="Edmonds-Karp = Ford-Fulkerson + BFS for shortest augmenting path. Time O(VE²).",
     flowchart="Residual graph → find path → augment → repeat",
     example="Airline scheduling: maximize passengers routed through network.",
     advantages=["Edmonds-Karp polynomial", "Models many problems", "Min-cut gives bottleneck insight"],
     disadvantages=["Ford-Fulkerson alone can be slow without BFS", "Integer capacities assumed for termination"],
     applications=["Network routing", "Bipartite matching", "Image segmentation", "Airline scheduling"],
     exam_tips="Explain residual graph clearly — exam favourite topic.",
     mistakes="Not drawing reverse edges in residual graph.",
     comparison="Ford-Fulkerson=any path | Edmonds-Karp=BFS path → O(VE²)",
     time="Edmonds-Karp O(V E²)",
     space="O(V+E)",
     interview="What is residual graph? Max-flow min-cut theorem?",
     memory="Flow through Residual; EK = FF + BFS",
     mark5="Define max-flow min-cut. Residual graph. Edmonds-Karp steps. Small example.",
     mark10="Theorem, Ford-Fulkerson method, Edmonds-Karp with dry-run, applications, complexity.",
     one_liner="FF = augment in residual; EK = FF+BFS; max flow = min cut.")

rule("long", "floyd", "warshall",
     definition="<strong>Floyd-Warshall</strong> finds <em>all-pairs shortest paths</em> using dynamic programming in O(V³).",
     introduction="DP tries every intermediate vertex k to improve paths.",
     why="When you need distances between every pair of nodes (flight matrix).",
     working="For each k,i,j: dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j]).",
     steps=["Initialize dist from adjacency matrix (∞ if no edge, 0 diagonal).", "Loop k from 1 to V.", "Loop i,j: try k as intermediate.", "Output dist matrix."],
     diagram="3 nested loops over k, i, j",
     algorithm="Triple loop DP. Path reconstruction via predecessor matrix optional.",
     flowchart="For each intermediate k → update all pairs",
     example="Cheapest flight between every pair of cities in an airline network.",
     advantages=["Simple to code", "Handles negative weights (no negative cycles)", "All-pairs in one run"],
     disadvantages=["O(V³) slow for large V", "Fails with negative cycles", "No path info without extra matrix"],
     applications=["Transitive closure", "All-pairs routing", "Game map analysis"],
     exam_tips="State limitation: negative cycles. Paradigm: Dynamic Programming.",
     mistakes="Using for single-source only (use Dijkstra instead).",
     comparison="Dijkstra=single-source O((V+E)logV) | Floyd=all-pairs O(V³)",
     time="O(V³)",
     space="O(V²)",
     interview="When Floyd vs running Dijkstra V times?",
     memory="Floyd = For All pairs, 3 nested loops",
     mark5="Define, DP recurrence, triple loop, limitation (negative cycles), O(V³).",
     mark10="Full algorithm, 4-node dry-run, DP explanation, limitations, comparison with Dijkstra.",
     one_liner="Floyd-Warshall = DP over intermediates → all-pairs shortest paths in O(V³).")

rule("long", "np", "complete",
     definition="A problem is <strong>NP-complete</strong> if it is in NP (solution verifiable in polynomial time) AND is NP-hard (every NP problem reduces to it).",
     introduction="NP-complete problems are the hardest problems in NP.",
     why="Explains why many problems have no known fast exact algorithm.",
     working="Prove X in NP (verifier). Reduce known NP-complete Y to X in polynomial time.",
     steps=["Define NP, NP-hard, NP-complete.", "Give examples: SAT, 3-SAT, TSP, Vertex Cover.", "Explain reduction proof idea.", "Discuss P vs NP open problem.", "Mention approximations/heuristics."],
     diagram="SAT → 3-SAT → Vertex Cover → Your problem X",
     algorithm="Reduction: transform instance of Y to instance of X preserving yes/no answer.",
     flowchart="Verify in NP → Pick known NPC → Reduce → Conclude NPC",
     example="Sudoku generalization, timetable scheduling — no fast exact algorithm known.",
     advantages=["Classification helps choose approximation/heuristic", "Unified proof technique"],
     disadvantages=["No polynomial exact algorithm known", "Exact solutions exponential in worst case"],
     applications=["Scheduling", "Routing", "Boolean satisfiability", "Cryptography reductions"],
     exam_tips="Cook-Levin: SAT is first NP-complete. Know definition precisely.",
     mistakes="Confusing NP-hard with NP-complete (NP-hard may not be in NP).",
     comparison="P=solvable poly | NP=verify poly | NPC=hardest in NP",
     time="NP-complete decision: verifiable in polynomial time",
     space="Problem dependent",
     interview="Explain reduction. Is P=NP?",
     memory="NP-complete = in NP + NP-hard; prove by reduction",
     mark5="Define NP, NP-hard, NP-complete. Examples. Reduction idea. P vs NP open.",
     mark10="Full definitions, SAT example, reduction sketch, limitations, approximation strategies.",
     one_liner="NP-complete = in NP + NP-hard; prove by polynomial reduction from known NPC problem.")

# ==================== ACA ====================

rule("short", "parallelism",
     definition="<strong>Parallelism</strong> means doing multiple tasks at the same time using multiple processors to finish work faster.",
     key_points=["Needs multi-core/multi-CPU hardware.", "Needs parallel software design.", "Speedup limited by serial portion (Amdahl's Law)."],
     example="Restaurant kitchen — many chefs cook different dishes simultaneously.",
     exam_keyword="Concurrent execution · Multiple processors · Speedup",
     one_liner="Parallelism = many tasks at once using many processors.")

rule("short", "pram",
     definition="<strong>PRAM</strong> = Parallel Random Access Machine: many processors + shared memory + synchronous parallel steps.",
     key_points=["Theoretical model for algorithm design.", "Variants: EREW, CREW, CRCW (memory access rules).", "MCQ: shared memory + synchronous → PRAM."],
     example="All students reading the same whiteboard at the same clock tick.",
     exam_keyword="Shared memory · Synchronous · EREW/CREW/CRCW",
     one_liner="PRAM = shared memory + sync steps; used for theoretical analysis.")

rule("short", "multiprocessor", "multicomputer",
     definition="<strong>Multiprocessor</strong> = shared memory. <strong>Multicomputer</strong> = private memory + network messages.",
     key_points=["Multiprocessor: load/store to shared RAM (SMP, NUMA).", "Multicomputer: MPI message passing (clusters).", "Multiprocessor easier to program; multicomputer scales higher."],
     example="Multiprocessor = one office whiteboard. Multicomputer = separate offices emailing files.",
     exam_keyword="Shared vs distributed memory · MPI vs shared variables",
     one_liner="Multiprocessor=shared memory; Multicomputer=private memory+network.")

rule("long", "amdahl", "gustafson",
     definition="<strong>Amdahl's Law:</strong> Speedup = 1/(s+(1-s)/N), fixed problem. <strong>Gustafson's Law:</strong> Speedup = s+N(1-s), scaled problem.",
     introduction="Two views of parallel speedup limits.",
     why="Predict whether adding cores will help your application.",
     working="Amdahl: serial fraction s limits max speedup. Gustafson: bigger problems make serial part tiny.",
     steps=["Define s = serial fraction, N = processors.", "Write both formulas.", "Numeric example s=0.1, N=10.", "Compare pessimistic vs optimistic views."],
     diagram="Amdahl: 1 cashier bottleneck | Gustafson: bigger factory orders",
     algorithm="Plug s and N into formulas.",
     flowchart="Fixed problem → Amdahl | Scaled problem → Gustafson",
     example="s=0.1, N=10: Amdahl≈5.26×; max with ∞ cores = 10×.",
     advantages=["Simple performance models", "Explains real scaling behaviour"],
     disadvantages=["Amdahl pessimistic for fixed workloads", "Gustafson assumes scaled workload"],
     applications=["HPC planning", "Cloud capacity", "Multi-core design"],
     exam_tips="Always show numeric substitution in exam.",
     mistakes="Using wrong formula for fixed vs scaled problem.",
     comparison="<tr><th></th><th>Amdahl</th><th>Gustafson</th></tr><tr><td>Problem</td><td>Fixed</td><td>Scaled</td></tr><tr><td>View</td><td>Pessimistic</td><td>Optimistic</td></tr>",
     time="O(1) formula evaluation",
     space="N/A",
     interview="Explain serial bottleneck with example.",
     memory="Amdahl Always limits; Gustafson Grows problem",
     mark5="Both formulas + one numeric example each + when to use which.",
     mark10="Definitions, derivations intuition, 2 examples, comparison table, multicore relevance.",
     one_liner="Amdahl=fixed problem serial limit; Gustafson=scaled problem more optimistic.")

rule("long", "memory hierarchy",
     definition="<strong>Memory hierarchy</strong> layers storage from fast/small (registers) to slow/large (disk).",
     introduction="Bridges speed-cost gap in computer design.",
     why="Fast memory is expensive; hierarchy gives speed of cache with capacity of disk.",
     working="Check registers → L1 → L2 → L3 → RAM → disk on each access.",
     steps=["Draw pyramid.", "State size/speed at each level.", "Explain temporal and spatial locality.", "Explain cache hit vs miss impact."],
     diagram="Registers → L1 → L2 → L3 → RAM → Disk (fast to slow)",
     algorithm="On access: search hierarchy top-down until hit.",
     flowchart="Access → L1 hit? → L2? → ... → RAM → Disk",
     example="Mobile game: hot data in cache = smooth FPS; misses = stutter.",
     advantages=["Average access near cache speed", "Cost effective"],
     disadvantages=["Cache misses cause stalls", "Complex coherence in multiprocessors"],
     applications=["CPU design", "Database buffer pools", "OS paging"],
     exam_tips="Draw pyramid diagram — frequently asked.",
     mistakes="Saying more RAM always equals faster (locality matters).",
     comparison="Register fastest/smallest · Disk slowest/largest",
     time="Hit: few cycles; Miss: 100+ cycles to RAM",
     space="Hierarchy spans bytes to terabytes",
     interview="Temporal vs spatial locality?",
     memory="Fast/Small at top, Slow/Big at bottom",
     mark5="Pyramid diagram + locality + performance impact.",
     mark10="Full hierarchy, hit/miss, locality types, example, multiprocessor note.",
     one_liner="Hierarchy = Registers→Cache→RAM→Disk; locality makes it fast.")

rule("long", "pipeline", "instruction",
     definition="<strong>Instruction pipeline</strong> splits execution into stages so multiple instructions overlap.",
     introduction="RISC classic: IF, ID, EX, MEM, WB.",
     why="Increases throughput without raising clock rate.",
     working="Each stage works on different instruction simultaneously.",
     steps=["Name 5 stages.", "Draw timing diagram for 5 instructions.", "List 3 hazard types.", "Give one fix per hazard."],
     diagram="""IF ID EX MEM WB
Inst1: IF ID EX MEM WB
Inst2:    IF ID EX MEM WB
Inst3:       IF ID EX MEM WB""",
     algorithm="Each cycle advance all stages; handle hazards with stall/forwarding.",
     flowchart="Fetch → Decode → Execute → Memory → Writeback (pipelined)",
     example="Assembly line: body, paint, engine, test on different cars at once.",
     advantages=["Higher IPC", "Better hardware utilization"],
     disadvantages=["Hazards reduce efficiency", "Branch misprediction penalty"],
     applications=["All modern CPUs", "ARM", "RISC-V"],
     exam_tips="Draw timing chart — easy marks.",
     mistakes="Confusing latency (one instruction) with throughput (pipeline).",
     comparison="Linear pipeline=sequential stages | Superscalar=multiple pipelines",
     time="Latency ≥ sum of stages; throughput → 1 instr/cycle ideal",
     space="Pipeline registers between stages",
     interview="3 hazard types and solutions?",
     memory="Fine Dogs Eat My Waffles = IF ID EX MEM WB",
     mark5="5 stages, timing diagram, hazards list.",
     mark10="Full pipeline diagram, hazard details, forwarding example, superscalar contrast.",
     one_liner="Pipeline overlaps IF-ID-EX-MEM-WB → higher throughput; watch hazards.")

rule("long", "cache coherence",
     definition="<strong>Cache coherence</strong> ensures all CPU caches show the same value for shared data.",
     introduction="Multiprocessors share memory — each core has private cache.",
     why="Without coherence, cores see different values → program errors.",
     working="Snooping protocols track line states: Modified, Shared, Invalid (MSI/MESI).",
     steps=["Describe problem: CPU1 writes, CPU2 stale.", "Explain MSI states.", "Write invalidation on write.", "Give snooping bus example."],
     diagram="CPU1 cache M | CPU2 cache I after write",
     algorithm="On write: invalidate other copies. On read miss: fetch from owner or memory.",
     flowchart="Read hit/miss → Write → Invalidate others → Update state",
     example="Two cores updating shared counter — coherence keeps count correct.",
     advantages=["Correct shared-memory programs", "Hardware-transparent to programmer"],
     disadvantages=["Bus traffic", "Complexity in large systems"],
     applications=["Multicore desktops", "SMP servers", "NUMA machines"],
     exam_tips="Know MSI/MESI state names.",
     mistakes="Confusing coherence with consistency (ordering).",
     comparison="Coherence=same value | Consistency=operation ordering",
     time="Protocol-dependent",
     space="Directory or snoop metadata",
     interview="MESI states explained?",
     memory="Modified Exclusive Shared Invalid",
     mark5="Problem, MSI states, example invalidation.",
     mark10="Full protocol, diagram, example sequence, vs consistency.",
     one_liner="Cache coherence = all caches agree on shared data; MSI/MESI protocols.")

# ==================== PARALLEL COMPUTING ====================

rule("short", "parallel computing",
     definition="<strong>Parallel computing</strong> uses multiple processors working together on one problem to reduce time or handle larger data.",
     key_points=["Needs parallel hardware + parallel software.", "Models: shared memory (PThreads) or distributed (MPI).", "Goal: speedup, scalability, throughput."],
     example="10 courier agents delivering in different zones simultaneously.",
     exam_keyword="Simultaneous execution · Speedup · MPI/PThreads",
     one_liner="Parallel computing = many processors on one problem at the same time.")

rule("short", "flynn",
     definition="<strong>Flynn's classification</strong> categorizes architectures by instruction streams and data streams.",
     key_points=["SISD: 1 instr, 1 data (PC).", "SIMD: 1 instr, many data (GPU).", "MIMD: many instr, many data (cluster/multicore)."],
     example="SIMD = same filter on every pixel; MIMD = different apps on each core.",
     exam_keyword="SISD SIMD MISD MIMD",
     one_liner="Flynn = classify by Single/Multiple Instruction × Single/Multiple Data.")

rule("short", "mpi",
     definition="<strong>MPI</strong> (Message Passing Interface) is the standard for programming <em>distributed memory</em> systems where processes communicate by sending messages.",
     key_points=["Each process has private memory.", "Rank identifies process in communicator.", "Collective ops: Bcast, Reduce, Barrier."],
     example="Separate warehouses exchanging packages (messages) instead of sharing one shelf.",
     exam_keyword="Distributed memory · Rank · Send/Recv · Bcast",
     one_liner="MPI = message passing on distributed memory; Rank = process ID.")

rule("short", "mutex",
     definition="A <strong>mutex</strong> (mutual exclusion lock) allows only <em>one thread at a time</em> in a critical section.",
     key_points=["pthread_mutex_lock() before shared access.", "pthread_mutex_unlock() after.", "Prevents race conditions on shared data."],
     example="One person at a time using a shared bathroom key.",
     exam_keyword="Critical section · pthread_mutex · race condition",
     one_liner="Mutex = only one thread in critical section at a time.")

rule("long", "communication", "broadcast", "gather",
     definition="Collective communication patterns move data between parallel processes efficiently.",
     introduction="MPI provides standard patterns instead of ad-hoc messaging.",
     why="Common operations optimized by MPI library and network.",
     working="Broadcast=1→all same; Scatter=1→all different; Gather=all→1; Reduce=all→1 computed.",
     steps=["Define each pattern.", "Give MPI function name.", "Draw diagram.", "Give real-life analogy."],
     diagram="Broadcast: root sends to all | Gather: all send to root",
     algorithm="MPI_Bcast, MPI_Scatter, MPI_Gather, MPI_Reduce, MPI_Barrier",
     flowchart="Choose pattern → call MPI collective → synchronize if needed",
     example="Manager (Broadcast) announces schedule to all workers.",
     advantages=["Optimized implementations", "Portable standard", "Collective efficiency"],
     disadvantages=["Must match all processes", "Deadlock if misused"],
     applications=["HPC simulations", "MapReduce-style reductions", "Parallel sorting"],
     exam_tips="MCQ: one-to-all = Broadcast; wait all = Barrier.",
     mistakes="Confusing Scatter with Broadcast.",
     comparison="Broadcast=same data | Scatter=different chunks | Reduce=computed sum/max",
     time="Depends on message size and network",
     space="Buffers at sender/receiver",
     interview="Difference Bcast vs Scatter?",
     memory="BSGR = Broadcast Scatter Gather Reduce",
     mark5="Define Broadcast, Gather, Reduce, Barrier with MPI names and diagrams.",
     mark10="All major collectives, diagrams, MPI examples, use cases.",
     one_liner="Broadcast=1→all; Gather=all→1; Reduce=all→1 computed; Barrier=sync.")

rule("long", "pthreads", "synchronization",
     definition="<strong>PThreads</strong> provides threads sharing one address space. Sync via mutex, semaphore, condition variables.",
     introduction="Shared-memory parallelism on multicore.",
     why="Threads lighter than processes; fast shared data access.",
     working="pthread_create starts thread; mutex protects critical section; join waits for finish.",
     steps=["Create thread.", "Lock mutex before shared update.", "Unlock after.", "pthread_join to wait."],
     diagram="Main thread + worker threads → shared memory region (protected by mutex)",
     algorithm="pthread_create / mutex_lock / unlock / join",
     flowchart="Create threads → parallel work → lock shared section → unlock → join",
     example="Multiple cashiers updating one shared inventory count safely with mutex.",
     advantages=["Fast shared memory", "Lightweight vs processes"],
     disadvantages=["Race conditions without sync", "Harder to debug"],
     applications=["Multicore apps", "Web servers", "Game engines"],
     exam_tips="PThreads=shared address; MPI=separate addresses.",
     mistakes="Forgetting to unlock mutex (deadlock).",
     comparison="Mutex=binary lock | Semaphore=counting lock",
     time="Thread ops microseconds",
     space="Shared heap + per-thread stack",
     interview="Mutex vs semaphore?",
     memory="MPI=Messages, PThreads=Shared memory",
     mark5="Thread creation, mutex, critical section, join.",
     mark10="Architecture, code sketch, mutex vs semaphore, race example, deadlock note.",
     one_liner="PThreads=shared memory threads; Mutex=one-at-a-time critical section.")

rule("long", "dfs", "bfs",
     definition="<strong>DFS</strong> uses Stack (deep first). <strong>BFS</strong> uses Queue (level first).",
     introduction="Fundamental parallel graph search strategies.",
     why="Graph algorithms on social networks, maps, web crawling.",
     working="DFS: recurse/stack. BFS: queue frontier level by level.",
     steps=["Define both.", "Write algorithms.", "Compare data structures.", "Parallel notes: BFS frontier sync; DFS speculative overhead."],
     diagram="DFS deep path; BFS ring by ring",
     algorithm="Standard DFS/BFS pseudocode; parallel BFS distributes frontier.",
     flowchart="DFS: stack pop/push | BFS: queue dequeue/enqueue",
     example="DFS=maze; BFS=shortest hops in unweighted social graph.",
     advantages=["BFS shortest unweighted", "DFS less memory on deep trees"],
     disadvantages=["DFS not shortest", "BFS wide graphs need memory"],
     applications=["Web crawl", "Connected components", "Social networks"],
     exam_tips="Parallel BFS uses distributed frontier (queue).",
     mistakes="Using wrong data structure.",
     comparison="<tr><th></th><th>DFS</th><th>BFS</th></tr><tr><td>DS</td><td>Stack</td><td>Queue</td></tr><tr><td>Shortest</td><td>No</td><td>Yes (unweighted)</td></tr>",
     time="O(V+E) sequential",
     space="O(V) frontier/stack",
     interview="When BFS over DFS in parallel?",
     memory="DFS=Stack deep; BFS=Queue levels",
     mark5="Algorithms, comparison table, one graph example.",
     mark10="Full comparison, parallel notes, graph traversal example, applications.",
     one_liner="DFS=Stack+deep; BFS=Queue+levels+shortest unweighted.")

# ==================== RPA ====================

rule("short", "rpa",
     definition="<strong>RPA</strong> uses software bots to automate repetitive, rule-based computer tasks by mimicking human clicks and typing.",
     key_points=["Works on existing apps — no backend change.", "Best for structured, high-volume tasks.", "24/7 operation with audit trail."],
     example="Bank bot reads loan PDF, enters data into core banking system, sends email.",
     exam_keyword="Software bots · Rule-based · Non-invasive",
     one_liner="RPA = software robots automating repetitive manual computer tasks.")

rule("short", "control room",
     definition="<strong>Web Control Room</strong> is the central web console to deploy, schedule, monitor, and manage bots.",
     key_points=["Panels: Dashboard, Activity, Bots, Devices, Workload, Audit.", "Upload bots and manage credentials.", "Monitor running and scheduled tasks."],
     example="Airport control tower managing all flights — Control Room manages all bots.",
     exam_keyword="Dashboard · Activity · Bots · Audit Log",
     one_liner="Control Room = central hub to manage, schedule, and monitor all bots.")

rule("short", "device pool",
     definition="A <strong>device pool</strong> is a group of machines (runtime/development clients) where bots can be assigned to run.",
     key_points=["Load balancing across machines.", "If one machine busy, bot runs on another.", "Links to Workload queues."],
     example="5 PCs in pool processing insurance claims — bot auto-assigns to free PC.",
     exam_keyword="Runtime client · Load balancing · Workload",
     one_liner="Device pool = group of machines for bot execution and load sharing.")

rule("long", "automation anywhere", "features",
     definition="<strong>Automation Anywhere Enterprise</strong> = Bot Creator + Control Room + Bot Runner + IQ Bot + Credential Vault.",
     introduction="Leading enterprise RPA cloud platform.",
     why="Centralized bot lifecycle from development to production monitoring.",
     working="Create in Bot Creator → upload to Control Room → schedule on device pool → Bot Runner executes.",
     steps=["List components.", "Attended vs Unattended bots.", "IQ Bot OCR/AI.", "Credential Vault.", "Bot Insight analytics."],
     diagram="Creator → Control Room → Runner → Target apps (SAP/Excel/Web)",
     algorithm="Design → Upload → Schedule → Execute → Monitor → Audit",
     flowchart="Record/Build → Deploy → Run → Monitor",
     example="Bank: 50 bots process KYC documents nightly via Control Room schedule.",
     advantages=["Enterprise scale", "Audit/compliance", "AI document processing"],
     disadvantages=["License cost", "UI change breaks bots", "Not for complex judgment"],
     applications=["Banking KYC", "HR onboarding", "Invoice processing", "Insurance claims"],
     exam_tips="Mid-I Q1 favourite — list all components clearly.",
     mistakes="Confusing Bot Creator with Control Room roles.",
     comparison="Creator=build | Control Room=manage | Runner=execute",
     time="Bots run 24/7",
     space="Cloud + on-prem runners",
     interview="AA architecture components?",
     memory="CCR = Creator Control Runner",
     mark5="Components list + one-line role each + attended/unattended.",
     mark10="Architecture diagram, features, enterprise example, IQ Bot note.",
     one_liner="AA = Creator builds, Control Room manages, Runner executes, IQ Bot reads documents.")

rule("long", "benefits", "limitations", "rpa",
     definition="<strong>RPA</strong> automates rule-based digital work using software bots.",
     introduction="Enterprise adoption driven by cost and accuracy gains.",
     why="Humans spend 60-80% time on repetitive tasks; bots work 24/7.",
     working="Bot mimics human UI interaction: login, read screen, enter data, submit.",
     steps=["List benefits with examples.", "List limitations honestly.", "Give bank/hospital/HR examples.", "Conclude when RPA fits vs not."],
     diagram="Human task → Bot replicates → 24/7 execution → Audit log",
     algorithm="Identify rule-based process → Record → Test → Deploy → Monitor",
     flowchart="Rule-based? → Yes:RPA | No: consider AI/human",
     example="Hospital: bot extracts discharge codes, fills insurance claim form.",
     advantages=["60-80% cost saving", "Near-zero errors", "24/7", "Audit trail", "Fast ROI"],
     disadvantages=["No emotional judgment", "UI dependency", "Exception handling", "Maintenance"],
     applications=["Banking", "Insurance", "HR", "Payroll", "Customer support"],
     exam_tips="Must give BOTH benefits AND limitations with industry examples.",
     mistakes="Saying RPA replaces all human jobs or handles all decisions.",
     comparison="RPA=UI automation | Traditional integration=API level",
     time="ROI often 3-12 months",
     space="Cloud/on-prem infrastructure",
     interview="When NOT to use RPA?",
     memory="Benefits ASSC (Accuracy Speed Scale Compliance)",
     mark5="Define RPA + 4 benefits + 3 limitations + 2 examples.",
     mark10="Full evaluation with bank/hospital cases, architecture, limits, ROI discussion.",
     one_liner="RPA wins on speed/accuracy/24-7; loses on complex judgment and UI changes.")

rule("long", "recorder", "smart", "web", "screen",
     definition="Three recorders build bots: <strong>Smart</strong> (desktop/ERP), <strong>Web</strong> (browser), <strong>Screen</strong> (coordinates/Citrix).",
     introduction="Recorders capture user actions and generate bot commands.",
     why="Faster bot development than manual coding.",
     working="Smart=AI object ID; Web=HTML selectors; Screen=pixel coordinates.",
     steps=["Compare three recorders.", "Best use case each.", "Give HR/bank example.", "Mention Task Editor customization."],
     diagram="Smart→SAP | Web→Portal | Screen→Legacy Citrix",
     algorithm="Start recorder → perform actions → stop → edit in Task Editor",
     flowchart="Pick recorder type → Record → Edit → Test → Publish",
     example="Web recorder captures insurance portal login and form fill.",
     advantages=["Fast development", "Low coding", "Smart handles UI changes better"],
     disadvantages=["Screen recorder fragile on resolution change", "Recorded bots need cleanup"],
     applications=["ERP automation", "Web portals", "Legacy Citrix apps"],
     exam_tips="Differentiate all three recorders in table.",
     mistakes="Using Screen recorder when Web recorder would be better.",
     comparison="<tr><th>Smart</th><th>Web</th><th>Screen</th></tr><tr><td>Desktop</td><td>Browser</td><td>Any/Citrix</td></tr>",
     time="Record session minutes",
     space="Bot file in Control Room",
     interview="Which recorder for SAP vs Chrome?",
     memory="SWS = Smart Web Screen",
     mark5="Three recorders table + one example each.",
     mark10="Detailed comparison, recording workflow, Task Editor, enterprise example.",
     one_liner="Smart=desktop AI; Web=browser HTML; Screen=coordinates/legacy.")
