import os

for folder in ["novo_dataset/cookies/labels"]:
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r") as f:
                lines = f.readlines()
            with open(path, "w") as f:
                for line in lines:
                    parts = line.strip().split()
                    parts[0] = "0"  # muda a classe para 0
                    f.write(" ".join(parts) + "\n")