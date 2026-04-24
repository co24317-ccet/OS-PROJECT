def run(trace, algo_name, capacity, predictor=None):
    faults = 0
    history = []

    if algo_name == "FIFO":
        from algorithms.fifo import FIFO
        algo = FIFO(capacity)
    elif algo_name == "LRU":
        from algorithms.lru import LRU
        algo = LRU(capacity)
    else:
        from algorithms.ml_policy import MLPolicy
        algo = MLPolicy(capacity, predictor)

    steps = []

    for i, page in enumerate(trace):
        next_page = trace[i+1] if i+1 < len(trace) else None

        if algo_name == "ML-Based":
            fault = algo.access(history, page, next_page)
            frames = algo.frames
        else:
            fault = algo.access(page)
            frames = algo.frames

        if fault:
            faults += 1

        steps.append({
            "step": i+1,
            "page": page,
            "frames": frames.copy(),
            "fault": fault
        })
        history.append(page)

    return faults, steps
