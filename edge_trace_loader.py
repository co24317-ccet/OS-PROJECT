import pandas as pd

def load_vm_cpu_trace(path, max_rows=None):
    df = pd.read_csv(path)
    df = df.sort_values("report_ts")
    if max_rows:
        df = df.head(max_rows)
    return df

def convert_to_page_sequence(df, scale=10, max_pages=50):
    sequence = []
    for _, row in df.iterrows():
        vm_id = int(row["vm_id"]) % max_pages
        cpu = row.get("cpu_rate", 0.1)
        repeat = max(1, int(cpu * scale))
        sequence.extend([vm_id] * repeat)
    return sequence

def generate_edge_trace(file_path):
    df = load_vm_cpu_trace(file_path, max_rows=5000)
    return convert_to_page_sequence(df)
