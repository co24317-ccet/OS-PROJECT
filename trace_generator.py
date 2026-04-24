import random

def generate_trace(length=20, max_page=10, locality=True):
    trace = []
    if not locality:
        return [random.randint(0, max_page) for _ in range(length)]
    # simple locality: bursts around a working set
    ws = [random.randint(0, max_page) for _ in range(3)]
    for i in range(length):
        if random.random() < 0.7:
            trace.append(random.choice(ws))
        else:
            val = random.randint(0, max_page)
            trace.append(val)
            ws[random.randrange(len(ws))] = val
    return trace
