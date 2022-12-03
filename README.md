# Discord
Discord Bots using Python

Features:
  - retrive discord messages
  - fetch all users from a server
  - fetch all roles from a server
  - fetch announcement channel messages

# Binance.py

This code uses the `requests` library to make a `GET` request to the `Binance API` endpoint for the Solana token price. It then parses the response data and extracts the Solana token price.

Next, the code uses the `Discord API` to update the bot's status with the Solana token price. It does this by making a `PATCH request` to the `Discord API` endpoint for the bot's user settings, along with the necessary authentication headers and the new bot status data.