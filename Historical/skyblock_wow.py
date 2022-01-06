import requests
import json
data = requests.get("https://api.hypixel.net/skyblock/auctions").json()
auctions = data["auctions"]
items = []
for auction in auctions:
    try:
        if auction["bin"]:
            items.append(auction)
    except KeyError:
        pass
print(items)
with open('auctions.json', 'w') as file:
    json.dump(items, file, indent=4)
