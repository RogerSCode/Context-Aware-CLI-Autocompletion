import os
import glob
import sys
path = os.environ['PATH']
paths = path.split(os.pathsep)
files = []
for p in paths:
    files.extend(glob.glob(os.path.join(p, '*')))
# sepparate commands
commands = []
for f in files:
    commands.append(f.rsplit('/', 1)[1])

prefix = sys.argv[1]
for command in commands:
    if command.startswith(prefix):
        print(command[len(prefix):])
        break        


