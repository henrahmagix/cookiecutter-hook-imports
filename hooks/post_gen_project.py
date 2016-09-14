import json
import os
from collections import OrderedDict
from subprocess import call


# Overwrite properties in package.json.
print("Updating package.json...")
with open('package.json', 'r') as file_in, open('package.json.sample', 'r') as file_sample:
    # Keep the JSON object keys in the same order as they're read in.
    data = json.load(file_in, object_pairs_hook=OrderedDict)
    sample = json.load(file_sample, object_pairs_hook=OrderedDict)
    data.update(sample)
    with open('package.json', 'w') as file_out:
        # Pretty-print to 4-space indentation.
        json.dump(data, file_out, indent=4)
        os.remove('package.json.sample')
