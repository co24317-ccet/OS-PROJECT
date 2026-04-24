# ML-Based Page Replacement (Streamlit UI)

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Structure
- app.py: Streamlit UI + simulation + animated charts
- algorithms/: FIFO, LRU, ML policy
- simulator/: controller
- utils/: trace generator, metrics
- ml/: predictor stubs (plug your trained model here)
