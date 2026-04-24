def hit_ratio(faults, total):
    return (total - faults) / total if total else 0.0
