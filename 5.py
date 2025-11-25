class Process: 
def __init__(self, pid, active=True): 
self.pid = pid 
self.active = active 
def ring_election(processes, initiator): 
print(f"\nProcess {initiator} starts election...") 
msg = [] 
n = len(processes) 
index = initiator 
while True: 
p = processes[index] 
if p.active: 
print(f"Process {p.pid} passes message → {msg + [p.pid]}") 
msg.append(p.pid) 
index = (index + 1) % n 
if index == initiator: 
break 
coordinator = max(msg) 
print(f"\nCoordinator Elected: Process {coordinator}\n") 
return coordinator 
# ---------------- Main Program ---------------- # 
if __name__ == "__main__": 
process_ids = list(map(int, input("Enter process IDs (comma separated): ").split(","))) 
processes = [Process(pid) for pid in process_ids] 
initiator = int(input("Enter initiator process index (0-based): ")) 
ring_election(processes, initiator)
