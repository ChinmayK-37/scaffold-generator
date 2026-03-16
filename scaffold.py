import os

STRUCTURE_FILE = "treeStructure.txt"
INDENT = 4

with open(STRUCTURE_FILE, "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f if line.strip()]

stack = []

for line in lines:

    indent = len(line) - len(line.lstrip(" "))
    level = indent // INDENT
    name = line.strip()

    stack = stack[:level]
    stack.append(name)

    path = os.path.join(*stack)

    # file
    if "." in name:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            open(path, "w").close()

    # folder
    else:
        os.makedirs(path, exist_ok=True)

print("Structure generated successfully.")