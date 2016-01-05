## Unofficial Python lib for DNSdumpster (dnsdumpster.com)

### Usage

Install requirements:

```shell
pip install -r requirements.txt
```

Import the class:

```python
import dnsdumpsterapi
```

Extract all subdomains for specific domain:

```python
api = dnsdumpsterapi.DNSdumpster("apple.com")
print api.get_subdomains()
```

Result is an array (list()) of all subdomains.

### Contributing

Feel free to open issues, contribute and submit your Pull Requests.
