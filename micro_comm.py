#!/usr/bin/env python3
"""
Arduino Communication using PySerial

This script opens a serial connection to an Arduino, sends a message, and prints the Arduino's response.

Usage:
1. Connect your Arduino to the Raspberry Pi via USB.
2. Upload a compatible Arduino sketch (see guide below).
3. Install PySerial: pip install pyserial
4. Adjust the serial port and baud rate if needed.
5. Run this script: python3 arduino_comm.py
"""

import serial
import time

def main():
    # Serial port settings: change '/dev/ttyUSB0' if your device is different (e.g., '/dev/ttyACM0' or '/dev/serial0')
    serial_port = '/dev/ttyUSB0'
    baud_rate = 9600 # Must match the baud rate set in the Arduino sketch
    timeout = 2  # seconds

    # Attempt to open the serial connection
    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=timeout)
        print(f"Connected to {serial_port} at {baud_rate} baud.")
    except Exception as e:
        print(f"Failed to connect on {serial_port}. Error: {e}")
        return

    # Allow time for the Arduino to reset (common when opening a new serial connection)
    time.sleep(2)

    # Define the message to send
    message = "Hello, Arduino!\r\n"
    print("Sending message:", message.strip())

    # Send the message to the Arduino
    ser.write(message.encode('utf-8'))

    # Wait a moment to receive the response
    time.sleep(1)

    # Read the response from the Arduino
    response = ser.readline().decode('utf-8').strip()
    print("Received response:", response)

    # Close the serial connection
    ser.close()

if __name__ == '__main__':
    main()
