import json

requirements = {"length":8,"min_length":8,"max_length":12,"symbol":True,"letters":True,"numbers":True,"capital_letters":True}

with open('json_storage/requirements.json', 'w') as file:
    json.dump(requirements, file, indent = 4) # the indent makes the file easier to read
