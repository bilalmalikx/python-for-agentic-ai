tasks = ["search", "summarize", "calculate", "translate"]

def run_task(task_name):
    if task_name == "calculate":
        return (task_name, "error")  # Suppose calculation fail hogaya
    else:
        return (task_name, "done")


for task in tasks:
    result = run_task(task)  # Yeh tuple return karega
    task_name, status = result  # Tuple unpacking

    if status == "done":
        print(f"✅ {task_name} completed successfully.")
    elif status == "error":
        print(f"❌ {task_name} failed. Agent will retry or log error.")
    else:
        print(f"⏳ {task_name} is still in progress.")
