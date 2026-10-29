from pathlib import Path
root = Path("99-work/01-files")
root.mkdir(parents=True, exist_ok=True)
source = root / "01-message.txt"
source.write_text("hello platform\n", encoding="utf-8")
copy = root / "02-copy.txt"
copy.write_bytes(source.read_bytes())
print(source.name)
print(source.stat().st_size)
print(source.read_bytes() == copy.read_bytes())
