import sys
import glob
import serial

def serialPorts():
    if sys.platform.startswith('win'):
        ports =['COM%s' % (i+1) for i in range(256)]
    elif sys.platform.startswith('linux'):
        ports =glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported Platform')

    result = []
    for port in ports:
        try:
            s= serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    
    return result

if __name__ == '__main__':
    print(serialPorts())
