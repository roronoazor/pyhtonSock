
import socket
import re

HOST = "localhost"
PORT = 3000
search_username_string = '(?<=username=)([^&]*)(?=&)?'
search_password_string = '(?<=password=)([^&]*)(?=&)?'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            request = conn.recv(1024)
            if not request:
                break
            request = str(request)
            username_in_list = re.findall(search_username_string, request)
            password_in_list = re.findall(search_password_string, request)
            print(username_in_list, password_in_list)
            print('Content = %s' % request)

            # write this data to a python file
            with open("config.py", "w+") as file:
                file.write("username: %s" % (username_in_list[0] if username_in_list else "Error"))
                file.write("\n")
                file.write("password: %s" % (password_in_list[0] if password_in_list else "Error"))

        # close the socket
        conn.close()



"""
import asyncio
import websockets
import os
import json

async def hello(websocket, path):
    credentials = await websocket.recv()
    print(f"< {credentials}")

    echo = f"Hello {credentials}!"
    # convert the string into a json object
    credentials = json.loads(credentials)

    await websocket.send(echo)
    print(f"> {echo}")

    # write the data to a file
    if os.path.isfile('credentials.json'):
        with open("credentials.json", "r+") as file:
            old_data = json.load(file)
            old_data["credentials"] = old_data.get("credentials", list())
            old_data["credentials"].append(credentials)
            file.seek(0)
            json.dump(old_data, file, indent=4, sort_keys=False)
    else:
        # just write the data to a new file
        data = dict()
        data["credentials"] = list()
        data["credentials"].append(credentials)
        with open("credentials.json", "w+") as file:
            json.dump(data, file, indent=4, sort_keys=False)


print("running")
start_server = websockets.serve(hello, "localhost", 3000)
print("socket started")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
"""