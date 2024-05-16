import socket
import threading

# Define host and port
HOST = 'https://python-http-server-zntk.onrender.com'  # Standard loopback interface address (localhost)
PORT = 8080        # Port to listen on (non-privileged ports are > 1023)

# Read the content of index.html
with open("index.html", "r") as file:
    INDEX_HTML_CONTENT = file.read()

# Read the content of 404.html
with open("404.html", "r") as file:
    NOT_FOUND_HTML_CONTENT = file.read()

# Define HTTP response
HTTP_RESPONSE_OK = f"""\
HTTP/1.1 200 OK

{INDEX_HTML_CONTENT}
"""

HTTP_RESPONSE_NOT_FOUND = f"""\
HTTP/1.1 404 Not Found

{NOT_FOUND_HTML_CONTENT}
"""

# Function to handle client requests
def handle_client(conn, addr):
    print(f"Connected by {addr}")

    # Receive data from client
    data = conn.recv(1024)
    if data:
        # Print details of the HTTP request
        print(f"Request from {addr}:\n{data.decode()}")

        if data.decode().startswith("GET /index.html"):
            # Send HTTP response with index.html content to client
            conn.sendall(HTTP_RESPONSE_OK.encode())
        else:
            # Send a 404 response for requests other than index.html
            conn.sendall(HTTP_RESPONSE_NOT_FOUND.encode())

    # Close connection
    conn.close()
    print(f"Connection closed by {addr}")

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind the socket to the address
    s.bind((HOST, PORT))
    
    # Listen for incoming connections
    s.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        # Accept connections from clients
        conn, addr = s.accept()

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
