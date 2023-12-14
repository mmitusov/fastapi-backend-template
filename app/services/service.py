from dotenv import load_dotenv
import os
from app.helpers.utils import helper_func

load_dotenv()
gitlab_access_token = os.getenv("GITLAB_ACCESS_TOKEN_PROD")
openai_api_key = os.getenv("OPENAI_API_KEY")

class Service:
  async def service1():
    try:
      data = helper_func()
      return "Test!"
    except Exception as error:
        print(f"Error occurred. Error: {error}")
        return