
#
import serial
import datetime
from mintsXU4 import mintsSensorReader as mSR
from mintsXU4 import mintsDefinitions as mD
import time
import sys

dataFolder    = mD.dataFolder
ozonePort     = mD.ozonePort


def main(portNum):
    if(len(nanoPorts)>0):

        ser = serial.Serial(
        port= nanoPorts[portNum],\
        baudrate=2400,\
        parity  =serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
        timeout=0)

        print(" ")
        print("Connected to: " + ser.portstr)
        print(" ")

        #this will store the line
        line = []

        while True:
            try:
                for c in ser.read():
                    line.append(chr(c))
                    if chr(c) == '\n':
                        dataString     = (''.join(line)).replace("\n","").replace("\r","")
                        dateTime  = datetime.datetime.now()
                        print(dataString)
                        TB108LWrite(dataString,dateTime)
                        line = []
                    break
            except:
                print("Incomplete String Read")
                line = []
        ser.close()


if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    print("Monitoring Ozone Sensor on port: {0}".format(ozonePort))
    main(ozonePort)