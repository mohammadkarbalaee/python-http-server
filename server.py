import socket
import threading

HOST = '127.0.0.1' 
PORT = 8080     


with open("index.html", "r") as file:
    INDEX_HTML_CONTENT = file.read()

with open("404.html", "r") as file:
    NOT_FOUND_HTML_CONTENT = file.read()


HTTP_RESPONSE_OK = f"""\
HTTP/1.1 200 OK

{INDEX_HTML_CONTENT}
"""

HTTP_RESPONSE_NOT_FOUND = f"""\
HTTP/1.1 404 Not Found

{NOT_FOUND_HTML_CONTENT}
"""

def handle_client(conn, addr):
    print(f"Connected by {addr}")

    data = conn.recv(1024)
    if data:
        print(f"Request from {addr}:\n{data.decode()}")

        if data.decode().startswith("GET /index.html"):
            conn.sendall(HTTP_RESPONSE_OK.encode())
        else:
            conn.sendall(HTTP_RESPONSE_NOT_FOUND.encode())

    conn.close()
    print(f"Connection closed by {addr}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    
    s.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()

        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
