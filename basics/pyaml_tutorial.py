# !pip install pyaml
from pathlib import Path

import yaml

curr_dir = Path(__file__).resolve().parent
with open(curr_dir / "data/items.yaml", "r") as f:
    # load_all: is to load multiple document in a single YAML
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:
        for k, v in doc.items():
            print(k, v)
