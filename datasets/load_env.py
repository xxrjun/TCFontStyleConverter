from dotenv import load_dotenv
import os

load_dotenv()

var = "ACCESS_TOKEN"
value = os.getenv(var)


print(f'export {var}="{value}"')