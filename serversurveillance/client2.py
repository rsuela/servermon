import websocket
import _thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send("{'name' : 'Wakenaizzz'," \
                 "'processor' : 'processor'," \
                 "'memory' : 'memory'," \
                 "'arch' : 'arch'," \
                 "'ipaddress' : '192.168.1.22'," \
                 "'mac' : 'mac'," \
                 "'system' : 'Windows 10 Pro'}")
                  
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8000/connect",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()