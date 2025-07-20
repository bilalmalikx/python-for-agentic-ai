def agent_decide(state):
    if state.get("task") == "complete":
        return "Agent: Shutting down"
    elif state.get("error"):
        return f"Agent: Handling error: {state['error']}"
    elif state.get("needs_tool"):
        return f"Agent: Calling tool {state['tool_name']}"
    else:
        return "Agent: Planning next step"

# Example input
state = {
    "task": "running",
    "needs_tool": True,
    "tool_name": "web_search"
}

print(agent_decide(state))


#kitchen task with real world example
def kitchen_task(state):
    if state.get("task") == "complete":
        return "agent: Shutting down"
    elif state.get("error"):
        return f"agent: i am handling the error: {state['error']}"
    elif state.get("needs_tool"):
        return f"kitchen: calling tool {state['tool_name']}"
    else:
        return "kitchen: Planning next step"
    
state = {
    "task": "Clean the kitchen",
    "needs_tool": True,
    "tool_name": "mop"
}
print(kitchen_task(state))

