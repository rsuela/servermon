import websocket
import _thread
import time
import platform
import socket
import psutil
import uuid


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        linux_sys = "'%s %s'}"%(platform.linux_distribution()[0],platform.linux_distribution()[1])
        raw_mem = str(psutil.virtual_memory().total >> 20).replace('L','')
        memory = raw_mem[:2] + " GB" if len(raw_mem) == 5 else raw_mem[:1]
        mac = str(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])).upper()
        send_msg = "{'name' : " + "'%s'"%platform.uname()[1] + "," \
                 "'processor' : " + "'%s'"%(platform.processor())+ "," \
                 "'memory' : " + "'%s'"%memory + "," \
                 "'arch' : " + "'%s'"%(platform.architecture()[0]) + "," \
                 "'ipaddress' : " + "'%s'"%(socket.gethostbyname(platform.uname()[1])) + "," \
                 "'mac' : " + "'%s'"%mac + "," \
                 "'system' : " + "'%s %s'}"%(platform.uname()[0],platform.uname()[2]) if "windows" in platform.platform().lower() else linux_sys
        print(send_msg)
        ws.send(send_msg)
                  
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8000/connect",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()