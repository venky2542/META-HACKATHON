import requests
import time

API_URL = "http://localhost:7860"

def main():
    # 1. Reset Environment
    requests.post(f"{API_URL}/reset")
    
    # 2. Loop to patch/shutdown servers
    # We run 20 steps to ensure 12 servers are handled
    for step in range(1, 21):
        # Get current state
        state = requests.get(f"{API_URL}/state").json()
        
        if state.get("done"):
            print("Task Completed Successfully")
            break
            
        # Action: Patch if servers exist
        action = {"type": "shutdown"}
        res = requests.post(f"{API_URL}/step", json=action).json()
        print(f"Step {step}: VMs Remaining: {res['vms']}")
        
        time.sleep(0.1)

if __name__ == "__main__":
    main()
