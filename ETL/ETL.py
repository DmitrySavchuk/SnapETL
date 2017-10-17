import subprocess
import sys

url = sys.argv[1]
html_file = sys.argv[2]
csv_file = sys.argv[3]

subprocess.call('Crawler.py ' + url + ' ' + html_file, shell=True)   # calling the ETL-modules
subprocess.call('Extractor.py ' + html_file + ' ' + csv_file, shell=True)
subprocess.call('Loader.py ' + csv_file, shell=True)
