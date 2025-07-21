name = "Bilal"

text = "  Hello Agent Bilal  "

print(text.strip())         # "Hello Agent Bilal"
print(text.upper())         # "  HELLO AGENT BILAL  "
print(text.lower())         # "  hello agent bilal  "
print(text.replace("Agent", "AI"))  # "  Hello AI Bilal  "


sentence = "search summarize respond"

# Split → string → list
words = sentence.split()  # ['search', 'summarize', 'respond']

# Join → list → string
joined = "-".join(words)  # 'search-summarize-respond'

def build_prompt(agent_name, task):
    return f"Agent {agent_name} is now performing the task: {task.upper()}."

print(build_prompt("BilalBot", "search"))


def learning(friend_name, other_name):
    return f"Hey {friend_name} and {other_name}, let's learn Python together!"

print(learning("Ahmad", "waleed"))