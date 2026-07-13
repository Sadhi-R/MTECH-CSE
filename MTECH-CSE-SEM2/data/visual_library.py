# -*- coding: utf-8 -*-
"""SVG visual examples for short and long question bank answers."""

from __future__ import annotations

# ---- SVG helpers ----

def _svg(content: str, w: int = 520, h: int = 240, compact: bool = False) -> str:
    cls = "visual-svg visual-compact" if compact else "visual-svg"
    return (
        f'<div class="visual-example">'
        f'<p class="diagram-label">Visual Example</p>'
        f'<svg class="{cls}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img">'
        f"{content}</svg></div>"
    )


def _node(x, y, label, fill="#0d9488", r=22):
    return (
        f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="#0f172a" stroke-width="2"/>'
        f'<text x="{x}" y="{y+5}" text-anchor="middle" fill="#fff" font-size="14" font-weight="600">{label}</text>'
    )


def _edge(x1, y1, x2, y2, label="", dashed=False):
    dash = ' stroke-dasharray="6,4"' if dashed else ""
    mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
    lbl = f'<text x="{mid_x}" y="{mid_y-6}" text-anchor="middle" fill="#475569" font-size="11">{label}</text>' if label else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#64748b" stroke-width="2"{dash}/>{lbl}'


def _rect(x, y, w, h, label, fill="#1e293b"):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="{x+w/2}" y="{y+h/2+5}" text-anchor="middle" fill="#fff" font-size="12" font-weight="600">{label}</text>'
    )


def _arrow(x1, y1, x2, y2):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#0d9488" stroke-width="2" marker-end="url(#arr)"/>'


def _defs():
    return (
        '<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
        '<path d="M0,0 L6,3 L0,6 Z" fill="#0d9488"/></marker></defs>'
    )


# ---- Topic SVG builders ----

def vis_bfs(compact=False):
    c = (
        _defs()
        + _node(80, 120, "A", "#0d9488")
        + _node(200, 70, "B", "#38bdf8")
        + _node(200, 170, "C", "#38bdf8")
        + _node(320, 120, "D", "#f59e0b")
        + _edge(102, 120, 178, 70) + _edge(102, 120, 178, 170)
        + _edge(222, 70, 298, 120) + _edge(222, 170, 298, 120)
        + '<text x="80" y="30" fill="#0f172a" font-size="13" font-weight="700">BFS — Level by Level (Queue)</text>'
        + '<text x="80" y="210" fill="#64748b" font-size="11">Level 0: A → Level 1: B,C → Level 2: D (shortest = 2 hops)</text>'
    )
    return _svg(c, 420, 230, compact)


def vis_dfs(compact=False):
    c = (
        _defs()
        + _node(80, 120, "A", "#0d9488")
        + _node(180, 70, "B", "#38bdf8")
        + _node(280, 70, "D", "#f59e0b")
        + _node(180, 170, "C", "#a78bfa")
        + _edge(102, 120, 158, 70) + _edge(202, 70, 258, 70) + _edge(102, 120, 158, 170)
        + '<path d="M80,120 L180,70 L280,70" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="8,4"/>'
        + '<text x="80" y="30" fill="#0f172a" font-size="13" font-weight="700">DFS — Go Deep First (Stack)</text>'
        + '<text x="80" y="210" fill="#64748b" font-size="11">Path A→B→D (red dashed) before backtracking to C</text>'
    )
    return _svg(c, 420, 230, compact)


def vis_dijkstra(compact=False):
    c = (
        _defs()
        + _node(70, 120, "A", "#0d9488")
        + _node(190, 70, "B", "#38bdf8")
        + _node(190, 170, "C", "#38bdf8")
        + _node(310, 120, "D", "#f59e0b")
        + _edge(92, 120, 168, 70, "4") + _edge(92, 120, 168, 170, "2")
        + _edge(212, 70, 288, 120, "1") + _edge(212, 170, 288, 120, "3")
        + '<text x="60" y="30" fill="#0f172a" font-size="13" font-weight="700">Dijkstra — Min-Heap (non-negative weights)</text>'
        + '<text x="60" y="210" fill="#64748b" font-size="11">A→C→D = 2+3 = 5 (cheapest path highlighted)</text>'
        + '<path d="M70,120 L190,170 L310,120" fill="none" stroke="#ef4444" stroke-width="3"/>'
    )
    return _svg(c, 420, 230, compact)


def vis_mst(compact=False):
    c = (
        _defs()
        + _node(100, 80, "A", "#0d9488")
        + _node(260, 80, "B", "#0d9488")
        + _node(100, 180, "C", "#0d9488")
        + _node(260, 180, "D", "#0d9488")
        + _edge(122, 80, 238, 80, "4", True)
        + _edge(100, 102, 100, 158, "2")
        + _edge(122, 180, 238, 180, "3")
        + _edge(122, 102, 238, 158, "1")
        + _edge(260, 102, 260, 158, "5", True)
        + '<line x1="122" y1="102" x2="238" y2="158" stroke="#ef4444" stroke-width="4"/>'
        + '<line x1="100" y1="102" x2="100" y2="158" stroke="#ef4444" stroke-width="4"/>'
        + '<line x1="122" y1="180" x2="238" y2="180" stroke="#ef4444" stroke-width="4"/>'
        + '<text x="60" y="30" fill="#0f172a" font-size="13" font-weight="700">MST — Minimum Cost Connect All (red = chosen)</text>'
        + '<text x="60" y="220" fill="#64748b" font-size="11">Total MST cost = 2 + 1 + 3 = 6</text>'
    )
    return _svg(c, 420, 240, compact)


def vis_maxflow(compact=False):
    c = (
        _defs()
        + _rect(30, 90, 50, 40, "s", "#0d9488")
        + _rect(130, 50, 50, 40, "A", "#38bdf8")
        + _rect(130, 140, 50, 40, "B", "#38bdf8")
        + _rect(250, 90, 50, 40, "t", "#f59e0b")
        + _arrow(80, 110, 130, 70) + _arrow(80, 110, 130, 160)
        + _arrow(180, 70, 250, 110) + _arrow(180, 160, 250, 110)
        + '<text x="95" y="55" fill="#475569" font-size="10">10</text>'
        + '<text x="95" y="145" fill="#475569" font-size="10">5</text>'
        + '<text x="210" y="85" fill="#475569" font-size="10">8</text>'
        + '<text x="210" y="145" fill="#475569" font-size="10">7</text>'
        + '<text x="30" y="30" fill="#0f172a" font-size="13" font-weight="700">Max-Flow — Push flow s→t through network</text>'
        + '<text x="30" y="210" fill="#64748b" font-size="11">Max flow = 15 (limited by min-cut capacity)</text>'
    )
    return _svg(c, 380, 230, compact)


def vis_toposort(compact=False):
    c = (
        _defs()
        + _node(80, 100, "Math", "#0d9488", 28)
        + _node(220, 60, "OS", "#38bdf8", 28)
        + _node(220, 140, "DB", "#38bdf8", 28)
        + _node(360, 100, "Cloud", "#f59e0b", 28)
        + _arrow(108, 100, 192, 60) + _arrow(108, 100, 192, 140)
        + _arrow(248, 60, 332, 100) + _arrow(248, 140, 332, 100)
        + '<text x="40" y="30" fill="#0f172a" font-size="13" font-weight="700">DAG + Topological Sort (prerequisites)</text>'
        + '<text x="40" y="200" fill="#64748b" font-size="11">Valid order: Math → OS → Cloud  (or Math → DB → Cloud)</text>'
    )
    return _svg(c, 440, 220, compact)


def vis_sorting(compact=False):
    c = (
        _defs()
        + "".join(_rect(40 + i * 55, 120 - h * 8, 40, h * 8, str(v), "#38bdf8" if i % 2 else "#0d9488")
                  for i, (v, h) in enumerate([(8, 8), (3, 3), (5, 5), (1, 1), (9, 9), (2, 2)]))
        + '<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">Sorting — Arrange elements in order</text>'
        + '<text x="40" y="210" fill="#64748b" font-size="11">Before: [8,3,5,1,9,2] → After: [1,2,3,5,8,9]</text>'
        + "".join(_rect(40 + i * 55, 170 - h * 8, 40, h * 8, str(v), "#f59e0b")
                  for i, (v, h) in enumerate([(1, 1), (2, 2), (3, 3), (5, 5), (8, 8), (9, 9)]))
    )
    return _svg(c, 420, 240, compact)


def vis_pipeline(compact=False):
    stages = ["IF", "ID", "EX", "MEM", "WB"]
    c = _defs()
    for i, s in enumerate(stages):
        c += _rect(30 + i * 95, 60, 80, 40, s, "#1e293b")
        if i < 4:
            c += _arrow(110 + i * 95, 80, 125 + i * 95, 80)
    for row, label in enumerate(["Inst1", "Inst2", "Inst3"]):
        y = 130 + row * 35
        c += f'<text x="10" y="{y+5}" fill="#64748b" font-size="11">{label}</text>'
        for col in range(5 - row):
            c += _rect(30 + (col + row) * 95, y - 12, 80, 24, stages[col], "#0d9488" if row == 0 else "#38bdf8" if row == 1 else "#f59e0b")
    c += '<text x="30" y="30" fill="#0f172a" font-size="13" font-weight="700">Instruction Pipeline — Overlap stages</text>'
    return _svg(c, 520, 250, compact)


def vis_memory_hierarchy(compact=False):
    layers = [("Registers", 60, "#0d9488"), ("L1 Cache", 100, "#14b8a6"), ("L2/L3", 140, "#38bdf8"), ("RAM", 180, "#6366f1"), ("Disk", 220, "#94a3b8")]
    c = _defs() + '<text x="160" y="30" fill="#0f172a" font-size="13" font-weight="700" text-anchor="middle">Memory Hierarchy Pyramid</text>'
    for i, (name, w, color) in enumerate(layers):
        x = 260 - w / 2
        c += _rect(x, 50 + i * 38, w, 32, name, color)
        c += f'<text x="400" y="{66 + i * 38}" fill="#64748b" font-size="10">{"Fastest" if i == 0 else "Slowest" if i == 4 else "↓"}</text>'
    return _svg(c, 480, 260, compact)


def vis_amdahl(compact=False):
    c = (
        _defs()
        + _rect(40, 80, 80, 100, "Serial\n10%", "#ef4444")
        + _rect(130, 80, 280, 100, "Parallel 90% — split across N cores", "#0d9488")
        + '<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">Amdahl\'s Law — Serial part limits speedup</text>'
        + '<text x="40" y="210" fill="#64748b" font-size="11">Speedup = 1 / (0.1 + 0.9/N)  →  max ≈ 10× even with ∞ cores</text>'
    )
    return _svg(c, 460, 230, compact)


def vis_flynn(compact=False):
    c = (
        _defs()
        + _rect(40, 50, 200, 160, "", "#f8fafc")
        + '<line x1="140" y1="50" x2="140" y2="210" stroke="#cbd5e1" stroke-width="2"/>'
        + '<line x1="40" y1="130" x2="240" y2="130" stroke="#cbd5e1" stroke-width="2"/>'
        + _rect(50, 60, 80, 60, "SISD\n(PC)", "#94a3b8")
        + _rect(150, 60, 80, 60, "SIMD\n(GPU)", "#0d9488")
        + _rect(50, 140, 80, 60, "MISD\n(rare)", "#64748b")
        + _rect(150, 140, 80, 60, "MIMD\n(cluster)", "#38bdf8")
        + '<text x="40" y="30" fill="#0f172a" font-size="13" font-weight="700">Flynn\'s Classification</text>'
        + '<text x="250" y="80" fill="#64748b" font-size="10">Single/Multiple</text>'
        + '<text x="250" y="95" fill="#64748b" font-size="10">Instruction</text>'
    )
    return _svg(c, 420, 230, compact)


def vis_mpi(compact=False):
    c = (
        _defs()
        + _rect(30, 70, 70, 50, "P0", "#0d9488")
        + _rect(130, 70, 70, 50, "P1", "#38bdf8")
        + _rect(230, 70, 70, 50, "P2", "#6366f1")
        + _rect(330, 70, 70, 50, "P3", "#f59e0b")
        + _arrow(100, 95, 130, 95) + _arrow(200, 95, 230, 95) + _arrow(300, 95, 330, 95)
        + '<text x="30" y="40" fill="#0f172a" font-size="13" font-weight="700">MPI — Message Passing (distributed memory)</text>'
        + '<text x="30" y="160" fill="#64748b" font-size="11">Each process has private memory; Send/Recv/Bcast move data</text>'
        + _rect(130, 150, 120, 35, "Shared Network", "#e2e8f0")
    )
    return _svg(c, 440, 210, compact)


def vis_pthreads(compact=False):
    c = (
        _defs()
        + _rect(40, 60, 360, 100, "Shared Memory (Heap)", "#e2e8f0")
        + _rect(60, 80, 80, 30, "Thread 1", "#0d9488")
        + _rect(180, 80, 80, 30, "Thread 2", "#38bdf8")
        + _rect(300, 80, 80, 30, "Thread 3", "#6366f1")
        + _rect(150, 120, 120, 25, "Mutex Lock 🔒", "#ef4444")
        + '<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">PThreads — Shared memory + Mutex sync</text>'
        + '<text x="40" y="190" fill="#64748b" font-size="11">Only one thread enters critical section at a time</text>'
    )
    return _svg(c, 440, 210, compact)


def vis_cache_coherence(compact=False):
    c = (
        _defs()
        + _rect(40, 60, 100, 60, "CPU1 Cache\nM (Modified)", "#ef4444")
        + _rect(200, 60, 100, 60, "CPU2 Cache\nI (Invalid)", "#94a3b8")
        + _rect(120, 150, 100, 40, "Main Memory", "#6366f1")
        + _arrow(140, 90, 200, 90)
        + '<text x="155" y="85" fill="#475569" font-size="10">invalidate</text>'
        + '<text x="40" y="30" fill="#0f172a" font-size="13" font-weight="700">Cache Coherence — MSI states</text>'
        + '<text x="40" y="220" fill="#64748b" font-size="11">CPU1 writes → CPU2 copy marked Invalid → same value everywhere</text>'
    )
    return _svg(c, 400, 240, compact)


def vis_rpa_arch(compact=False):
    c = (
        _defs()
        + _rect(30, 80, 90, 50, "Bot\nCreator", "#0d9488")
        + _rect(160, 70, 110, 70, "Control\nRoom", "#1e293b")
        + _rect(310, 80, 90, 50, "Bot\nRunner", "#38bdf8")
        + _arrow(120, 105, 160, 105) + _arrow(270, 105, 310, 105)
        + _rect(160, 170, 110, 35, "Target Apps (SAP/Excel/Web)", "#f59e0b")
        + _arrow(215, 140, 215, 170)
        + '<text x="30" y="40" fill="#0f172a" font-size="13" font-weight="700">RPA Architecture — Build → Manage → Execute</text>'
    )
    return _svg(c, 440, 220, compact)


def vis_control_room(compact=False):
    panels = ["Dashboard", "Activity", "Bots", "Devices", "Audit"]
    c = _defs() + '<text x="30" y="30" fill="#0f172a" font-size="13" font-weight="700">Web Control Room Panels</text>'
    for i, p in enumerate(panels):
        c += _rect(30 + (i % 3) * 130, 55 + (i // 3) * 55, 115, 42, p, "#1e293b" if i == 0 else "#0d9488" if i < 3 else "#6366f1")
    c += '<text x="30" y="175" fill="#64748b" font-size="11">Central console: deploy, schedule, monitor, audit all bots</text>'
    return _svg(c, 420, 200, compact)


def vis_device_pool(compact=False):
    c = (
        _defs()
        + _rect(180, 40, 120, 40, "Control Room", "#1e293b")
        + _arrow(240, 80, 240, 100)
        + _rect(60, 110, 80, 45, "PC-1 ✓", "#0d9488")
        + _rect(160, 110, 80, 45, "PC-2 ✓", "#0d9488")
        + _rect(260, 110, 80, 45, "PC-3 …", "#94a3b8")
        + '<text x="30" y="180" fill="#0f172a" font-size="12" font-weight="700">Device Pool — Load balance bots across machines</text>'
    )
    return _svg(c, 400, 200, compact)


def vis_recorders(compact=False):
    c = (
        _defs()
        + _rect(30, 70, 100, 55, "Smart\n(SAP/Desktop)", "#0d9488")
        + _rect(160, 70, 100, 55, "Web\n(Browser)", "#38bdf8")
        + _rect(290, 70, 100, 55, "Screen\n(Citrix)", "#6366f1")
        + '<text x="30" y="40" fill="#0f172a" font-size="13" font-weight="700">Three Recorders — Pick by application type</text>'
        + '<text x="30" y="160" fill="#64748b" font-size="11">Smart=object ID | Web=HTML | Screen=coordinates</text>'
    )
    return _svg(c, 430, 190, compact)


def vis_matrix_mult(compact=False):
    c = (
        _defs()
        + _rect(40, 70, 60, 80, "A\n3×3", "#0d9488")
        + '<text x="115" y="115" fill="#0f172a" font-size="20">×</text>'
        + _rect(140, 70, 60, 80, "B\n3×3", "#38bdf8")
        + '<text x="215" y="115" fill="#0f172a" font-size="20">=</text>'
        + _rect(240, 70, 60, 80, "C\n3×3", "#f59e0b")
        + '<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">Matrix Multiplication — Row × Column</text>'
        + '<text x="40" y="180" fill="#64748b" font-size="11">Parallel: split rows of A across processors</text>'
    )
    return _svg(c, 340, 200, compact)


def vis_np(compact=False):
    c = (
        _defs()
        + _rect(40, 70, 80, 45, "P\n(poly)", "#0d9488")
        + _rect(160, 70, 80, 45, "NP\n(verify poly)", "#38bdf8")
        + _rect(280, 70, 100, 45, "NP-Complete\n(hardest)", "#ef4444")
        + _arrow(120, 92, 160, 92) + _arrow(240, 92, 280, 92)
        + '<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">Complexity Classes — P vs NP</text>'
        + '<text x="40" y="150" fill="#64748b" font-size="11">NP-complete: SAT, TSP, Vertex Cover — no known poly exact algo</text>'
    )
    return _svg(c, 420, 180, compact)


def vis_graph_colouring(compact=False):
    c = (
        _defs()
        + _node(100, 100, "1", "#ef4444")
        + _node(200, 60, "2", "#38bdf8")
        + _node(200, 140, "3", "#0d9488")
        + _node(300, 100, "4", "#f59e0b")
        + _edge(122, 100, 178, 60) + _edge(122, 100, 178, 140)
        + _edge(222, 60, 278, 100) + _edge(222, 140, 278, 100)
        + _edge(200, 82, 200, 118)
        + '<text x="40" y="30" fill="#0f172a" font-size="13" font-weight="700">Graph Colouring — No adjacent same colour</text>'
        + '<text x="40" y="200" fill="#64748b" font-size="11">χ(G) = 3 here (minimum colours needed)</text>'
    )
    return _svg(c, 400, 220, compact)


def vis_fft(compact=False):
    c = (
        _defs()
        + _rect(30, 90, 90, 40, "Coeffs\nO(n²)", "#94a3b8")
        + _arrow(120, 110, 150, 110)
        + _rect(155, 90, 90, 40, "DFT/FFT\nO(n log n)", "#0d9488")
        + _arrow(245, 110, 275, 110)
        + _rect(280, 90, 90, 40, "Pointwise\n×", "#38bdf8")
        + '<text x="30" y="40" fill="#0f172a" font-size="13" font-weight="700">FFT — Fast polynomial multiply</text>'
        + '<text x="30" y="170" fill="#64748b" font-size="11">Evaluate → multiply points → inverse FFT</text>'
    )
    return _svg(c, 400, 200, compact)


def vis_parallelism(compact=False):
    c = (
        _defs()
        + "".join(_rect(40 + i * 90, 80, 70, 50, f"Core {i+1}", "#0d9488") for i in range(4))
        + '<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">Parallelism — Multiple cores work simultaneously</text>'
        + '<text x="40" y="160" fill="#64748b" font-size="11">Task split across cores → finish faster (limited by serial part)</text>'
    )
    return _svg(c, 420, 190, compact)


def vis_shared_vs_distributed(compact=False):
    c = (
        _defs()
        + _rect(30, 60, 160, 100, "Shared Memory\n(one RAM, all CPUs)", "#0d9488")
        + _rect(230, 60, 160, 100, "Distributed\n(private RAM + network)", "#6366f1")
        + _rect(50, 90, 120, 40, "CPU1 CPU2", "#14b8a6")
        + _rect(250, 85, 50, 35, "P0", "#38bdf8")
        + _rect(320, 85, 50, 35, "P1", "#38bdf8")
        + _arrow(300, 102, 320, 102)
        + '<text x="30" y="40" fill="#0f172a" font-size="13" font-weight="700">Shared vs Distributed Memory</text>'
    )
    return _svg(c, 430, 190, compact)


def vis_load_balance(compact=False):
    c = (
        _defs()
        + _rect(30, 50, 80, 120, "Worker 1\n2 tasks", "#0d9488")
        + _rect(130, 50, 80, 120, "Worker 2\n2 tasks", "#0d9488")
        + _rect(230, 50, 80, 120, "Worker 3\n2 tasks", "#0d9488")
        + '<text x="30" y="30" fill="#0f172a" font-size="13" font-weight="700">Load Balancing — Equal work per processor</text>'
        + '<text x="30" y="195" fill="#64748b" font-size="11">Redistribute tasks so no core sits idle</text>'
    )
    return _svg(c, 360, 210, compact)


def vis_mutex_semaphore(compact=False):
    c = (
        _defs()
        + _rect(40, 60, 150, 50, "Mutex (1 key)\nOne at a time", "#ef4444")
        + _rect(230, 60, 150, 50, "Semaphore (N keys)\nUp to N allowed", "#0d9488")
        + '<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">Mutex vs Semaphore</text>'
        + '<text x="40" y="140" fill="#64748b" font-size="11">Mutex=binary lock | Semaphore=counting (e.g. 3 parking slots)</text>'
    )
    return _svg(c, 430, 170, compact)


def vis_radix_sort(compact=False):
    c = (
        _defs()
        + '<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">Radix Sort — Sort by digits/characters</text>'
        + '<text x="40" y="70" fill="#64748b" font-size="11">Pass 1 (ones): 170, 90, 802, 24, 2, 66, 45</text>'
        + "".join(_rect(40 + i * 45, 90, 38, 35, v, "#38bdf8") for i, v in enumerate(["170", "90", "802", "24", "2", "66", "45"]))
        + '<text x="40" y="150" fill="#64748b" font-size="11">Pass 2 (tens) → Pass 3 (hundreds) → sorted</text>'
        + "".join(_rect(40 + i * 45, 165, 38, 35, v, "#0d9488") for i, v in enumerate(["2", "24", "45", "66", "90", "170", "802"]))
    )
    return _svg(c, 400, 220, compact)


def vis_workflow(compact=False):
    c = (
        _defs()
        + _rect(30, 90, 70, 40, "Start", "#0d9488")
        + _arrow(100, 110, 130, 110)
        + _rect(135, 90, 80, 40, "Read Excel", "#38bdf8")
        + _arrow(215, 110, 245, 110)
        + _rect(250, 90, 80, 40, "If/Else", "#6366f1")
        + _arrow(330, 110, 360, 110)
        + _rect(365, 90, 70, 40, "Email", "#f59e0b")
        + '<text x="30" y="40" fill="#0f172a" font-size="13" font-weight="700">Workflow Designer — Bot flow visually</text>'
    )
    return _svg(c, 460, 170, compact)


def vis_generic_concept(title: str, subtitle: str, compact=False):
    c = (
        _defs()
        + _rect(60, 70, 100, 50, "Input", "#0d9488")
        + _arrow(160, 95, 200, 95)
        + _rect(205, 70, 100, 50, "Process", "#1e293b")
        + _arrow(305, 95, 345, 95)
        + _rect(350, 70, 100, 50, "Output", "#f59e0b")
        + f'<text x="40" y="40" fill="#0f172a" font-size="13" font-weight="700">{title}</text>'
        + f'<text x="40" y="160" fill="#64748b" font-size="11">{subtitle}</text>'
    )
    return _svg(c, 480, 190, compact)


# ---- Matching: question id or keywords → visual builder ----

def _kw(text: str, *words) -> bool:
    t = text.lower()
    return all(w.lower() in t for w in words)


VISUAL_BY_ID = {
    "AA-U1-S01": vis_bfs,
    "AA-U1-L02": lambda c=False: vis_bfs(c) + vis_dfs(c),
    "PC-U5-L04": vis_bfs,
    "AA-U1-S05": vis_dfs,
    "AA-U1-S02": vis_dijkstra, "AA-U1-L04": vis_dijkstra, "PC-U5-L02": vis_dijkstra, "PC-U5-S04": vis_dijkstra,
    "AA-U1-L05": vis_mst, "AA-U2-L01": vis_mst, "AA-U2-S04": vis_mst, "PC-U5-L01": vis_mst, "PC-U5-S02": vis_mst,
    "AA-U1-L01": vis_sorting, "PC-U4-L03": vis_sorting,
    "AA-U1-L03": vis_toposort, "AA-U2-L04": vis_toposort,
    "AA-U2-L03": vis_graph_colouring,
    "AA-U3-L02": vis_maxflow, "AA-U3-L04": vis_maxflow, "AA-U3-L05": vis_maxflow, "AA-U3-L06": vis_maxflow,
    "AA-U3-S03": vis_maxflow, "AA-U3-S05": vis_maxflow,
    "AA-U4-L04": vis_fft, "AA-U4-S05": vis_fft,
    "AA-U5-S03": vis_np, "AA-U5-L01": vis_np, "AA-U5-L03": vis_np,
    "AA-U3-L01": vis_matrix_mult, "AA-U3-L03": vis_matrix_mult, "PC-U4-L01": vis_matrix_mult, "PC-U4-L02": vis_matrix_mult,
    "ACA-U1-S01": vis_parallelism, "ACA-U1-L01": vis_parallelism, "PC-U1-S01": vis_parallelism, "PC-U1-L05": vis_parallelism,
    "ACA-U1-S04": vis_flynn, "ACA-U1-L03": vis_flynn, "PC-U1-S02": vis_flynn, "PC-U1-L02": vis_flynn,
    "ACA-U2-S01": vis_amdahl, "ACA-U2-L01": vis_amdahl, "PC-U2-S02": vis_amdahl, "PC-U2-L05": vis_amdahl,
    "ACA-U2-S04": vis_memory_hierarchy, "ACA-U2-L02": vis_memory_hierarchy,
    "ACA-U3-S03": vis_pipeline, "ACA-U3-L01": vis_pipeline, "ACA-U3-L02": vis_pipeline, "ACA-U3-L03": vis_pipeline, "ACA-U3-L04": vis_pipeline,
    "ACA-U4-S01": vis_cache_coherence, "ACA-U4-L01": vis_cache_coherence,
    "ACA-U1-S03": vis_shared_vs_distributed, "ACA-U4-L05": vis_shared_vs_distributed, "PC-U1-S03": vis_shared_vs_distributed, "PC-U1-L03": vis_shared_vs_distributed,
    "PC-U3-S01": vis_mpi, "PC-U3-L01": vis_mpi, "PC-U3-L03": vis_mpi, "PC-U1-L01": vis_mpi,
    "PC-U3-S04": vis_pthreads, "PC-U3-L02": vis_pthreads, "PC-U3-L04": vis_pthreads,
    "PC-U3-L05": vis_mutex_semaphore, "PC-U3-S05": vis_mutex_semaphore,
    "PC-U2-S01": vis_load_balance, "PC-U2-L03": vis_load_balance,
    "PC-U4-L05": vis_radix_sort, "PC-U4-S04": vis_radix_sort,
    "PC-U5-L03": vis_dfs, "PC-U5-L05": lambda c=False: vis_dfs(c) + vis_bfs(c),
    "RPA-U1-S01": vis_rpa_arch, "RPA-U1-L01": vis_rpa_arch, "RPA-U1-L04": vis_rpa_arch,
    "RPA-U2-S01": vis_control_room, "RPA-U2-L01": vis_control_room, "RPA-U2-L02": vis_control_room,
    "RPA-U2-L03": vis_control_room, "RPA-U2-L04": vis_control_room, "RPA-U2-L05": vis_control_room,
    "RPA-U3-S02": vis_device_pool, "RPA-U3-L01": vis_device_pool, "RPA-U3-L05": vis_device_pool,
    "RPA-U4-S01": vis_recorders, "RPA-U4-L01": vis_recorders, "RPA-U4-L05": vis_recorders,
    "RPA-U5-S05": vis_workflow, "RPA-U5-L03": vis_workflow, "RPA-U5-L04": vis_workflow,
}

# Keyword rules: (keywords, builder) — checked in order
VISUAL_RULES = [
    (("bfs",), vis_bfs),
    (("dfs",), vis_dfs),
    (("dijkstra",), vis_dijkstra),
    (("mst",), vis_mst),
    (("kruskal",), vis_mst),
    (("prim",), vis_mst),
    (("spanning",), vis_mst),
    (("sort",), vis_sorting),
    (("topological",), vis_toposort),
    (("dag",), vis_toposort),
    (("colour",), vis_graph_colouring),
    (("color",), vis_graph_colouring),
    (("chromatic",), vis_graph_colouring),
    (("flow",), vis_maxflow),
    (("fulkerson",), vis_maxflow),
    (("matching",), vis_maxflow),
    (("residual",), vis_maxflow),
    (("floyd",), vis_dijkstra),
    (("warshall",), vis_dfs),
    (("fft",), vis_fft),
    (("dft",), vis_fft),
    (("polynomial",), vis_fft),
    (("matrix",), vis_matrix_mult),
    (("lup",), vis_matrix_mult),
    (("strassen",), vis_matrix_mult),
    (("np",), vis_np),
    (("simplex",), vis_generic_concept),
    (("random",), vis_generic_concept),
    (("pipeline",), vis_pipeline),
    (("superscalar",), vis_pipeline),
    (("hazard",), vis_pipeline),
    (("memory hierarchy",), vis_memory_hierarchy),
    (("cache",), vis_cache_coherence),
    (("coherence",), vis_cache_coherence),
    (("amdahl",), vis_amdahl),
    (("gustafson",), vis_amdahl),
    (("flynn",), vis_flynn),
    (("simd",), vis_flynn),
    (("vector",), vis_parallelism),
    (("parallel",), vis_parallelism),
    (("pram",), vis_parallelism),
    (("interconnect",), vis_mpi),
    (("multiprocessor",), vis_shared_vs_distributed),
    (("multicomputer",), vis_shared_vs_distributed),
    (("shared", "memory"), vis_shared_vs_distributed),
    (("distributed",), vis_shared_vs_distributed),
    (("mpi",), vis_mpi),
    (("message",), vis_mpi),
    (("broadcast",), vis_mpi),
    (("pthread",), vis_pthreads),
    (("thread",), vis_pthreads),
    (("mutex",), vis_mutex_semaphore),
    (("semaphore",), vis_mutex_semaphore),
    (("deadlock",), vis_mutex_semaphore),
    (("critical section",), vis_mutex_semaphore),
    (("load balanc",), vis_load_balance),
    (("decompos",), vis_load_balance),
    (("radix",), vis_radix_sort),
    (("bucket",), vis_radix_sort),
    (("rpa",), vis_rpa_arch),
    (("bot",), vis_rpa_arch),
    (("automation anywhere",), vis_rpa_arch),
    (("control room",), vis_control_room),
    (("dashboard",), vis_control_room),
    (("activity",), vis_control_room),
    (("audit",), vis_control_room),
    (("device",), vis_device_pool),
    (("workload",), vis_device_pool),
    (("sla",), vis_device_pool),
    (("recorder",), vis_recorders),
    (("excel",), vis_recorders),
    (("task editor",), vis_recorders),
    (("workflow",), vis_workflow),
    (("object cloning",), vis_workflow),
    (("ftp",), vis_workflow),
    (("terminal",), vis_workflow),
    (("consistency",), vis_cache_coherence),
    (("synchron",), vis_pthreads),
    (("latency",), vis_mpi),
    (("bandwidth",), vis_mpi),
    (("greedy",), vis_mst),
    (("matroid",), vis_mst),
    (("augmenting",), vis_maxflow),
    (("amortized",), vis_sorting),
    (("strongly connected",), vis_dfs),
    (("scc",), vis_dfs),
]


def attach_visual(q: dict) -> dict:
    """Add visual SVG example to question dict."""
    if q.get("visual"):
        return q
    qid = q.get("id", "")
    compact = q.get("type") == "short"
    text = q.get("question", "")

    builder = VISUAL_BY_ID.get(qid)
    if builder:
        if callable(builder):
            visual = builder(compact)
        else:
            visual = builder
        return {**q, "visual": visual}

    for keywords, fn in VISUAL_RULES:
        if _kw(text, *keywords):
            if fn is vis_generic_concept:
                topic = text.replace("Explain", "").replace("Define", "").strip()[:50]
                visual = vis_generic_concept(topic, "Input → Process → Output flow", compact)
            else:
                visual = fn(compact)
            return {**q, "visual": visual}

    # Subject fallback
    tags = " ".join(q.get("tags", [])) if isinstance(q.get("tags"), list) else str(q.get("tags", ""))
    unit = q.get("unit", "")
    if "algorithm" in tags or unit.startswith("Unit-1") and "AA" in qid:
        visual = vis_generic_concept("Algorithm Concept", "Input → Steps → Correct Output", compact)
    elif "ACA" in qid or "architecture" in tags:
        visual = vis_pipeline(compact) if "Unit-3" in unit else vis_parallelism(compact)
    elif "PC" in qid:
        visual = vis_mpi(compact)
    elif "RPA" in qid:
        visual = vis_rpa_arch(compact)
    else:
        visual = vis_generic_concept("Exam Concept", "Define → Explain → Example → Complexity", compact)

    return {**q, "visual": visual}
