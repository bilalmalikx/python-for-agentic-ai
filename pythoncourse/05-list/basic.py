fruits = ["apple", "banana", "cherry"]

names = ["Bilal", "Ahmed", "Ayesha"]

print(names[0])  # Bilal
print(names[-1]) # Ayesha

# Add item
names.append("Zara")        # end mein add
names.insert(1, "Usman")    # index pe add

# Remove item
names.remove("Ahmed")       # name se remove
names.pop()                 # last item remove

# Update item
names[0] = "Ali"
