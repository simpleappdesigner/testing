# run it $echo '[{"k": ["10", "20"]}]' | python3 myscript.py - 
import argparse, json

parser = argparse.ArgumentParser()
parser.add_argument('json', nargs='?', type=argparse.FileType('r'))
args = parser.parse_args()
with args.json as f:
  obj = json.load(f)
print(obj)
