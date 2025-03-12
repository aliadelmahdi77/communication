#!/usr/bin/env python3
"""
Microcontroller Communication using PySerial



import serial
import time

def main():

    serial_port = '/dev/ttyACM0'
    baud_rate = 9600 # Must match the baud rate set in the Microcontroller sketch
    timeout = 2  # seconds

    # Attempt to open the serial connection
    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=timeout)
        print(f"Connected to {serial_port} at {baud_rate} baud.")
    except Exception as e:
        print(f"Failed to connect on {serial_port}. Error: {e}")
        return

    # Allow time for the Microcontroller to reset (common when opening a new serial connection)
    time.sleep(2)

    # Define the message to send
    message = "Hello, Microcontroller!\r\n"
    print("Sending message:", message.strip())

    # Send the message to the Microcontroller
    ser.write(message.encode('utf-8'))

    # Wait a moment to receive the response
    time.sleep(1)

    # Read the response from the Microcontroller
    response = ser.readline().decode('utf-8').strip()
    print("Received response:", response)

    # Close the serial connection
    ser.close()

if __name__ == '__main__':
    main()
