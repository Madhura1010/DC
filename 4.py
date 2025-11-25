import socket # Import socket module
# Create a socket object
s = socket.socket()

# Bind the socket to localhost on port 6666
s.bind(('localhost', 6666))

# Start listening for a connection (max 1 client)
s.listen(1)
print("Waiting for connection...")
# Accept a client connection
conn, addr = s.accept()
print("Connected by", addr)

# Receive data from client (max 1024 bytes)
data = conn.recv(1024).decode()

# Split the received string into two parts
a, b = data.split()

# Convert to integers and print their sum
print("Sum =", int(a) + int(b))
# Close the connection
conn.close()
s.close()


####### Client.py ###########


import socket # Import socket module
# Create a socket object
s = socket.socket()

# Connect to the server on localhost and port 6666
s.connect(('localhost', 6666))

# Get two numbers from the user
a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")

# Send both numbers to server as a single string
s.send(f"{a} {b}".encode())

# Close the connection
s.close()
