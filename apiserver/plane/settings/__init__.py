import os

from dotenv import load_dotenv

# Adjust the path if needed
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", ".env"))
print("Loading .env from:", os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", ".env"))