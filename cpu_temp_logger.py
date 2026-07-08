import time                    
from datetime import datetime  

TEMP_FILE = "/sys/class/thermal/thermal_zone0/temp"  
LOG_FILE = "temp_log.csv"                            

print("Logging to", LOG_FILE, "— press Ctrl+C to stop")

while True:
    raw = open(TEMP_FILE).read()
    celsius = int(raw) / 1000
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"{timestamp},{celsius:.1f}"

    print(line)

    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

    time.sleep(1)
