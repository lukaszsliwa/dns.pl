import string
import argparse
import itertools
import re

parser = argparse.ArgumentParser(description='Generate valid domains')
parser.add_argument('--output', default='dns.txt', help='Output file')
parser.add_argument('--length', default=3)
parser.add_argument('--tld', default='pl')
parser.add_argument('--list', default='')
args = parser.parse_args()

lst = list(string.ascii_lowercase)
lst += list(string.digits)
lst += list('-')

if len(args.list) > 0:
  lst = list(args.list)

with open(args.output, 'w') as file:
  for x in itertools.product(lst, repeat=int(args.length)):
    name = ''.join(x)
    domain = f'{name}.{args.tld}'

    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"
    p = re.compile(regex)

    if re.search(p, domain):
      file.write(f'{domain}\n')
