import dnsdumpsterapi

api = dnsdumpsterapi.DNSdumpster("apple.com")
print api.get_subdomains()