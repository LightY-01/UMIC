Prime Factorization Client-Server Application
This project contains a simple client-server application that computes the unique prime factors of a given positive integer. The server processes the input received from the client and returns the prime factors of the integer.

Files
server.py: A TCP server that listens for incoming connections, receives a number from a client, computes its unique prime factors, and sends the result back to the client.
client.py: A TCP client that connects to the server, sends a positive integer input, and displays the prime factors returned by the server.
Prerequisites
Python 3.x
A working internet or localhost connection for client-server communication
The socket library, which is included in the Python standard library
Setup and Running Instructions
Step 1: Clone or Download the Repository
Download or clone the project folder to your local machine.

Step 2: Run the Server
Open a terminal or command prompt.

Navigate to the folder containing the server.py file.

Run the server script using the following command:

bash
Copy code
python server.py
The server will start and listen for incoming client connections on 127.0.0.1:65432 (localhost).

You should see output like:

bash
Copy code
Server listening on 127.0.0.1:65432
Step 3: Run the Client
Open another terminal or command prompt.
Navigate to the folder containing the client.py file.
Run the client script using the following command:
bash
Copy code
python client.py
You should see output indicating that the client has connected to the server:
bash
Copy code
Connected to server at 127.0.0.1:65432
Step 4: Interact with the Application
The client will prompt you to enter a positive integer.

Enter a number (e.g., 12) and press Enter. The server will compute and return the unique prime factors. You should see output similar to:

bash
Copy code
Enter a positive integer (or 'q' to quit): 12
Prime factorization: 2, 3
If you enter an invalid number (e.g., negative or a non-integer value), the server will return an appropriate error message.

Enter 'q' to quit the client.

Example Session
Here’s an example of a session from the client side:

Connected to server at 127.0.0.1:65432
Enter a positive integer (or 'q' to quit): 28
Prime factorization: 2, 7
Enter a positive integer (or 'q' to quit): 1
Prime factorization: 1
Enter a positive integer (or 'q' to quit): -5
Prime factorization: Invalid input. Please send a positive integer.
Enter a positive integer (or 'q' to quit): abc
Prime factorization: Invalid input. Please send a positive integer.
Enter a positive integer (or 'q' to quit): q
Error Handling
If the input is not a valid integer, the server responds with the message: Invalid input. Please send a positive integer.
If a negative number or zero is entered, the same message is sent.
Notes
The server will run indefinitely and can handle multiple client connections sequentially. Each client must connect one at a time.
The prime factors of 1 are returned as {1}, which is a special case handled by the prime_factors() function.
Ensure that the server is running before you attempt to connect with the client.
Both the server and client scripts are designed to run on the same machine (localhost). To run the application over a network, adjust the host IP address accordingly.
Exiting the Program
To stop the client, enter q when prompted.
To stop the server, press CTRL + C in the terminal running the server.
