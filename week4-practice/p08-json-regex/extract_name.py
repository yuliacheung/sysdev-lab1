import json
import sys

data = json.load(sys.stdin)
print(data["name"])
