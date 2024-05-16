import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8080

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))

        while True:
    
            file_name = input("Enter file name (or 'exit' to quit): ")

            if file_name.lower() == 'exit':
                s.sendall(b"__CLOSE_CONNECTION__")
                break

            HTTP_REQUEST = f"GET /{file_name} HTTP/1.1\r\nHost: localhost\r\n\r\n"

            s.sendall(HTTP_REQUEST.encode())

            file = open('response.txt', 'wb')

            while True:
                line = s.recv(1024)
                if b'__END_OF_TRANSMISSION__' in line:
                    line = line.replace(b'__END_OF_TRANSMISSION__', b'')
                    file.write(line)
                    break
                else:
                    file.write(line)

            file.close()
            with open('response.txt', 'r') as file:
                first_line = file.readline()
                print(f"----------- HTTP RESPONSE ----------- \n{first_line}")

        s.close()    
