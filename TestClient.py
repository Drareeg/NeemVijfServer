from websocket import create_connection
from time import sleep

ws = create_connection("ws://localhost:8888")
#ws2 = create_connection("ws://localhost:8888/join")
ws.send("Hello, World")
print("Sent")
result = ws.recv()
print("Received '%s'" % result)
sleep(6)

#
# ws2 = create_connection("ws://localhost:8888/joinServer")
# ws2.send("Hello, World22222")
# print("Sent")
# result =  ws2.recv()
# print("Received '%s'" % result)
#
# result =  ws.recv()
# print("Received '%s'" % result)


ws.close()


