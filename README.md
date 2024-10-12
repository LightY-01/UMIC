# Prime Factorization Server/Client

This project implements a simple client-server application that calculates the prime factorization of positive integers. The server listens for incoming connections, receives numbers from clients, computes their prime factors, and sends the results back to the clients.

## Prerequisites

- Python 3.6 or higher

## Files

- `server.py`: The server-side script that listens for connections and computes prime factors.
- `client.py`: The client-side script that connects to the server and sends numbers for factorization.

## Running the Application

### Starting the Server

1. Open a terminal or command prompt.
2. Navigate to the directory containing the project files.
3. Run the following command:

   ```
   python server.py
   ```

4. You should see a message indicating that the server is listening on 127.0.0.1:65432.

### Running the Client

1. Open a new terminal or command prompt (keep the server running in the first one).
2. Navigate to the directory containing the project files.
3. Run the following command:

   ```
   python client.py
   ```

4. You should see a message indicating that the client has connected to the server.
5. Follow the prompts to enter positive integers for prime factorization.
6. Enter 'q' to quit the client application.

## Testing the Application

1. Ensure the server is running in one terminal.
2. Start the client in another terminal.
3. Test various scenarios:
   - Enter positive integers (e.g., 12, 97, 100) and verify the correct prime factorization is returned.
   - Enter 1 and verify it returns {1}.
   - Enter negative numbers or non-integer values to test error handling.
   - Enter very large numbers (e.g., 123456789) to test performance with big integers.
4. Quit the client by entering 'q'.
5. You can run multiple client instances simultaneously to test concurrent connections.

## Notes

- The server runs indefinitely until manually terminated (e.g., by pressing Ctrl+C).
- The client will disconnect after entering 'q', but the server will continue running and accepting new connections.
- For security reasons, this application only accepts connections from localhost (127.0.0.1). Modify the `host` variable in both scripts if you want to allow remote connections.

## Troubleshooting

- If you encounter a "Address already in use" error when starting the server, ensure no other application is using port 65432, or modify the `port` variable in both scripts to use a different port number.
- If the client fails to connect, ensure the server is running and that both scripts are using the same host and port numbers.
