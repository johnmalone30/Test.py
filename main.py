import requests
import json
from datetime import datetime
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)