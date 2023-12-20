# `.env`
- Installation: `pip install python-dotenv==1.0.0`
- Config file stores in `.env` file
```shell
HUGGINGFACEHUB_API_TOKEN="<hf_token>"
```
- Load environmental variables
```Python
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv("../config/.env") 
# load_dotenv(find_dotenv()) # find_dotenv() is to find the .env 
os.environ["HUGGINGFACEHUB_API_TOKEN"] = ... # insert your API_TOKEN here
```
