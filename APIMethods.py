import aiohttp
import asyncio
import requests
import json

async def getAuctionData(API_Key):
    url = f"https://api.hypixel.net/skyblock/auctions?key={API_Key}"
    iterations = requests.get(url).json()['totalPages']
    iterations -= 1
    fb = 0;
    rb = 0;
    async with aiohttp.ClientSession() as session:
        for i in range(1, iterations):
            url = f"https://api.hypixel.net/skyblock/auctions?key={API_Key}&page={i}"
            async with session.get(url) as resp:
                store = await resp.json()
                if store['success']:
                    for x in store['auctions']:
                        if "bin" in x:
                                if x['claimed'] == False:
                                    if x['item_name'] == 'Farmer Boots':
                                        if x['starting_bid'] < fb or fb == 0:
                                            fb = x['starting_bid']
                                            print(f"Found Farmer Boots with price {x['starting_bid']}")
                                    elif x['item_name'] == 'Rancher\u0027s Boots':
                                        if x['starting_bid'] < rb or rb == 0:
                                            rb = x['starting_bid']
                                            print(f"Found Rancher Boots with price {x['starting_bid']}")
                else:
                    i-=1
    print(f"Cheapest Farmer Boots found in BIN: {fb}")
    print(f"Cheapest Rancher Boots found in BIN: {rb}")
    return [fb, rb]

def getBazaarData(API_Key):
    url = f"https://api.hypixel.net/skyblock/bazaar?key={API_Key}"
    store = requests.get(url).json()
    ep = store['products']['ENCHANTED_PUMPKIN']['buy_summary'][0]['pricePerUnit']
    pp = store['products']['POLISHED_PUMPKIN']['buy_summary'][0]['pricePerUnit']
    print(f"Enchanted Pumpkin sold at bazaar: {ep}")
    print(f"Polished Pumpkin sold at bazaar: {pp}")
    return [ep, pp]

# store = asyncio.run(getAuctionData())
# getBazaarData()

