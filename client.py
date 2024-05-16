import socket

SERVER_HOST = '127.0.0.1' 
SERVER_PORT = 8080         

HTTP_REQUEST = "GET /index.html HTTP/1.1\r\nHost: localhost\r\n\r\n"

def send_request():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        
        s.sendall(HTTP_REQUEST.encode())

        while True:
            data = s.recv(1024)
            if not data:
                break
            print(f"Received from server:\n{data.decode()}")

send_request()
