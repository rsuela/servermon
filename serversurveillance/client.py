import websocket
import _thread
import time

def on_message(ws, message):
    print(message)
    # if message.lower() =='yolo':
        # ws.close()

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        print('1')
        # for i in range(3):
            # time.sleep(1)
        ws.send("hostname:Wakenaiz,ip:192.168.1.20,os:Windows 10 Pro")
        # print('2')
        # time.sleep(1)
        # ws.close()
        # print("thread terminating...")
    # print('4')
    _thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8000",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()