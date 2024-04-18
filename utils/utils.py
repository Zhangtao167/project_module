import torch
import numpy as np
import yaml
import argparse
from datetime import datetime
import os
import pdb
def add_args_from_config(parser):
    args=parser.parse_args()
    with open(args.config, 'r') as file:
        config=yaml.safe_load(file)

    existing_args = {action.dest for action in parser._actions}
    
    # Add arguments from the config file to the parser
    for key, value in config.items():
        # If the argument is not already added, add it to the parser
        if key not in existing_args:
            parser.add_argument(f'--{key}', type=type(value), default=value)
    
    return parser
def save_config_from_args(args):
    config_dict = {k: v for k, v in vars(args).items() if k != 'config'}
    time_now = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    config_dir = args.exp_path+'/results/'+time_now
    os.makedirs(config_dir, exist_ok=True)  # Ensure the directory exists
    config_file_path = os.path.join(config_dir, 'config.yaml')
    with open(config_file_path, 'w') as file:
        yaml.dump(config_dict, file, default_flow_style=False)

    return 