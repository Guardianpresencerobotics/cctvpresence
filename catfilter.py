import os
import datetime
import subprocess
import re

[query_date = datetime.datetime.fromtimestamp(int(float(1516188526532974000)/1000000000))
results = []
for root, dirs, files in os.walk('/Users/Nafty/Sync/sxs'):
    for filename in files:
        path = os.path.join(root, filename)
        file_mtime = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
        if(file_mtime > query_date):
            results.append(path)  # yield path?

return results]



{timestamp = '"2018-01-17 03:28:46"'
path = '.'
files = []
find = subprocess.Popen('find ' + path + ' -newermt ' + timestamp, shell=True, 
stdout=subprocess.PIPE)
for line in find.stdout:
   files.append(line.decode('UTF-8').strip())
print(files)}




[files = [file for file in os.listdir(".") if (file.lower().endswith('.gz'))]
files.sort(key=os.path.getmtime)

for file in sorted(files,key=os.path.getmtime):
    print(file)]
