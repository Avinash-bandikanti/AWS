import socket
import json


# function to read a json config file
def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config


def main():
    config = read_config('config_file.json')

    # extract server onformation from configuration
    server_info = config['servers'][0]
    server_ip = server_info['ip']
    server_port = server_info['port']
    max_buffer_size = config['max_buffer_size']

    # creating a socket for server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to the servers ip and port
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print(f"Server listening on {server_ip}:{server_port}")
    while True:
        # Accept incoming client connections
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        try:
            # receive data from client and decode it
            data = client_socket.recv(max_buffer_size).decode()
            print("received from client", data)
            if data == 'exit':
                print("Client sent 'exit', so client connection is closed. ")
                break

            response = f"Server1 received: {data}"
            client_socket.send(response.encode())

        except Exception as e:
            # handle any exceptions that may occur during communication between client
            print(f"Error handling client: {e}")
        finally:
            # close the client socket
            client_socket.close()

    # close server socket when loop exits
    server_socket.close()


# when script is run it executes the main function
if __name__ == "__main__":
    main()
