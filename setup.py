import websockets
import asyncio

port = 7890
ip = "172.19.2.66"
print(f"server listening to {port}")


file = open("store.txt", "w")


async def echo(websocket, path):
    print("A client just connected")
    print(path)
    try:
        async for message in websocket:
            print("recieved message from client" + message)
            await websocket.send(message)
            file.write(message + "\n\n")
    except websockets.exceptions.ConnectionClosed as e:
        print("a client just disconnected")
        file.close()


start_server = websockets.serve(echo, ip, port)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
