lock = False
     # False = free, True = busy 
current_process = None 
process_id = 0 
print("Press a key (except q) to enter a process:") 
print("Press q at any time to exit") 
while True: 
key = input() 
if key == "q": 
break 
print(f"Process {process_id} wants to enter...") 
if not lock:   # critical section is free 
lock = True 
current_process = process_id 
print(f"Process {process_id} entered critical section.") 
print(f"Process {process_id} exited critical section.") 
lock = False 
current_process = None 
else: 
print("Error: Another process is currently executing!") 
process_id += 1
