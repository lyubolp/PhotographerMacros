import json


def read_presets(path="presets.json") -> list:
    with open(path) as f:
        return json.loads(f.read())["presets"]
