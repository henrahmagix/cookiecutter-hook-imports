import re
import sys
from subprocess import check_output
from utils import which


required_commands = ['node', 'npm']

erred = False
for command in required_commands:
    if which(command) is None:
        erred = True
if erred:
    sys.exit(1)

node_version = check_output(["node", "--version"]).decode(sys.stdout.encoding).strip()
if re.match(r"^v4", node_version) is None:
    print('Node v4 is required but %s is found' % node_version)
    sys.exit(1)
