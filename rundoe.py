from utils.parser import parse_args, parse_json
from runner import Runner

filepath = parse_args()
print('-==== RunDOE ====-\n')
config = parse_json(filepath)
runner = Runner(config)
runner.run()