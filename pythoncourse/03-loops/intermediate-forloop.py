agent_plan = ["analyze", "search", "respond"]

for step in agent_plan:
    if step == "search":
        print("🔍 Agent is using web search tool")
    elif step == "respond":
        print("💬 Agent is writing a final answer")
    else:
        print("🧠 Agent is analyzing task")
