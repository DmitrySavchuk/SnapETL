import json
import csv
import sys


in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file, 'r') as input_file:
    json_text = input_file.read()

jobs = json.loads(json_text)   # json to dictionary


job_list = []

i = 0
for job in jobs['jobs']:   # getting job information from dictionary to string list
    job_list.append([])
    job_list[i].append(job['title'])
    job_list[i].append(job['departments'][0]['name'])
    job_list[i].append(job['metadata'][0]['value'].title())
    job_list[i].append(job['offices'][0]['name'])
    i += 1

with open(out_file, "w", newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for job in job_list:
        writer.writerow(job)
