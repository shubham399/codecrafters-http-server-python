# Uncomment this to pass the first stage
import socket


# parse received HTTP request
def parse(data):
    lines = data.split(b"\r\n")
    # print(lines[0].split(b' '))
    path = lines[0].split(b" ")[1]
    if path == b"/":
        return b"HTTP/1.1 200 OK\r\n\r\n"
    else:
        return b"HTTP/1.1 404 Not Found\r\n\r\n"

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    conn, address = server_socket.accept()  # wait for client
    
    data = conn.recv(1024)
    # parse the data
    res = parse(data)
    print(res)
    conn.sendall(res)

if __name__ == "__main__":
    main()
