# Simple Distributed Deadlock Example 
# Resource ownership 
resources = { 
"R1": "P1",   # P1 has R1 
"R2": "P1"    # P1 has R2 
} 
# Print what P1 has 
print("P1 acquired R1.") 
print("P1 acquired R2.") 
# P2 tries to acquire R1 
needed = "R1" 
holder = resources[needed] 
print(f"P2 is waiting for {needed} held by {holder}.") 
# Deadlock check 
if holder == "P1" and len(resources.values()) == list(resources.values()).count("P1"): 
print(f"Potential deadlock detected with P1 holding {len(resources)} resources")
