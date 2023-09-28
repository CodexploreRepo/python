# Get current director
from pathlib import Path

# need to provide .resolve() before calling parents to go up certain level
data_path = Path("__file__").resolve().parents[1]

# convert Pathlib to String
data_path_str = data_path.as_posix()

# to create a folder if it is not exist
folder_path = Path('/this/is/the/new/folder')
# parents=True -> will create if parent folder is not existed
# exist_ok=True -> to ignore the warning if the parent folder is already existed
folder_path.mkdir(parents=True, exist_ok=True)
