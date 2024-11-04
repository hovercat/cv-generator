import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', '-d', type=str, help='path to data.json file', required=False)
parser.add_argument('--output', '-o', type=str, help='path to output file', required=False)
parser.add_argument('--index', '-i', type=str, help='path to index file', required=False)
args = parser.parse_args()

import json
from jinja2 import Environment, FileSystemLoader
import pathlib

with open(args.data if args.data else 'data.json', 'r') as f:
    data = json.load(f)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template(args.index if args.index else 'index.html')

output_path = pathlib.Path(args.output if args.output else 'output')
with open('output.html', 'w') as f:
    f.write(template.render(data))
