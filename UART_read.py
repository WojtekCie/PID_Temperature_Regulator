import serial
import csv
import numpy as np
import matplotlib.pyplot as plt
import time


from PIL.ImageOps import expand

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM3"
ser.timeout = 1

temp_lst = []
tim_lst = []
ctr_lsc = []

try:
    ser.open()
    print("Serial port opened successfully.")
except Exception as e:
    print(f"Failed to open serial port: {e}")
    exit()

csv_file = "data.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp (ms)", "Temperature (°C)"])

    print("Start reading data...")
    plt.figure('Temerature & ControlSignal Plot')
    plt.grid(True)
    plt.xlabel('Timestamp')
    plt.axhline(y=40, color='r', linestyle='--', linewidth=0.5, label='40[°C]')
    #plt.legend()
    try:
        while True:
            line = ser.readline().decode("utf-8").strip()
            if line:
                try:
                    timestamp, temperature, controlSignal = line.split(",")
                    #print(timestamp)
                    timestamp = int(timestamp)
                    temperature = float(temperature)
                    controlSignal = float(controlSignal)
                    print(f"Timestamp: {timestamp} s, Temperature: {temperature} °C, ControlSignal: {controlSignal}")
                    writer.writerow([timestamp, temperature])
                    tim_lst.append(timestamp)
                    temp_lst.append(temperature)
                    ctr_lsc.append(controlSignal)
                    #plt.ylabel('Temperature')
                    plt.plot(tim_lst,temp_lst,color='red',label='Temperature')
                    plt.plot(tim_lst,ctr_lsc,color='blue',label='Control_Signal')
                    plt.pause(0.05)
                except ValueError:
                    print(f"Malformed data: {line}")

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Data logging stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

ser.close()
print("Serial port closed.")
plt.show()