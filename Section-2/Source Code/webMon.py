import sys
import requests
from pathlib import Path


all_args = sys.argv[1:]
opts = [opt for opt in all_args if opt.startswith("-")]
sites = [opt for opt in all_args if not opt.startswith("-") ]
fname = Path(__file__).name

if len(opts) > 1:
    print('Please enter one timeout')
    exit
elif len(opts) == 0:
    timeout = 5
elif opts[0] == '--help' or opts[0] == '-help':
    help_msg = f"""
    Usage: {fname} website1 website2 website3 [OPTION]
      Website health monitor

    Options:
      -t=x     timeout in seconds replace x with required timeout
"""
    print(help_msg)
    quit()
else:
    try:
        opt = opts[0].split('=')[-1]
        timeout = float(opt)
    except ValueError:
        print('Please enter a valid timeout')

if len(sites) >= 1:
    for site in sites:
        try:
            response = requests.get(site, timeout=timeout)
            if response.status_code == 200:
                print(f'Website {site} is responding in timely manner')
            else:
                print(f'Website {site} is not responding')
        except requests.exceptions.ConnectionError:
            print(f'Website {site} is not responding')
        except requests.exceptions.MissingSchema:
            print(f'Please enter a valid url for website {site}')

else:
    print(f'{fname}: missing arguments')
    print(f'try {fname} --help for more information')
