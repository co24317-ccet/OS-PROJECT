# ML-Based Page Replacement Project CO24317 

## Brief Overview

Effective memory management plays an important role in improving
the performance of an operating system in conditions where the amount of physical
memory available is restricted. In this work, an interactive simulation environment
has been developed to investigate the efficiency of different page replacement
algorithms. In addition to using standard techniques such as FIFO and LRU, a new
mechanism based on machine learning is proposed for the prediction of future
memory accesses based on past behavior.The application is developed using a
web-based frontend which enables the user to simulate both random reference
string generation or import reference strings from external sources in order to
observe the behavior of different page replacement policies. In addition to
generating statistics related to page faults and hit rate, a step-by-step execution of
each algorithm can be achieved by the user. By using machine learning in the page
replacement algorithm, a certain level of predictability is obtained to select and
keep the appropriate pages in memory.Even though the application uses a primitive
machine learning method, the possibility of integrating more complicated machine
learning algorithms is considered in the design of the framework, which could
serve as the basis for conducting additional studies in this area.

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
- ml/: predictor 
