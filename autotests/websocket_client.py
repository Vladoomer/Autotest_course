import asyncio
import websockets

async def client():
    url = "ws://127.0.0.1:8765"
    async with websockets.connect(url) as websocket:
        message = "Hello Server"
        print(f"Send {message}")
        await websocket.send(message)

        resp = await websocket.recv()
        print(f"Receive {resp}")

asyncio.run(client())