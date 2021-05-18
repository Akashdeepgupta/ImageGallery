import os
base_dir = os.path.dirname(__file__)
file = open(base_dir+'data_generator.py', 'r').read()
exec(file)