# Get current director
from pathlib import Path

# need to provide .resolve() before calling parents to go up certain level
data_path = Path("__file__").resolve().parents[1]

# convert Pathlib to String
data_path = data_path.as_posix()