Managing Arduino Resets
=======================
The Arduino does an excellent job of abstracting away the implementation details of a microcontroller and allowing the user to think about it as a collection of easy-to-use high-level functions.


Wait on Arduino auto-reset using pySerial
https://stackoverflow.com/questions/21073086/wait-on-arduino-auto-reset-using-pyserial

Reset Arduino from Python!

Linux: serial port, Arduino reset, avrdude
http://forum.arduino.cc/index.php?topic=39468.0

DisablingAutoResetOnSerialConnection
http://playground.arduino.cc/Main/DisablingAutoResetOnSerialConnection


http://www.codeproject.com/Articles/1012319/Arduino-Software-Reset
http://www.theengineeringprojects.com/2015/11/reset-arduino-programmatically.html
http://www.xappsoftware.com/wordpress/2013/06/24/three-ways-to-reset-an-arduino-board-by-code/
https://arduino.stackexchange.com/questions/1477/reset-an-arduino-uno-by-an-command-software
Reset command
http://forum.arduino.cc/index.php?topic=12874.0

http://playground.arduino.cc/Main/ArduinoReset

http://www.instructables.com/id/two-ways-to-reset-arduino-in-software/

<pre>
>>> import serial
>>> arduino = serial.Serial('/dev/arduino_uno',bytesize=serial.EIGHTBITS,
...                      parity=serial.PARITY_NONE,
...                      stopbits=serial.STOPBITS_ONE,
...                      timeout=1,
...                      xonxoff=0,
...                      rtscts=0
...                      )
>>> arduino.setDTR(False); sleep(1); arduino.flushInput(); arduino.setDTR(True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sleep' is not defined
>>> from time import sleep
>>> arduino.setDTR(False); sleep(1); arduino.flushInput(); arduino.setDTR(True)
>>> arduino.setDTR(False); sleep(1); arduino.flushInput(); arduino.setDTR(True)
</pre>
