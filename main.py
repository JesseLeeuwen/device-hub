from data import connect, close
from server import serveThreaded
from window import openWindow

connect()

serveThreaded()
openWindow()

# clean up
close()