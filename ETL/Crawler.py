import requests
import sys


url = str(sys.argv[1])
out_file = sys.argv[2]

json = requests.get(url)  # getting the json-answer from url

with open(out_file, 'w') as output_file:
    output_file.write(json.text)
