step_result = ("search", "done")

if step_result[1] == "done":
    print(f"✅ Task {step_result[0]} completed")
else:
    print(f"❌ Task {step_result[0]} failed")
