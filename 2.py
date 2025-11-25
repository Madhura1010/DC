import threading 
import time 
import queue 
task_queue = queue.Queue() 
# Put tasks 
for i in range(5): 
task_queue.put(f"Task {i}") 
def worker(worker_id): 
while not task_queue.empty(): 
try: 
task = task_queue.get_nowait() 
except queue.Empty: 
break 
print(f"Worker {worker_id} processing: {task}") 
time.sleep(0.5)  # simulate work 
print(f"Worker {worker_id} finished: {task}") 
task_queue.task_done() 
workers = [] 
# Start 2 workers 
for i in range(2): 
t = threading.Thread(target=worker, args=(i,)) 
workers.append(t) 
t.start() 
# Wait for all workers to finish 
for t in workers: 
t.join() 
print("All tasks processed.") 
