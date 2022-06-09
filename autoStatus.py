from random import choice
import requests
from time import sleep

url = "https://ptb.discordapp.com/api/v6/users/@me/settings"

sleepTime=99999999999
token=""
statuses=["FAILURE"]
with open("/root/discordStatus/time", "r") as timefile:
    sleepTime=int(timefile.read())
with open("/root/discordStatus/.token", "r") as f:
    token = f.read().strip("\n")

print(sleepTime)

while True:
    st = requests.get("https://raw.githubusercontent.com/Un10ck3d/Un10ck3d/main/discordStatus.txt")
    statuses = st.text.split("\n")
    print(statuses)
    stat=choice(statuses)
    content = {
        "custom_status": {
            "text": stat,
            "expires_at": None,
            "emoji_id": None,
            "emoji_name": None
        }
    }
    rq = requests.patch(url, headers={"authorization": token}, json=content)
    print("setting status to:", stat)
    sleep(sleepTime)
