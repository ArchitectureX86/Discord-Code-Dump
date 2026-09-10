import pypresence
from pypresence import Presence
from pypresence.types import ActivityType, StatusDisplayType
import time
import psutil
import random

client_id = "1546844285645627542"
RPC = Presence(client_id)
RPC.connect()

while True:
# Show as "Playing"
    RPC.update(
            state="Doin' cool stuff.",
            details="Making my own Rich Presence with pypresence!",
            name=f"{random.random()} eggs in my barn.",
        )

    print("des news")

    time.sleep(15)
