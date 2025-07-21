tasks = {
    "step1": "search",
    "step2": "summarize",
    "step3": "respond"
}

for step, task in tasks.items():
    print(f"🧠 {step.upper()} → Agent will {task}")
