import requests
import string
import argparse
import datetime
import os

URL = 'https://dns.pl/api/domain-browser'

parser = argparse.ArgumentParser(description='Dns.pl')
parser.add_argument('--input', default='domains.txt', help='Input file')
parser.add_argument('--output', default='result.txt', help='Output file')
args = parser.parse_args()

lst = list(string.ascii_lowercase)
lst += list(string.digits)

domains = {}
if os.path.exists(args.output):
  with open(args.output, 'r') as output:
    for line in output.readlines():
      domain, checked_at, value = line.strip().split(',')
      value = value.strip()
      domains[domain] = value

with open(args.input, 'r') as input:
  for domain in input.readlines():
    domain = domain.strip()
    if domain == 'xor.pl' or domains.get(domain):
      continue
    data = { 'domain_browser[domain]': domain, 'domain_browser[lang]': 'pl' }
    resp = requests.post(URL, data=data).json()
    if len(resp['apiResponse']['errors']) > 0:
      if resp['apiResponse']['errors'].get('limit'):
        print(resp['apiResponse']['errors']['limit'])
        exit(1)
    with open(args.output, 'a') as output:
      current = datetime.datetime.now().isoformat()
      not_available = f'{domain},{current},not available'
      available = f'{domain},{current},available'
      if len(resp['apiResponse']['results']) == 0:
        print(not_available)
        output.write(f'{not_available}\n')
      elif domain in resp['apiResponse']['results'] and int(resp['apiResponse']['results'][domain]) == 0:
        print(available)
        output.write(f'{available}\n')
      else:
        print(not_available)
        output.write(f'{not_available}\n')
