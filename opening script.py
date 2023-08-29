import serial

# Open the serial port (change the port number to the port of your arduino)
port = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

#code to open and close the jar
command = input("open or close the jar?: ")

if command=="open":
    port.write(bytes("open", 'utf-8'))
elif command=="close":
    port.write(bytes("close", 'utf-8'))



