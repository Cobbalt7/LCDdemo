import serial
import serial.tools.list_ports
import datetime
import time

portlist=serial.tools.list_ports.comports()

for i in range(0, len(portlist)):
    print("%d. "% (i+1) +portlist[i].device)
option=int(input("Choose one option: "))
port=portlist[option-1].device
print(port)
s=serial.Serial(port, 9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=None)
try:
    s.isOpen()
except:
    print("Error in opening port")
    exit()
out=''
userinput=''
dateFormat='{:%H:%M:%S%z}'
dateString=''
try:
    while 1:
        userinput=input(">> ").upper()
        if userinput=="EXIT":
            s.close()
            exit()
        elif userinput=="HELP":
            f=open("help.txt", "r", encoding="utf-8")
            print(f.read())
            continue
        elif userinput !='':
            if(userinput=="TIME"):
                dateString=dateFormat.format(datetime.datetime.now())
            userinput+=dateString+'\0'
            s.write(userinput.encode())
        time.sleep(1)
        while s.inWaiting() > 0:
            out += s.read(1).decode()
        if out != '':
            print(">> " + out)
        out=''
except Exception as e:
    print(e)