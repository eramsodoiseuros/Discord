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

# Fetch.py

This code attempts to retrieve a list of messages from a channel in a Discord server using the `Discord API`.
It is using the `os.getenv` function to get the value of the `API_ENDPOINT` environment variable, which is the base URL of the `Discord API`. It then constructs the URL for the `/channels/{channel_id}/messages` endpoint using the `channel_id` argument passed to the `retrieve_messages` function and the `API_ENDPOINT` environment variable.