import websocket
import sys

isPython27 = False

if '2.7' in sys.version:
    python27 = True

import time
import platform
import socket
import psutil
import uuid
from subprocess import Popen, PIPE, STDOUT
import re

if python27:
    print("Detected python 2.7")
    from _winreg import *
    from thread import *
else:
    from _winreg import *
    from _thread import *

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def get_software_list():
    software_list = "{'openssl':'%s','java':'%s'}"%(get_openssl_version(),get_java_version())
    print("Sulodz")
    return software_list
    
def on_open(ws):
############## SOFTWARE LIST ###################
    def get_openssl_version():
        result = ""
        try:
            version = Popen("openssl version", stdout=PIPE, stderr=STDOUT)
            result = str(version.stdout.readlines()[0].decode('ascii'))
            regex_result = re.search('OpenSSL (.*)  ', result)
            result = regex_result.group(1)
        except:
            pass
        return result
        
    def get_java_version():
        result = ""
        try:
            version = Popen("java -version", stdout=PIPE, stderr=STDOUT)
            result = str(version.stdout.readlines()[0]).split("version")[-1]
            regex_result = re.search('"(.*)"', result)
            result = regex_result.group(1)
        except:
            pass
        return result
        
    def get_registry_value(reg_path, target, permFlag=False):
        result = ""
        try:
            perm = (KEY_WOW64_64KEY | KEY_ALL_ACCESS) if permFlag else KEY_ALL_ACCESS
            reg_key = OpenKey(HKEY_LOCAL_MACHINE, "%s"%(reg_path), 0, perm)
            result = QueryValueEx(reg_key, target)
        except:
            pass
            # print('WINDOWS ERROR: No permission to access registry')
            # pass
        # except FileNotFoundError:
            # print('The target %s was not found in the registry'%(reg_path + "::" + target))
            # pass
        return result

    def get_ams_product():
        logix = get_registry_value(r'SOFTWARE\WOW6432Node\Logix', 'ProductVersion', False)
        EPM = get_registry_value(r'SOFTWARE\WOW6432Node\NCR\PreferenceManager', 'ProductVersion', False)
        Broker = get_registry_value(r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\AMS Brokers', 'DisplayVersion', False)
        UE = get_registry_value(r'SOFTWARE\NCR\AMS', 'ProductVersion', False)
        
        all_products = []
        
        if logix:
            all_products.append("'logix':'%s'"%(logix[0]))
            
        if EPM:
            all_products.append("'epm':'%s'"%(EPM[0]))
        
        if Broker:
            all_products.append("'broker':'%s'"%(Broker[0]))
            
        if UE:
            all_products.append("'ue':'%s'"%(UE[0]))
        
        found = ""
        for product in all_products:
            found = found + product + ","
        
        # all_products = "%s,%s,%s,%s" %(logix[0],EPM[0],Broker[0],UE[0])
        if found:
            found = found[0:len(found)-1]
        print(found)
        return found
    
############# END SOFTWARE LIST ################

    def get_software_list():
        software_list = []
        
        openssl = get_openssl_version()
        ams = get_ams_product()
        java = get_java_version()
        
        if openssl:
            software_list.append("'openssl':'%s'"%(openssl))
        
        if java:
            software_list.append("'java':'%s'"%(java))
            
        if ams:
            software_list.append(get_ams_product())
            
        found = "{"
        for software in software_list:
            found = found + software + ","
            
        if len(found) > 1:
            found = found[0:len(found)-1] + "}"
        else:
            found = "{}"
        
        print(found)
        # software_list = "{'openssl':'%s','java':'%s',%s}"%(get_openssl_version(),get_java_version(),get_ams_product())
        return found

    def run(*args):
        linux_sys = "'%s %s'}"%(platform.linux_distribution()[0],platform.linux_distribution()[1])
        raw_mem = str(psutil.virtual_memory().total >> 20).replace('L','')
        memory = raw_mem[:2] + " GB" if len(raw_mem) == 5 else raw_mem[:1]
        mac = str(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])).upper()
        send_msg = "{'name' : " + "'%s'"%platform.uname()[1] + "," \
                 "'processor' : " + "'%s'"%(platform.processor())+ "," \
                 "'softwares' : " + "%s"%(get_software_list()) + ","\
                 "'memory' : " + "'%s'"%memory + "," \
                 "'arch' : " + "'%s'"%(platform.architecture()[0]) + "," \
                 "'ipaddress' : " + "'%s'"%(socket.gethostbyname(platform.uname()[1])) + "," \
                 "'mac' : " + "'%s'"%mac + "," \
                 "'system' : " + "'%s %s'}"%(platform.uname()[0],platform.uname()[2]) if "windows" in platform.platform().lower() else linux_sys
        print(send_msg)
        ws.send(send_msg)

    start_new_thread(run, ())


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Error please specify the servermon master hostname")
        sys.exit(1)
    #endif
    
    servermon = sys.argv[1]
    
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://%s/connect"%(servermon),
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()