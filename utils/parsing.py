import argparse
import json
import sys

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to the experiment config file')

    args = parser.parse_args()
    return args.filepath

def parse_json(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.loads(f.read())
            return data
    except OSError as e:
        print(f'Unable to open "{filepath}": {e}', file=sys.stderr)
        sys.exit(e.errno)