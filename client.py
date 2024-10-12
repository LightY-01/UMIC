import socket  # Import the socket library for network communication

host = '127.0.0.1'  # Localhost (loopback address)
port = 65432        # Port number of the server

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establish a connection to the server
s.connect((host, port))
print(f"Connected to server at {host}:{port}")  # Notify the user of a successful connection

while True:
    # Prompt the user for input
    num = input("Enter a positive integer (or 'q' to quit): ")
    
    # Check if the user wants to quit
    if num.lower() == 'q':
        break  # Exit the loop if 'q' is entered
    
    # Send the input number to the server
    s.sendall(num.encode())
    
    # Receive the response from the server
    data = s.recv(1024)  # Buffer size is 1024 bytes
    # Print the server's response, which contains the prime factorization
    print(f"Prime factorization: {data.decode()}")

# Close the socket connection before exiting
s.close()
