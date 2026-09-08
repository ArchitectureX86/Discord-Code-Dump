from pypresence import Presence
import time

client_id = "1546844285645627542"
RPC = Presence(client_id)

RPC.connect()

RPC.update(
        state="Doin' cool stuff.",
        details="Making my own Rich Presence with pypresence!",
        name="My current state,",
    )
print("I swear it works.")
while True:
        time.sleep(15)
