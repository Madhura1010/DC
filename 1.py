class RR: 
def __init__(self, servers): 
self.s = servers 
self.i = 0 
def next(self): 
if not self.s: return None 
srv = self.s[self.i] 
self.i = (self.i + 1) % len(self.s) 
return srv 
def add(self, x): 
self.s.append(x) 
def remove(self, x): 
if x in self.s: 
self.s.remove(x) 
if self.i >= len(self.s): 
self.i = 0 
if __name__ == "__main__": 
servers = [s.strip() for s in input("Enter servers: ").split(",")] 
lb = RR(servers) 
ch = input("Add or remove server? (add/remove/none): ").lower() 
if ch == "add": 
lb.add(input("Server to add: ")) 
elif ch == "remove": 
lb.remove(input("Server to remove: ")) 
n = int(input("Enter number of requests: ")) 
for r in range(1, n + 1): 
print(f"Request {r}: {lb.next()}") 
