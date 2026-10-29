from pathlib import Path
root = Path("99-work/03-safe-root").resolve()
root.mkdir(parents=True, exist_ok=True)
def destination(relative):
    candidate = (root / relative).resolve()
    if candidate != root and root not in candidate.parents:
        raise ValueError("destination leaves allowed root")
    return candidate
print(destination("01-note.txt").name)
try:
    destination("../04-outside.txt")
except ValueError as error:
    print(error)
