import socket
import re

HOST = "localhost"
PORT = 3000
search_username_string = '(?<=username=)([^&]*)(?=&)?'
search_password_string = '(?<=password=)([^&]*)(?=&)?'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            request = conn.recv(1024)
            if not request:
                break
            request = str(request)
            username_in_list = re.findall(search_username_string, request)
            password_in_list = re.findall(search_password_string, request)
            print(username_in_list, password_in_list)
            print('Content = %s' % request)
    conn.close()

