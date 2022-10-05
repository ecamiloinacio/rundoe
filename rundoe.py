import subprocess
from itertools import product
from sys import stderr, stdout
from utils.parsing import parse_args, parse_json

filepath = parse_args()
config = parse_json(filepath)

factors = {}
args_ref = {}
for factor in config['factors']:
    factors[factor['name']] = factor['values']
    args_ref[factor['name']] = factor['arg']


guide = list(dict(zip(factors.keys(), values)) for values in product(*factors.values()))

for trial in guide:
    cmd = [config['cmd']]
    for arg_key, arg_val in trial.items():
        cmd.append(args_ref[arg_key])
        cmd.append(str(arg_val))
    print(cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout.decode('utf-8'))