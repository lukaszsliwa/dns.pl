# dns.pl
### Checking available domains from the input file

Create a file `domains.input` with a list of all domain that should be checked and call:

```python
python3 find.py --input domains.input --output domains.output
```

`domains.output` should contains the results

### Generate input file

You can generate input files using `generate.py`:

```python
python3 generate.py --tld pl --length 3 --output 3-domains.txt
```

The above command will create 3-domains.txt file with a list of all domains the length of 3 characters.
Add --list to set the list of characters:

```python
python3 generate.py --tld pl --length 3 --output 3-domains.txt --list ab09
```

### Calling for the specific domain data

```python
python3 api.py --domain abc.pl
```

```json
{'apiResponse': {'errors': [], 'name': 'abc', 'results': {'abc.pl': 1}}, 'zonesCheck': [], 'domainParsed': {'container': {}, 'zoneStats': {}, 'lang': 'pl', 'domain': 'abc.pl', 'domainLabel': 'abc', 'domainParent': ['pl'], 'domainLabelMain': 'abc', 'secondLevelOwnedByNask': True, 'secondLevelIsGovPl': False, 'parsedArray': ['abc', 'pl'], 'notPl': False}}
```

## Links

* https://github.com/lukaszsliwa/dns.pl/wiki/DNS.pl-API-endpoint
* https://dns.pl/
* https://github.com/lukaszsliwa/dns.pl 
* https://lukaszsliwa.github.io/dns.pl/
