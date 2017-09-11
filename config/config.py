import json
import os

def _load_endpoints(running_mode):
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    endpoints_path = os.path.join(parent_dir, 'endpoints.json')

    with open(endpoints_path) as endpoints_file:
        return json.load(endpoints_file)[running_mode]

def _set_running_mode():
    mode = os.environ.get('RUNNING_MODE')  # We load the contents of this environment var.

    # In case the var was empty or set with an unknown value, the default will be "develop"
    if mode is None or mode not in ['develop', 'test', 'production']:
        mode = 'develop'

    return mode if mode in ['develop', 'test', 'production'] else 'develop'

running_mode = _set_running_mode()
endpoints = _load_endpoints(running_mode)
