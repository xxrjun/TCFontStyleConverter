from dotenv import load_dotenv
import os

load_dotenv('../.env')

var = "ACCESS_TOKEN"
value = os.getenv(var)


print(f'export {var}="{value}"')