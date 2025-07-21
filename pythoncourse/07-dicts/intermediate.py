agent = {
    "name": "TaskPlanner",
    "language": "Python",
    "active": True
}

print(agent["name"])        # TaskPlanner
print(agent["language"])    # Python


agent["active"] = False
agent["memory"] = "short-term"
# if we to add a new 
# if we should dell any
del agent["language"]
