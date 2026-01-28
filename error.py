import json

# INTENTIONAL ERROR
data = "{ bad json "
json.loads(data)
