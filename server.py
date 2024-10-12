import socket  # Import the socket library for network communication

def prime_factors(n):
    """Function to compute the unique prime factors of a given number n."""
    factors = set()  # Use a set to hold the unique prime factors

    if n < 1:  # Handle case for negative numbers and zero
        return None

    if n == 1:  # Special case for 1
        return {1}  # Return 1 as a unique factor

    d = 2  # Starting divisor

    while n > 1:
        while n % d == 0:
            factors.add(d)  # Use set to ensure unique factors
            n //= d  # Reduce n by the factor
        d += 1  # Move to the next potential factor

        if d * d > n:  # If d exceeds the square root of n
            if n > 1:  # If there is still a remainder, it must be prime
                factors.add(n)
            break  # Exit the loop if we've found all factors
    return sorted(factors)  # Return the sorted list of unique prime factors


host = '127.0.0.1'  # Localhost (loopback address)
port = 65432        # Port to listen on

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
s.bind((host, port))  # Bind the socket to the address and port
s.listen()  # Start listening for incoming connections
print(f"Server listening on {host}:{port}")  # Notify that the server is ready

while True:
    conn, addr = s.accept()  # Accept a connection from a client
    print(f"Connected by {addr}")  # Print the address of the connected client

    while True:
        data = conn.recv(1024)  # Receive data from the client
        if not data:
            break  # Exit if no data is received
        
        try:
            num = int(data.decode())  # Decode the received data to an integer
            if num < 1:  # Handle invalid input (negative numbers)
                response = b"Invalid input. Please send a positive integer."
            else:
                factors = prime_factors(num)  # Get the unique prime factors of the number
                response = ', '.join(map(str, factors)).encode()  # Prepare the response

            conn.sendall(response)  # Send the response back to the client
        
        except ValueError:
            # Handle invalid input (non-integer values)
            conn.sendall(b"Invalid input. Please send a positive integer.")
        except Exception as e:
            print(f"Error: {e}")  # Print the error message
            conn.sendall(b"An error occurred. Please try again.")

    conn.close()  # Close the connection with the client
