import webview

from config import config

port = str( config.get("PORT") )
window = webview.create_window( "overview", url="http://127.0.0.1:" + port, height=620, text_select=True )

def openWindow():
    webview.start( debug=True )
