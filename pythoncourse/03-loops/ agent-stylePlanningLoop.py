agent_state = {"status": "working", "steps_done": 0}

while agent_state["status"] != "done":
    print(f"🔄 Step {agent_state['steps_done'] + 1}: Agent planning...")

    agent_state["steps_done"] += 1

    if agent_state["steps_done"] == 3:
        agent_state["status"] = "done"

print("✅ Agent finished the plan.")
