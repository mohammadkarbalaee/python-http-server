import socket

# Define server address
SERVER_HOST = 'https://python-http-server-zntk.onrender.com'  # The server's hostname or IP address
SERVER_PORT = 8080          # The port used by the server

# Define HTTP GET request
HTTP_REQUEST = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"

# Function to send HTTP GET request to server
def send_request():
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to server
        s.connect((SERVER_HOST, SERVER_PORT))
        
        # Send HTTP GET request to server
        s.sendall(HTTP_REQUEST.encode())

        # Receive and print data from server
        while True:
            data = s.recv(1024)
            if not data:
                break
            print(f"Received from server:\n{data.decode()}")

send_request()
