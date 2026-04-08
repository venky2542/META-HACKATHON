from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import psutil

app = FastAPI(title="Meta-Hack: OpenEnv Pro Optimizer")

# Simulation State
state = {"vms": 12, "reward": 0.0, "latency": 40.5, "done": False}

@app.get("/state")
def get_state():
    return {**state, "cpu": psutil.cpu_percent(), "mem": psutil.virtual_memory().percent}

@app.post("/reset")
def reset():
    global state
    state = {"vms": 12, "reward": 0.0, "latency": 40.5, "done": False}
    return state

@app.post("/step")
def step(action: dict):
    global state
    act = action.get("type", "")
    if act == "shutdown": 
        state["vms"] = max(0, state["vms"] - 1)
        state["reward"] += 0.1
    if act == "patch": 
        state["reward"] += 1.0
    
    # Logic to complete the task
    if state["vms"] <= 0:
        state["done"] = True
        
    return state

@app.get("/", response_class=HTMLResponse)
async def home():
    # Insert the HTML string from your aim.ipynb here
    return "<h1>System Online</h1>"
