import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
# Access the API key from environment variables
api_key = os.getenv("API_KEY")
