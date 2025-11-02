from ppadb.client import Client as AdbClient
import time

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

if len(devices) == 0:
    print("❌ No device connected. Check USB & Debugging!")
    quit()

device = devices[0]
print(f"✅ Connected to {device}")

WAIT_TIME = 15 # seconds between shorts
print("▶️ Auto YouTube Shorts scroller started...")

while True:
    device.shell("input swipe 500 1500 500 500 300")
    print("⬆️ Next short!")
    time.sleep(WAIT_TIME)
