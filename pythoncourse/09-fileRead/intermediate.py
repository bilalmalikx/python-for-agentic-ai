# Step 1: Agent completes task
result = {
    "agent": "BilalBot",
    "completed": True,
    "output": "Search completed with 3 results."
}

# Step 2: Save result to file
import json
with open("task_result.json", "w") as f:
    json.dump(result, f)

# Step 3: Load again when needed
with open("task_result.json", "r") as f:
    memory = json.load(f)

print(memory["output"])
