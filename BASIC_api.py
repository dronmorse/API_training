import requests
import json

def formatted_print(data):
    text = json.dumps(data, sort_keys=True, indent=3)
    print (text)

output = requests.get("https://api.github.com/users/dronmorse")

print (output.status_code)
print (output.json())
formatted_print(output.json())