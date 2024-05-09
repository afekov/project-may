import socket, threading
import datetime
MAX_CLIENTS = 1000
port = 8820
all_to_die = False

def handle_client(client_socket, name, client_address):
    return
def main():
    global all_to_die, port, MAX_CLIENTS
    threads = []
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(MAX_CLIENTS)
    print("Server is up and running")
    while True:
        (client_socket, client_address) = server_socket.accept()
        print("Client connected")
        t = threading.Thread(target=handle_client, args=(client_socket, str(client_address)+str(datetime.datetime.now()), client_address))
        t.start()
        threads.append(t)


# if __name__ == '__main__':
# 	main()
