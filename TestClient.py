from websocket import create_connection
from time import sleep

ws = create_connection("ws://localhost:8889")
#ws2 = create_connection("ws://localhost:8888/join")
ws.send("CREATEROOM")
ws.send("GETROOMS")
ws.send("JOINROOM 1 Drareeg")
result = ws.recv()
print("R: %s" % result)

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


