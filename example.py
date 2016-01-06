import dnsdumpsterapi

api = dnsdumpsterapi.DNSdumpster()
print api.get_subdomains("apple.com")