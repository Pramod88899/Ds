import datetime
import socket
import time


def sendClockTime(server_address, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_address, port))
        print("Connected to the server successfully.")

        while True:
            current_time = datetime.datetime.now()
            client_socket.send(str(current_time).encode())
            print("Sent clock time to the server:", current_time)
            time.sleep(5)  # Send clock time every 5 seconds
    except Exception as e:
        print("An error occurred while connecting to the server:", str(e))
    finally:
        client_socket.close()


if __name__ == '__main__':
    server_address = 'localhost'  # Replace with the server's IP address or hostname
    server_port = 8080  # Replace with the server's port number

    sendClockTime(server_address, server_port)
