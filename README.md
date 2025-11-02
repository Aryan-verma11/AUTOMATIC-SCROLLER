# AUTOMATIC-SCROLLER
Auto Scroller using Python + ADB is a lightweight automation tool that simulates smooth scrolling on Android devices. It uses Python to send ADB swipe commands with timed intervals, allowing continuous, hands-free scrolling on apps like Instagram, Twitter, or YouTube.


🌀 Auto Scroller using Python + ADB
📖 Overview

This project is an Auto Scroller tool built using Python, ADB (Android Debug Bridge), and the time module.
It automates screen scrolling on Android devices — perfect for apps like Instagram, Twitter, YouTube, or any app where you need continuous scrolling without manual input.

⚙️ How It Works

ADB (Android Debug Bridge) acts as a communication bridge between your computer and Android device.
It allows Python to send scroll commands directly to the connected device.

Python script sends a “swipe” command using ADB to simulate finger scrolling on the touchscreen.

Time module introduces a delay between each scroll to control the scrolling speed.

The script runs continuously (or for a specified number of scrolls) until you stop it.

🧩 Features

✅ Automated smooth scrolling on Android
✅ Adjustable scroll delay and distance
✅ Works over USB or wireless ADB connection
✅ Lightweight and easy to modify

🧱 Requirements

Before running the project, make sure you have:

Python 3.7+ installed

ADB (Android Debug Bridge) installed and added to your PATH

A USB-connected or wirelessly connected Android device with USB Debugging enabled

🪄 Setup Instructions

Install ADB

Download from Google’s Platform Tools

Extract it and add the folder path (e.g. C:\platform-tools) to your System PATH

Enable USB Debugging on Android

Go to:
Settings → About Phone → Tap Build Number 7 times → Developer Options → Enable USB Debugging

Connect Your Device

adb devices


If you see your device listed, you’re ready to go.

Install Dependencies
No external libraries are needed except built-in Python modules (os, time).

Run the Script

python autoscroll.py

🧠 Example Code
import os
import time

# Set scroll coordinates (start_x, start_y, end_x, end_y)
# Adjust based on your device screen size
start_x, start_y = 500, 1500
end_x, end_y = 500, 500

# Set scroll delay (seconds)
delay = 3

while True:
    # Perform scroll using ADB swipe command
    os.system(f"adb shell input swipe {start_x} {start_y} {end_x} {end_y}")
    print("Scrolled one step ⬆️")
    
    # Wait before next scroll
    time.sleep(delay)

🧰 Customization

Change scroll speed: Modify the delay variable.

Change scroll distance: Adjust the swipe coordinates.

Limit scroll count: Replace the infinite loop with a for loop and a counter.

🚀 Future Improvements

Add random delay intervals for human-like scrolling

Add start/stop GUI using Tkinter

Integrate with image recognition to detect scroll end

📜 License

This project is open-source under the MIT License — free to use, modify, and share.