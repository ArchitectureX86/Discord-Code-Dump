from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import time
import psutil

while True:
    print("Getting CPU usage and setting 'cpu' variable to CPU usage")
    cpu = psutil.cpu_percent(interval=None)

    print("Printing 'cpu'")
    print(f"{cpu}%")
    cpu = f"Cpu = {cpu}%"

    print("VRAM time.")
    vmem = psutil.virtual_memory()

    print("Printing 'vmem'")
    print(f"{vmem.percent}%")
    vmem = f"Ram = {vmem.percent}%"

    client_id = "1546844285645627542"
    RPC = Presence(client_id)
    RPC.connect()

# Show as "Playing"
    RPC.update(
            state="Doin' cool stuff.",
            details=cpu,
            name=vmem,
            # details=f"Cpu:{psutil.cpu_percent(interval=None)}%",
            # name=f"Ram:{psutil.virtual_memory().percent}%",
        )
    print("des news")

    time.sleep(15)
