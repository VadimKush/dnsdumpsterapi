import dnsdumpster

api = dnsdumpster.DNSdumpster("apple.com")
print api.get_subdomains()