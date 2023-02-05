import requests
import argparse

URL = 'https://dns.pl/api/domain-browser'

parser = argparse.ArgumentParser(description='Dns.pl API call')
parser.add_argument('--domain', default=None, help='Domain name')
args = parser.parse_args()

if args.domain:
  data = {'domain_browser[domain]': args.domain, 'domain_browser[lang]': 'pl'}
  result = requests.post(URL, data=data).json()
  print(result)
