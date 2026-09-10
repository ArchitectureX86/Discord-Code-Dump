from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import time
import datetime
import psutil

client_id = "1546844285645627542"
RPC = Presence(client_id)
RPC.connect()

while True:
    print("Getting cpu")
    cpu = f"{psutil.cpu_percent(interval=None)}%"
    print("Got cpu")

    print("Getting ram")
    mem = f"{psutil.virtual_memory().percent}%"
    print("Got ram")
# Show as "Playing"
    RPC.update(
            state=".",
            details=f"Cpu: {cpu} / Ram: {mem}",
            name=".",
        )
    print("des q-dos")

    time.sleep(5)
