
import telnetGPIO as tg
import time
import sys

if len(sys.argv) != 5:
    raise Exception("Not enough input arguments")

msgBroker = sys.argv[1]
msgBrokerPort = sys.argv[2]
serviceName = sys.argv[3]
gpioHost = sys.argv[4]

conn = tg.telnetGPIOHandler(msgBroker, msgBrokerPort, serviceName, gpioHost)
conn.initializeConn()

while(1 == 1):
    print(conn.newState)
    conn.read()
    conn.updateBinary()

    if(conn.newState != conn.oldState):
        conn.writeChange()

    time.sleep(.1)
