class NameResolver: 
def __init__(self): 
self.records = { 
"example.com": "33.423.243.24", 
"openai.com": "12.233.32.44", 
"google.com": "54.234.678.98" 
} 
self.cache = {} 
def resolve(self, hostname): 
if hostname in self.cache: 
return self.cache[hostname] 
ip = self.records.get(hostname) 
if ip: 
self.cache[hostname] = ip 
return ip 
return None 
if __name__ == "__main__": 
resolver = NameResolver() 
hostnames = ["example.com", "openai.com", "google.com", "not_exist.com"] 
for h in hostnames: 
ip = resolver.resolve(h) 
if ip: 
print(f"{h} -> resolves to -> {ip}") 
else: 
print(f"{h} does not exist")
