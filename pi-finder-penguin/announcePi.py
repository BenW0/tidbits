# From https://www.raspberrypi.org/forums/viewtopic.php?f=2&t=5953
# To run on startup, add the following to a script /etc/init.d/startupScript.sh:
# #! /bin/sh
#/usr/bin/python /scriptDirectoryPath/announcePi.py &
#
# Make it runnable, then update-rc.d startupScript.sh defaults

import socket, traceback, subprocess

host = ''
port = 10100
devname = "mUVe-printer-pi"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

while 1:
    try:
        message, address = s.recvfrom(8192)
        if message == 'raspberryPi?':
            try :
                msg = "raspberryPi!-" + devname + ",%s"%subprocess.check_output("ifconfig").split("\n")[1].split()[1][5:]
                print("got request! sending:%s"%msg)
                s.sendto(msg, address)
            finally :
                pass
    except (KeyboardInterrupt, SystemExit):
        raise


