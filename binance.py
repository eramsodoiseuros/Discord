import requests

# Binance API endpoint for Solana token price
price_endpoint = "https://api.binance.com/api/v3/ticker/price?symbol=SOL-7E5"

# Discord bot token
bot_token = "YOUR_BOT_TOKEN"

# Get the Solana token price from the Binance API
response = requests.get(price_endpoint)
price_data = response.json()
sol_price = float(price_data["price"])

# Use the Solana token price to update the Discord bot status
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bot {bot_token}"
}

payload = {
    "status": "online",
    "activity": {
        "name": f"Solana token price: {sol_price}",
        "type": "WATCHING"
    }
}

status_endpoint = "https://discordapp.com/api/v6/users/@me/settings"
response = requests.patch(status_endpoint, headers=headers, json=payload)
