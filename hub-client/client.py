import asyncio
import sys
import websockets

async def main():
    mac_address = "7C-21-4A-78-D3-18"
    url = "ws://localhost:8080/websocket"

    while True:
        try:
            async with websockets.connect( url ) as connection:
                await connection.send( mac_address )
                
                print( "connected" )
                
                while True:
                    msg = await connection.recv()
                    print( msg )
        except ConnectionRefusedError:
            print( "cannot connect" )
            await asyncio.sleep( 5 )
        except Exception as e:
            print( f"connection error: {e}" )
            await asyncio.sleep( 5 )
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, asyncio.CancelledError ) as e:
        print( "exit" )
        sys.exit()