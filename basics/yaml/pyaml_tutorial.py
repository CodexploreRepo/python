# !pip install pyaml
from pathlib import Path
from pprint import pprint

import yaml

curr_dir = Path(__file__).resolve().parent

with open(curr_dir / "data/config.yaml", "r") as f:
    # load_all: is to load multiple document in a single YAML
    # safe_load: is to load the config in safe manner
    """
    docs = yaml.load_all(f, Loader=yaml.FullLoader) # multiple_docs.yaml

    for doc in docs:
        for k, v in doc.items():
            print(k, v)
    """

    config = yaml.safe_load(f)
    pprint(config, sort_dicts=False)
