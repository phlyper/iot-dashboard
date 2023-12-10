import os
from dotenv import load_dotenv, dotenv_values
from pathlib import Path
from io import StringIO

dotenv_path = Path('../.env')

env_stream = StringIO("USER=foo\nEMAIL=foo@example.org")
load_dotenv(stream=env_stream)

config = {
    **dotenv_values(dotenv_path=dotenv_path), # load shared development variables
    # **dotenv_values(),
    **os.environ,  # override loaded values with environment variables
}


# GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
# SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
# STORAGE_BUCKET_NAME = os.getenv('STORAGE_BUCKET_NAME')

import config.db

dbc = config.db.db_connect()
