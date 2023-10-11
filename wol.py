from threading import Timer
from wakeonlan import send_magic_packet
from data import Device
from config import config

timers = {}

def wol(deviceName):
    global attempts
    device : Device = Device.get(Device.name == deviceName)
    attempts = 0
    # job already running
    if timers.get( device.name ) is not None:
        return

    def timerfunc():
        global attempts
        if attempts > config.get("MaxWolAttempts"):
            return # no use

        if device.state == False:
            send_magic_packet( device.mac )
            attempts = attempts + 1
            timers.update({ device.name: Timer( 40, timerfunc ) })
            return
        
        timers.pop( device.name )

    timerfunc()
