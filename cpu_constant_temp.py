import time

TEMP_FILE = "/sys/class/thermal/thermal_zone0/temp"

while True:
    raw = open(TEMP_FILE).read()
    millidegrees = int(raw)
    celsius = millidegrees / 1000

    print(f"CPU temp: {celsius:.1f} °C")

    time.sleep(1)
