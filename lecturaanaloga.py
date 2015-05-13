#lectura de datos por canal 0
#pcf pcf8591 direccion 0x48
import time
import smbus

bus = smbus.SMBus (1)

print ("Read the A/D")
print ("crtl c to stop")
bus.write_byte(0x48, 0x40) #dispositivo y canal analogo

while True: #do forever
        reading = bus.read_byte(0x48) #read A/D
        voltaje = reading * (3.3/255)
        pH = voltaje * (14.0/3.2)
        print (pH)
        time.sleep(1)
#hola
