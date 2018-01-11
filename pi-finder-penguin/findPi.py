# From https://www.raspberrypi.org/forums/viewtopic.php?f=2&t=5953
# Needs python 2!

import socket

host = socket.gethostbyname(socket.gethostname())
print("Using host: %r" % host)
port = 10100

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
s.settimeout(3)
s.sendto("raspberryPi?",('<broadcast>',port))
try:
    while 1:
        message, address = s.recvfrom(8192)
        #print('Msg: %r, addr: %r'%(message, address))
        if 'raspberryPi!' in message:
            try :
                print('Device Name: %r'%message.split(',')[0][13:])
                print('IP Address: %r'%message.split(',')[1])
            except :
                print("Error parsing response: %r" % message)
except (KeyboardInterrupt, SystemExit):
    raise
except:
    print('--Finish--')

