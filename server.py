from datetime import datetime
import json
from threading import Thread

from bottle import Bottle, template, run, static_file, request, response
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket

from data import Device
import data
from config import config

app = Bottle()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static/')

@app.get('/')
def index():
    devices = []
    for device in Device.select():
        devices.append( device.toJson() )

    return template('index', devices = devices )

@app.get('/devices')
def listDevices():
    query : str = request.query.filter.upper() or ""

    devices = []
    result = Device.select().where( 
        Device.name.contains( query ) or Device.mac.contains( query ) )
    
    device : Device = None
    for device in result:
        devices.append( device.toJson() )

    response.content_type = "application/json"
    return json.dumps( devices )

@app.post('/devices/<device>/startup')
def startDevice(device):
    from wol import wol
    wol( device )
    return 'OK'

@app.delete('/devices/<device>/remove')
def removeDevice(device):
    Device.get( Device.name == device ).delete_instance()
    return "OK"

@app.post('/devices/new')
def newDevice():
    name = request.forms.get('device-name')
    mac = request.forms.get('device-mac')
    Device.create( name = name, mac = mac, state = False, lastOnline = datetime(1970,1,1) )
    return "OK"

@app.get('/websocket', apply=[websocket])
def connect(ws):
    mac = ws.receive()
    device : Device = Device.get( Device.mac == mac )
    print(f"new connection {device.name}")

    if device is None:
        return # refuse connection

    device.lastOnline = datetime.now()
    device.state = True
    device.save()

    while True:
        msg = ws.receive()
        if msg is None:
            break

    print(f"closed connection {device.name}")

    device.lastOnline = datetime.now()
    device.state = False
    device.save()

# --------------------------------
def serveThreaded():
    thread = Thread(target = serve, daemon=True)
    thread.start()

def serve():
    global app
    run(app, host='0.0.0.0', port=config.get("PORT"), debug=config.get("Debug"), server=GeventWebSocketServer)


if __name__ == "__main__":
    data.connect()
    serve()
    data.close()