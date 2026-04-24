import streamlit as st
import time

from utils.trace_generator import generate_trace
from utils.edge_trace_loader import generate_edge_trace
from utils.metrics import hit_ratio
from simulator.controller import run
from ml.predictor import DummyMLPredictor

# ------------------ CONFIG ------------------
st.set_page_config(page_title="ML Page Replacement", layout="wide")
st.title("🧠 ML-Based Page Replacement Simulator")

# ------------------ SIDEBAR ------------------
st.sidebar.header("⚙️ Configuration")

# Trace source selector (FIXED)
trace_source = st.sidebar.selectbox(
    "Trace Source",
    ["Synthetic", "Edge Dataset"],
    key="trace_source"
)

# Common parameters
frames = st.sidebar.slider("Frame Size", 2, 10, 3, key="frames")
algo_choice = st.sidebar.selectbox(
    "Algorithm",
    ["FIFO", "LRU", "ML-Based"],
    key="algo"
)

# ------------------ TRACE HANDLING ------------------

# Synthetic controls
if trace_source == "Synthetic":
    trace_len = st.sidebar.slider("Trace Length", 10, 100, 25, key="trace_len")
    max_page = st.sidebar.slider("Max Page ID", 5, 50, 10, key="max_page")
    locality = st.sidebar.checkbox("Enable Locality", True, key="locality")

    if st.sidebar.button("Generate Trace", key="gen_trace"):
        st.session_state["trace"] = generate_trace(trace_len, max_page, locality)

# Edge dataset controls
elif trace_source == "Edge Dataset":
    uploaded_file = st.sidebar.file_uploader(
        "Upload VM_CPU.csv",
        type=["csv"],
        key="edge_upload"
    )

    if uploaded_file:
        st.session_state["trace"] = generate_edge_trace(uploaded_file)

# ------------------ INITIAL STATE ------------------
if "trace" not in st.session_state:
    st.session_state["trace"] = []

trace = st.session_state["trace"]

# ------------------ DISPLAY TRACE ------------------
st.subheader("📌 Reference String")

if trace:
    st.write(trace[:100])  # avoid huge dump
    st.caption(f"Length: {len(trace)}")
else:
    st.warning("No trace loaded. Generate or upload a dataset.")

# ------------------ RUN SIMULATION ------------------
if st.button("▶ Run Simulation", key="run_sim"):

    if not trace:
        st.error("Trace is empty. Please generate or upload data.")
        st.stop()

    predictor = DummyMLPredictor() if algo_choice == "ML-Based" else None

    faults, steps = run(trace, algo_choice, frames, predictor)
    hr = hit_ratio(faults, len(trace))

    # Metrics
    c1, c2, c3 = st.columns(3)
    c1.metric("Page Faults", faults)
    c2.metric("Hit Ratio", f"{hr:.2f}")
    c3.metric("Requests", len(trace))

    # Step-by-step visualization
    st.subheader("🧩 Step-by-Step Execution")

    box = st.empty()
    for s in steps[:100]:  # limit for performance
        box.markdown(
            f"**Step {s['step']}**  \n"
            f"Page: `{s['page']}`  \n"
            f"Frames: {s['frames']}  \n"
            f"{'❌ Fault' if s['fault'] else '✅ Hit'}"
        )
        time.sleep(0.05)

    # ML accuracy
    if algo_choice == "ML-Based" and predictor:
        acc = predictor.get_accuracy()
        st.subheader("🎯 ML Prediction Accuracy")
        st.metric("Accuracy", f"{acc*100:.2f}%")
        st.progress(acc)

# ------------------ COMPARISON ------------------
st.subheader("📊 Compare Algorithms")

if st.button("Compare All", key="compare"):

    if not trace:
        st.error("Trace is empty.")
        st.stop()

    results = []

    for algo in ["FIFO", "LRU", "ML-Based"]:
        predictor = DummyMLPredictor() if algo == "ML-Based" else None
        faults, _ = run(trace, algo, frames, predictor)
        hr = hit_ratio(faults, len(trace))

        results.append({
            "Algorithm": algo,
            "Faults": faults,
            "Hit Ratio": round(hr, 3)
        })

    st.table(results)