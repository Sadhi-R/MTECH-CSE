"""Full question-bank dataset for M.Tech CSE Sem-2 (VR25)."""

SEMESTER = ""


def _long_question(
    qid,
    title,
    question,
    unit,
    tags,
    weight,
    asked,
    confidence,
    definition,
    introduction,
    why,
    working,
    steps,
    diagram,
    algorithm,
    flowchart,
    example,
    advantages,
    disadvantages,
    applications,
    exam_tips,
    mistakes,
    comparison,
    time,
    space,
    interview,
    memory,
    mark5,
    mark10,
    one_liner,
):
    return {
        "id": qid,
        "title": title,
        "question": question,
        "type": "long",
        "unit": unit,
        "tags": tags,
        "weight": weight,
        "asked": asked,
        "confidence": confidence,
        "definition": definition,
        "introduction": introduction,
        "why": why,
        "working": working,
        "steps": steps,
        "diagram": diagram,
        "algorithm": algorithm,
        "flowchart": flowchart,
        "example": example,
        "advantages": advantages,
        "disadvantages": disadvantages,
        "applications": applications,
        "exam_tips": exam_tips,
        "mistakes": mistakes,
        "comparison": comparison,
        "time": time,
        "space": space,
        "interview": interview,
        "memory": memory,
        "mark5": mark5,
        "mark10": mark10,
        "semester": SEMESTER,
        "one_liner": one_liner,
    }


def _short_question(
    qid,
    title,
    question,
    unit,
    tags,
    weight,
    asked,
    confidence,
    definition,
    key_points,
    example,
    exam_keyword,
    one_liner,
):
    return {
        "id": qid,
        "title": title,
        "question": question,
        "type": "short",
        "unit": unit,
        "tags": tags,
        "weight": weight,
        "asked": asked,
        "confidence": confidence,
        "definition": definition,
        "key_points": key_points,
        "example": example,
        "exam_keyword": exam_keyword,
        "one_liner": one_liner,
    }


def _auto_long(qid, question, unit, tags, weight):
    title = question[:72]
    topic = question.replace("Explain", "").replace("Describe", "").strip().rstrip(".")
    return _long_question(
        qid=qid,
        title=title,
        question=question,
        unit=unit,
        tags=tags,
        weight=weight,
        asked="Question Bank",
        confidence="90%",
        definition=f"{topic} is an exam-focused concept from {unit} that should be explained in simple terms first.",
        introduction=f"This answer introduces {topic} from beginner level and then builds the exam-ready structure.",
        why=f"{topic} is important because it is repeated in internal and semester papers and connects theory with practical problem solving.",
        working=f"The working idea of {topic} can be understood by defining inputs, applying core rules, and validating output with one clear example.",
        steps=[
            f"Define {topic} in one or two lines.",
            "List assumptions and required inputs.",
            "Explain the logic in ordered steps.",
            "Show one dry run with simple values.",
            "Conclude with complexity and use-cases.",
        ],
        diagram=(
            "+---------------------------+\n"
            "| Input / Given Problem     |\n"
            "+------------+--------------+\n"
            "             |\n"
            "             v\n"
            "+---------------------------+\n"
            f"| Core Logic: {unit}        |\n"
            "+------------+--------------+\n"
            "             |\n"
            "             v\n"
            "+---------------------------+\n"
            "| Output / Interpretation   |\n"
            "+---------------------------+"
        ),
        algorithm=(
            "1. Read problem statement and constraints.\n"
            "2. Initialize data structures needed for the method.\n"
            "3. Apply the core rule repeatedly until termination.\n"
            "4. Track intermediate state for explanation.\n"
            "5. Return final result and verify correctness."
        ),
        flowchart="Start -> Define -> Process -> Validate -> Conclude -> End",
        example=f"Real-life example: A logistics team applies {topic} to plan routes/resources with lower time and cost.",
        advantages=[
            "Easy to explain in structured exam format.",
            "Connects with algorithmic thinking and implementation.",
            "Supports scoring in both 5-mark and 10-mark questions.",
        ],
        disadvantages=[
            "Can feel abstract without a worked example.",
            "Incorrect assumptions lead to wrong final answer.",
        ],
        applications=[
            "Academic problem solving",
            "Software and systems design",
            "Interview and competitive programming preparation",
        ],
        exam_tips="Write definition first, then steps, then one example, then time/space; this order gets consistent marks.",
        mistakes="Students often skip assumptions, miss edge cases, or forget to conclude with complexity.",
        comparison="Compare with a nearby method by approach, correctness condition, and complexity to show depth.",
        time="Depends on method and input size; write the standard asymptotic bound for the asked technique.",
        space="Mention both auxiliary memory and dominant data structures used during execution.",
        interview=f"Interview angle: explain {topic} with one dry run, then discuss trade-offs and limitations.",
        memory=f"Memory trick: Remember {topic} as Define -> Steps -> Example -> Complexity.",
        mark5=f"5-mark: define {topic}, write 3-5 clear steps, and add one compact example.",
        mark10=f"10-mark: write definition, detailed working, algorithm, diagram/flow, example, comparison, and complexity.",
        one_liner=f"{topic} is best answered using definition, steps, and one practical example.",
    )


def _auto_short(qid, question, unit, tags, weight):
    title = question[:72]
    return _short_question(
        qid=qid,
        title=title,
        question=question,
        unit=unit,
        tags=tags,
        weight=weight,
        asked="Question Bank",
        confidence="90%",
        definition=f"{question.rstrip('.')} is a core short-answer concept from {unit}.",
        key_points=[
            "Start with a one-line definition.",
            "State the core property or rule asked in the question.",
            "Add one exam-oriented keyword or contrast point.",
        ],
        example=f"Quick example: {question.rstrip('.')} in a small classroom/real-world scenario.",
        exam_keyword="Definition + Property + Example",
        one_liner=f"{question.rstrip('.')} should be answered in 4-6 crisp lines.",
    )


AA_SHORT = {
    "Unit-1": [
        "Why does BFS give shortest path in an unweighted graph?",
        "Why is Dijkstra not suitable for negative edge weights?",
        "What is a Strongly Connected Component (SCC)?",
        "Differentiate amortized analysis and worst-case analysis.",
        "What is the time complexity of DFS?",
    ],
    "Unit-2": [
        "List shortest path algorithms and when to use each.",
        "Define matroids and explain greedy connection.",
        "Explain amortized analysis with one example.",
        "Write applications of spanning trees.",
        "What is an augmenting path?",
    ],
    "Unit-3": [
        "Write time relations among matrix operations.",
        "Compare matrix multiplication complexities.",
        "Differentiate max-flow and min-cut.",
        "What is Strassen's algorithm?",
        "Define residual graph.",
    ],
    "Unit-4": [
        "What is Floyd-Warshall algorithm?",
        "What is dynamic programming?",
        "State Chinese Remainder Theorem.",
        "Differentiate base representation and modulo representation.",
        "What is DFT?",
    ],
    "Unit-5": [
        "What is feasible region in linear programming?",
        "What is Simplex algorithm used for?",
        "Define NP-completeness.",
        "Mention recent trends in data structures.",
        "What is polynomial-space-bounded computation?",
    ],
}

AA_LONG = {
    "Unit-1": [
        "Compare five sorting algorithms.",
        "Explain BFS and DFS algorithms with examples.",
        "Explain DAG and topological sorting.",
        "Explain Dijkstra algorithm with steps and example.",
        "Compare MST algorithms (Kruskal vs Prim).",
    ],
    "Unit-2": [
        "Explain MST application with a real problem.",
        "Explain Warshall technique.",
        "Explain graph colouring.",
        "Compare chromatic number concept and DAG scheduling.",
        "Explain three applications of graph algorithms.",
    ],
    "Unit-3": [
        "Explain LUP decomposition.",
        "Explain Ford-Fulkerson and Edmonds-Karp.",
        "Explain divide-and-conquer matrix multiplication.",
        "Explain airline scheduling using flow networks.",
        "Explain preflow-push algorithm.",
        "Explain bipartite matching.",
    ],
    "Unit-4": [
        "Explain dynamic programming and Floyd-Warshall with limitations.",
        "Explain CRT and polynomial interpolation (parts a and b).",
        "Explain polynomial multiplication and division.",
        "Compare FFT and direct polynomial product.",
        "Explain Schonhage-Strassen multiplication.",
    ],
    "Unit-5": [
        "Define NP-complete and discuss limitations.",
        "Explain random dictionaries.",
        "Write NP-hardness proof strategy.",
        "Explain randomized algorithms.",
        "Compare randomized catching and Chernoff bounds.",
    ],
}

ACA_SHORT = {
    "Unit-1": [
        "Define parallelism.",
        "Explain PRAM model.",
        "Differentiate multiprocessor and multicomputer.",
        "State Flynn classification.",
        "Write conditions of parallelism.",
    ],
    "Unit-2": [
        "State Amdahl's law.",
        "State Gustafson's law.",
        "Differentiate superscalar and vector processors.",
        "Explain memory hierarchy.",
        "Define performance metrics in parallel systems.",
    ],
    "Unit-3": [
        "Define sequential consistency.",
        "Differentiate linear and non-linear pipeline.",
        "List pipeline stages.",
        "Define shared memory model.",
        "List pipeline hazards.",
    ],
    "Unit-4": [
        "Define cache coherence.",
        "List synchronization mechanisms.",
        "What is message passing?",
        "Write three generations of multicomputers.",
        "List multiprocessor interconnects.",
    ],
    "Unit-5": [
        "Define SIMD.",
        "Define vector processing.",
        "What is compound vector processing?",
        "Explain CM-5 in one note.",
        "Define multivector computer.",
    ],
}

ACA_LONG = {
    "Unit-1": [
        "Explain parallel computer models with diagrams.",
        "Compare SIMD and multivector computers.",
        "Explain Flynn's classification with examples.",
        "Explain interconnect architectures.",
        "Explain program partitioning and scheduling.",
    ],
    "Unit-2": [
        "Explain Amdahl and Gustafson laws with examples.",
        "Explain memory hierarchy and performance impact.",
        "Explain scalable performance in parallel systems.",
        "Compare superscalar and vector architectures.",
        "Explain advanced processor performance issues.",
    ],
    "Unit-3": [
        "Explain instruction pipeline design.",
        "Compare linear and non-linear pipelines.",
        "Explain superscalar pipeline design.",
        "Explain arithmetic pipeline.",
        "Explain memory consistency models.",
    ],
    "Unit-4": [
        "Explain cache coherence protocols.",
        "Explain multiprocessor interconnects in detail.",
        "Explain synchronization in shared memory systems.",
        "Explain SIMD architecture.",
        "Compare multiprocessor and multicomputer systems.",
    ],
    "Unit-5": [
        "Explain vector processing principles.",
        "Explain SIMD organizations.",
        "Explain CM-5 architecture.",
        "Compare scalar and vector processing.",
        "Explain compound vector processing.",
    ],
}

PC_SHORT = {
    "Unit-1": [
        "Define parallel computing.",
        "State Flynn classification.",
        "Differentiate shared and distributed memory.",
        "Define SIMD and MIMD.",
        "Differentiate latency and bandwidth.",
    ],
    "Unit-2": [
        "Define load balancing.",
        "State Amdahl's law.",
        "State Gustafson's law.",
        "Define concurrency.",
        "Define task scheduling.",
    ],
    "Unit-3": [
        "Define MPI.",
        "What is deadlock?",
        "Define thread.",
        "Define mutex.",
        "Define critical section.",
    ],
    "Unit-4": [
        "Define dense matrix.",
        "What is pivot element?",
        "Define bucket sort.",
        "Define radix sort.",
        "What is divide-and-conquer?",
    ],
    "Unit-5": [
        "Define weighted graph.",
        "Define MST.",
        "State Prim algorithm idea.",
        "State Dijkstra algorithm idea.",
        "What is greedy strategy?",
    ],
}

PC_LONG = {
    "Unit-1": [
        "Explain basic communication operations.",
        "Explain Flynn's classification in parallel computing.",
        "Explain shared versus distributed memory architecture.",
        "Explain parallel programming platforms.",
        "Explain motivation and scope of parallel computing.",
    ],
    "Unit-2": [
        "Explain parallel algorithm design.",
        "Explain decomposition strategies.",
        "Explain load balancing techniques.",
        "Explain analytical modeling of parallel programs.",
        "Explain Amdahl and Gustafson laws with examples.",
    ],
    "Unit-3": [
        "Explain MPI functions with examples.",
        "Explain PThreads synchronization mechanisms.",
        "Explain MPI architecture.",
        "Explain thread creation and lifecycle.",
        "Compare mutex and semaphore.",
    ],
    "Unit-4": [
        "Explain parallel matrix-vector multiplication.",
        "Explain parallel matrix-matrix multiplication.",
        "Explain parallel bubble and quick sort.",
        "Explain bucket and enumeration sort.",
        "Explain radix sort.",
    ],
    "Unit-5": [
        "Explain Prim algorithm with example.",
        "Explain Dijkstra algorithm with example.",
        "Explain DFS algorithm.",
        "Explain BFS algorithm.",
        "Compare DFS and BFS.",
    ],
}

RPA_SHORT = {
    "Unit-1": [
        "Define RPA.",
        "List common RPA use cases.",
        "What is Automation Anywhere platform?",
        "List bot creation methods.",
        "Differentiate attended and unattended bots.",
    ],
    "Unit-2": [
        "Define Web Control Room.",
        "Write dashboard panel features.",
        "What is activity panel?",
        "What is bots panel?",
        "What are bot credentials?",
    ],
    "Unit-3": [
        "Differentiate development and runtime client.",
        "What is device pool?",
        "What is SLA calculator?",
        "What is audit log?",
        "List user roles in Control Room.",
    ],
    "Unit-4": [
        "Differentiate smart, web, and screen recorder.",
        "Explain loop command.",
        "What is command library?",
        "What is task editor?",
        "Explain database command.",
    ],
    "Unit-5": [
        "What is terminal emulator command?",
        "Explain PDF integration command.",
        "What is object cloning?",
        "List FTP command use cases.",
        "What is workflow designer?",
    ],
}

RPA_LONG = {
    "Unit-1": [
        "Explain RPA concepts and use cases.",
        "Explain Automation Anywhere advanced features.",
        "Explain bot creation methods.",
        "Explain benefits and limitations of RPA.",
        "Evaluate RPA for enterprise adoption.",
    ],
    "Unit-2": [
        "Explain Web Control Room architecture.",
        "Explain dashboard panel features.",
        "Explain activity and bots management.",
        "Explain enterprise role of Web Control Room.",
        "Explain Control Room panel functions.",
    ],
    "Unit-3": [
        "Explain device management and workload distribution.",
        "Explain relevance of audit log.",
        "Explain administration capabilities.",
        "Explain API exposure in Control Room.",
        "Explain workload distribution with SLA planning.",
    ],
    "Unit-4": [
        "Explain bot creation using recorders.",
        "Explain Excel, String, and XML commands.",
        "Explain task editor customization.",
        "Explain three-command enterprise use case.",
        "Compare recorders in Automation Anywhere.",
    ],
    "Unit-5": [
        "Explain object cloning and error handling.",
        "Explain FTP, PGP, and terminal commands.",
        "Explain workflow and report designers.",
        "Explain end-to-end automation scenario.",
        "Explain advanced command examples.",
    ],
}


FREQUENT_HIGH = {
    "BFS",
    "DFS",
    "Dijkstra",
    "Topological",
    "MST",
    "Ford-Fulkerson",
    "Edmonds-Karp",
    "Floyd-Warshall",
    "NP",
    "Amdahl",
    "Gustafson",
    "Pipeline",
    "Cache coherence",
    "MPI",
    "PThreads",
    "Load balancing",
    "Web Control Room",
    "Automation Anywhere",
    "RPA",
    "Device",
    "Workload",
}


def _weight_for(question):
    for token in FREQUENT_HIGH:
        if token.lower() in question.lower():
            return "high"
    return "medium"


def _build_subject(prefix, short_map, long_map, tag):
    rows = []
    for unit_no, unit in enumerate(["Unit-1", "Unit-2", "Unit-3", "Unit-4", "Unit-5"], start=1):
        for i, q in enumerate(short_map[unit], start=1):
            qid = f"{prefix}-U{unit_no}-S{i:02d}"
            rows.append(_auto_short(qid, q, unit, [tag, "question-bank", "short"], _weight_for(q)))
        for i, q in enumerate(long_map[unit], start=1):
            qid = f"{prefix}-U{unit_no}-L{i:02d}"
            rows.append(_auto_long(qid, q, unit, [tag, "question-bank", "long"], _weight_for(q)))
    return rows


QUESTIONS = {
    "advanced-algorithms": _build_subject("AA", AA_SHORT, AA_LONG, "advanced-algorithms"),
    "advanced-computer-architecture": _build_subject("ACA", ACA_SHORT, ACA_LONG, "advanced-computer-architecture"),
    "parallel-computing": _build_subject("PC", PC_SHORT, PC_LONG, "parallel-computing"),
    "robotic-process-automation": _build_subject("RPA", RPA_SHORT, RPA_LONG, "robotic-process-automation"),
}


UNITS = {
    "advanced-algorithms": [
        {
            "unit": "Unit-1",
            "title": "Sorting and Graph Foundations",
            "topics": ["BFS", "DFS", "Dijkstra", "SCC", "Topological sort", "Amortized analysis"],
            "must_read": ["AA-U1-S01", "AA-U1-L02", "AA-U1-L04"],
            "expected_short": ["AA-U1-S01", "AA-U1-S02", "AA-U1-S05"],
            "expected_long": ["AA-U1-L02", "AA-U1-L03", "AA-U1-L04"],
        },
        {
            "unit": "Unit-2",
            "title": "Matroids and Matching",
            "topics": ["Matroids", "Greedy paradigm", "MST applications", "Warshall", "Graph colouring"],
            "must_read": ["AA-U2-S02", "AA-U2-L01", "AA-U2-L02"],
            "expected_short": ["AA-U2-S01", "AA-U2-S02", "AA-U2-S05"],
            "expected_long": ["AA-U2-L01", "AA-U2-L02", "AA-U2-L03"],
        },
        {
            "unit": "Unit-3",
            "title": "Flow and Matrix Computation",
            "topics": ["LUP", "Ford-Fulkerson", "Edmonds-Karp", "Preflow-push", "Bipartite matching"],
            "must_read": ["AA-U3-S03", "AA-U3-L02", "AA-U3-L06"],
            "expected_short": ["AA-U3-S03", "AA-U3-S04", "AA-U3-S05"],
            "expected_long": ["AA-U3-L01", "AA-U3-L02", "AA-U3-L06"],
        },
        {
            "unit": "Unit-4",
            "title": "DP, CRT, and FFT",
            "topics": ["Floyd-Warshall", "Dynamic programming", "CRT", "DFT/FFT", "Polynomial operations"],
            "must_read": ["AA-U4-S01", "AA-U4-L01", "AA-U4-L04"],
            "expected_short": ["AA-U4-S01", "AA-U4-S02", "AA-U4-S03"],
            "expected_long": ["AA-U4-L01", "AA-U4-L02", "AA-U4-L04"],
        },
        {
            "unit": "Unit-5",
            "title": "LP and Complexity",
            "topics": ["Simplex", "NP-complete", "NP-hard", "Randomized algorithms", "Chernoff bounds"],
            "must_read": ["AA-U5-S03", "AA-U5-L01", "AA-U5-L03"],
            "expected_short": ["AA-U5-S01", "AA-U5-S03", "AA-U5-S05"],
            "expected_long": ["AA-U5-L01", "AA-U5-L03", "AA-U5-L04"],
        },
    ],
    "advanced-computer-architecture": [
        {
            "unit": "Unit-1",
            "title": "Theory of Parallelism",
            "topics": ["Parallel models", "PRAM", "Flynn taxonomy", "Interconnects", "Partitioning"],
            "must_read": ["ACA-U1-S02", "ACA-U1-L01", "ACA-U1-L03"],
            "expected_short": ["ACA-U1-S01", "ACA-U1-S02", "ACA-U1-S03"],
            "expected_long": ["ACA-U1-L01", "ACA-U1-L02", "ACA-U1-L03"],
        },
        {
            "unit": "Unit-2",
            "title": "Scalable Performance",
            "topics": ["Amdahl", "Gustafson", "Memory hierarchy", "Superscalar", "Metrics"],
            "must_read": ["ACA-U2-S01", "ACA-U2-L01", "ACA-U2-L02"],
            "expected_short": ["ACA-U2-S01", "ACA-U2-S02", "ACA-U2-S04"],
            "expected_long": ["ACA-U2-L01", "ACA-U2-L02", "ACA-U2-L03"],
        },
        {
            "unit": "Unit-3",
            "title": "Pipelining and Consistency",
            "topics": ["Instruction pipeline", "Hazards", "Shared memory", "Consistency"],
            "must_read": ["ACA-U3-S03", "ACA-U3-L01", "ACA-U3-L05"],
            "expected_short": ["ACA-U3-S01", "ACA-U3-S03", "ACA-U3-S05"],
            "expected_long": ["ACA-U3-L01", "ACA-U3-L03", "ACA-U3-L05"],
        },
        {
            "unit": "Unit-4",
            "title": "Parallel Architectures",
            "topics": ["Cache coherence", "Synchronization", "Interconnects", "SIMD"],
            "must_read": ["ACA-U4-S01", "ACA-U4-L01", "ACA-U4-L02"],
            "expected_short": ["ACA-U4-S01", "ACA-U4-S02", "ACA-U4-S05"],
            "expected_long": ["ACA-U4-L01", "ACA-U4-L03", "ACA-U4-L04"],
        },
        {
            "unit": "Unit-5",
            "title": "Vector and SIMD Processing",
            "topics": ["SIMD", "Vector processing", "CM-5", "Multivector"],
            "must_read": ["ACA-U5-S01", "ACA-U5-L01", "ACA-U5-L02"],
            "expected_short": ["ACA-U5-S01", "ACA-U5-S02", "ACA-U5-S05"],
            "expected_long": ["ACA-U5-L01", "ACA-U5-L02", "ACA-U5-L03"],
        },
    ],
    "parallel-computing": [
        {
            "unit": "Unit-1",
            "title": "Foundations of Parallel Computing",
            "topics": ["Communication ops", "Flynn", "Memory models", "Platforms"],
            "must_read": ["PC-U1-S01", "PC-U1-L01", "PC-U1-L04"],
            "expected_short": ["PC-U1-S01", "PC-U1-S02", "PC-U1-S03"],
            "expected_long": ["PC-U1-L01", "PC-U1-L03", "PC-U1-L04"],
        },
        {
            "unit": "Unit-2",
            "title": "Design and Modeling",
            "topics": ["Decomposition", "Load balancing", "Amdahl", "Gustafson", "Modeling"],
            "must_read": ["PC-U2-S01", "PC-U2-L03", "PC-U2-L05"],
            "expected_short": ["PC-U2-S01", "PC-U2-S02", "PC-U2-S05"],
            "expected_long": ["PC-U2-L01", "PC-U2-L03", "PC-U2-L05"],
        },
        {
            "unit": "Unit-3",
            "title": "MPI and PThreads",
            "topics": ["MPI", "Threads", "Mutex", "Critical section", "Synchronization"],
            "must_read": ["PC-U3-S01", "PC-U3-L01", "PC-U3-L02"],
            "expected_short": ["PC-U3-S01", "PC-U3-S04", "PC-U3-S05"],
            "expected_long": ["PC-U3-L01", "PC-U3-L02", "PC-U3-L05"],
        },
        {
            "unit": "Unit-4",
            "title": "Matrix and Sorting Algorithms",
            "topics": ["Matrix-vector", "Matrix-matrix", "Bucket", "Enumeration", "Radix"],
            "must_read": ["PC-U4-S03", "PC-U4-L01", "PC-U4-L05"],
            "expected_short": ["PC-U4-S02", "PC-U4-S03", "PC-U4-S04"],
            "expected_long": ["PC-U4-L01", "PC-U4-L03", "PC-U4-L05"],
        },
        {
            "unit": "Unit-5",
            "title": "Graph and Search Algorithms",
            "topics": ["Prim", "Dijkstra", "DFS", "BFS", "Greedy"],
            "must_read": ["PC-U5-S03", "PC-U5-L01", "PC-U5-L05"],
            "expected_short": ["PC-U5-S02", "PC-U5-S03", "PC-U5-S04"],
            "expected_long": ["PC-U5-L01", "PC-U5-L02", "PC-U5-L05"],
        },
    ],
    "robotic-process-automation": [
        {
            "unit": "Unit-1",
            "title": "RPA Foundations",
            "topics": ["RPA basics", "Use cases", "AA platform", "Bot types"],
            "must_read": ["RPA-U1-S01", "RPA-U1-L01", "RPA-U1-L04"],
            "expected_short": ["RPA-U1-S01", "RPA-U1-S03", "RPA-U1-S05"],
            "expected_long": ["RPA-U1-L01", "RPA-U1-L02", "RPA-U1-L04"],
        },
        {
            "unit": "Unit-2",
            "title": "Web Control Room",
            "topics": ["Dashboard", "Activity panel", "Bots panel", "Credentials"],
            "must_read": ["RPA-U2-S01", "RPA-U2-L01", "RPA-U2-L05"],
            "expected_short": ["RPA-U2-S01", "RPA-U2-S02", "RPA-U2-S03"],
            "expected_long": ["RPA-U2-L01", "RPA-U2-L03", "RPA-U2-L05"],
        },
        {
            "unit": "Unit-3",
            "title": "Devices, Workload, Audit",
            "topics": ["Device pools", "SLA", "Audit log", "Administration"],
            "must_read": ["RPA-U3-S02", "RPA-U3-L01", "RPA-U3-L05"],
            "expected_short": ["RPA-U3-S02", "RPA-U3-S03", "RPA-U3-S04"],
            "expected_long": ["RPA-U3-L01", "RPA-U3-L02", "RPA-U3-L05"],
        },
        {
            "unit": "Unit-4",
            "title": "Recorders and Commands",
            "topics": ["Smart/Web/Screen recorder", "Task editor", "Excel/DB/XML commands"],
            "must_read": ["RPA-U4-S01", "RPA-U4-L01", "RPA-U4-L05"],
            "expected_short": ["RPA-U4-S01", "RPA-U4-S02", "RPA-U4-S04"],
            "expected_long": ["RPA-U4-L01", "RPA-U4-L02", "RPA-U4-L05"],
        },
        {
            "unit": "Unit-5",
            "title": "Advanced RPA Design",
            "topics": ["Terminal", "PDF/FTP/PGP", "Object cloning", "Workflow designer"],
            "must_read": ["RPA-U5-S03", "RPA-U5-L01", "RPA-U5-L03"],
            "expected_short": ["RPA-U5-S01", "RPA-U5-S03", "RPA-U5-S05"],
            "expected_long": ["RPA-U5-L01", "RPA-U5-L03", "RPA-U5-L04"],
        },
    ],
}


EXPECTED = {
    "advanced-algorithms": {
        "top10": [
            "AA-U1-L02",
            "AA-U1-L04",
            "AA-U1-L05",
            "AA-U3-L02",
            "AA-U4-L01",
            "AA-U5-L01",
            "AA-U1-S01",
            "AA-U1-S02",
            "AA-U3-S03",
            "AA-U5-S03",
        ],
        "short5": ["AA-U1-S01", "AA-U1-S02", "AA-U2-S02", "AA-U3-S03", "AA-U5-S03"],
        "long5": ["AA-U1-L02", "AA-U1-L04", "AA-U3-L02", "AA-U4-L01", "AA-U5-L01"],
        "confidence_notes": [
            "Traversal, shortest path, and flow questions are highly repeated.",
            "Floyd-Warshall and NP-completeness are very likely long answers.",
            "Matroid-greedy and residual graph are frequent short answers.",
        ],
    },
    "advanced-computer-architecture": {
        "top10": [
            "ACA-U1-L01",
            "ACA-U1-L03",
            "ACA-U2-L01",
            "ACA-U2-L02",
            "ACA-U3-L01",
            "ACA-U4-L01",
            "ACA-U1-S02",
            "ACA-U2-S01",
            "ACA-U3-S05",
            "ACA-U5-S01",
        ],
        "short5": ["ACA-U1-S02", "ACA-U2-S01", "ACA-U2-S02", "ACA-U3-S05", "ACA-U4-S01"],
        "long5": ["ACA-U1-L01", "ACA-U2-L01", "ACA-U2-L02", "ACA-U3-L01", "ACA-U4-L01"],
        "confidence_notes": [
            "Parallel models and speedup laws remain high probability.",
            "Pipeline and cache coherence dominate descriptive papers.",
            "Vector/SIMD definitions appear repeatedly in short answers.",
        ],
    },
    "parallel-computing": {
        "top10": [
            "PC-U1-L01",
            "PC-U1-L03",
            "PC-U2-L03",
            "PC-U2-L05",
            "PC-U3-L01",
            "PC-U3-L02",
            "PC-U1-S03",
            "PC-U2-S01",
            "PC-U3-S04",
            "PC-U5-L05",
        ],
        "short5": ["PC-U1-S03", "PC-U2-S01", "PC-U2-S02", "PC-U3-S04", "PC-U5-S04"],
        "long5": ["PC-U1-L01", "PC-U2-L03", "PC-U3-L01", "PC-U3-L02", "PC-U5-L05"],
        "confidence_notes": [
            "Communication operations and load balancing are highly repeated.",
            "MPI/PThreads and synchronization are common long questions.",
            "DFS versus BFS is a recurring unit-V comparison.",
        ],
    },
    "robotic-process-automation": {
        "top10": [
            "RPA-U1-L01",
            "RPA-U1-L02",
            "RPA-U2-L01",
            "RPA-U2-L05",
            "RPA-U3-L01",
            "RPA-U4-L01",
            "RPA-U1-S01",
            "RPA-U1-S03",
            "RPA-U2-S01",
            "RPA-U3-S03",
        ],
        "short5": ["RPA-U1-S01", "RPA-U1-S03", "RPA-U2-S01", "RPA-U3-S03", "RPA-U4-S01"],
        "long5": ["RPA-U1-L01", "RPA-U1-L02", "RPA-U2-L01", "RPA-U3-L01", "RPA-U4-L01"],
        "confidence_notes": [
            "Web Control Room architecture and panel functions are repeated.",
            "RPA fundamentals and AA platform features are high probability.",
            "Device pools, workload, and SLA are common applied questions.",
        ],
    },
}


PAST_PAPERS = {
    "advanced-algorithms": {
        "mid1_descriptive": ["AA-U1-L02", "AA-U1-L03", "AA-U1-L04", "AA-U2-L01", "AA-U3-L02"],
        "mid1_mcq": ["AA-U1-S01", "AA-U1-S02", "AA-U1-S03", "AA-U1-S04", "AA-U2-S05"],
        "mid2_descriptive": ["AA-U3-L01", "AA-U4-L01", "AA-U4-L02", "AA-U5-L01", "AA-U5-L03"],
        "mid2_mcq": ["AA-U3-S01", "AA-U3-S04", "AA-U4-S01", "AA-U5-S03", "AA-U5-S05"],
    },
    "advanced-computer-architecture": {
        "mid1_descriptive": ["ACA-U1-L01", "ACA-U1-L02", "ACA-U2-L01", "ACA-U2-L02", "ACA-U3-L01"],
        "mid1_mcq": ["ACA-U1-S02", "ACA-U1-S04", "ACA-U2-S01", "ACA-U2-S03", "ACA-U2-S04"],
        "mid2_descriptive": ["ACA-U3-L01", "ACA-U3-L03", "ACA-U4-L01", "ACA-U5-L01", "ACA-U5-L02"],
        "mid2_mcq": ["ACA-U3-S02", "ACA-U3-S05", "ACA-U4-S01", "ACA-U5-S01", "ACA-U5-S05"],
    },
    "parallel-computing": {
        "mid1_descriptive": ["PC-U1-L01", "PC-U1-L03", "PC-U2-L03", "PC-U2-L05", "PC-U3-L01"],
        "mid1_mcq": ["PC-U1-S02", "PC-U1-S03", "PC-U2-S01", "PC-U2-S02", "PC-U3-S01"],
        "mid2_descriptive": ["PC-U3-L02", "PC-U4-L01", "PC-U4-L04", "PC-U5-L02", "PC-U5-L05"],
        "mid2_mcq": ["PC-U3-S04", "PC-U4-S03", "PC-U4-S04", "PC-U5-S03", "PC-U5-S04"],
    },
    "robotic-process-automation": {
        "mid1_descriptive": ["RPA-U1-L01", "RPA-U1-L02", "RPA-U2-L01", "RPA-U2-L04", "RPA-U3-L01"],
        "mid1_mcq": ["RPA-U1-S01", "RPA-U1-S03", "RPA-U2-S01", "RPA-U2-S03", "RPA-U3-S02"],
        "mid2_descriptive": ["RPA-U3-L02", "RPA-U4-L01", "RPA-U4-L05", "RPA-U5-L01", "RPA-U5-L03"],
        "mid2_mcq": ["RPA-U3-S03", "RPA-U3-S04", "RPA-U4-S01", "RPA-U5-S03", "RPA-U5-S05"],
    },
}
