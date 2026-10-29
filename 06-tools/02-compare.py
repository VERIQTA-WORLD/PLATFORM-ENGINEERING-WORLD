import sys
from pathlib import Path
if len(sys.argv) != 3:
    sys.exit('usage: python3 06-tools/02-compare.py FIRST SECOND')
equal = Path(sys.argv[1]).read_bytes() == Path(sys.argv[2]).read_bytes()
print('MATCH' if equal else 'DIFFERENT')
sys.exit(0 if equal else 1)
