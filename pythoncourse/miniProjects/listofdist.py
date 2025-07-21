# 🔹 Agents ka list of dictionaries
agents = [
    {
        "name": "AgentAlpha",
        "tasks": ["search", "summarize", "respond"],
        "status": "active"
    },
    {
        "name": "AgentBeta",
        "tasks": ["calculate", "translate"],
        "status": "idle"
    },
    {
        "name": "AgentGamma",
        "tasks": [],
        "status": "error"
    }
]

# 🔄 Har agent ke liye loop chalega
for agent in agents:
    print(f"\n👤 {agent['name']} — Status: {agent['status']}")

    # Agar agent active hai to uske tasks ko run karo
    if agent["status"] == "active" and agent["tasks"]:
        print("🔄 Running tasks:")
        for task in agent["tasks"]:
            print(f"✅ Performing: {task}")
    elif agent["status"] == "idle":
        print("⏳ Agent is idle, waiting for instructions.")
    elif agent["status"] == "error":
        print("❌ Agent encountered an error. Sending alert...")
    else:
        print("📭 No tasks assigned.")
