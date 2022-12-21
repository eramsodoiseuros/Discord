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

This code uses `Logging in with Discord` special token - `access token` - to fetch important server infomations that the users has, such as list of servers, user roles in those servers and announcement channel messages in those servers.

# Loggin in with Discord

Logging in with Discord allows users to easily access their `Discord account` from other websites and applications. When a user logs in with Discord, they are redirected to the Discord login page, where they can enter their login credentials (`email address` and `password`).

If the login is successful, the user is redirected back to the website or application that requested the login, and a special token is issued to the website or application. This token can then be used to access the user's Discord account and perform actions on behalf of the user.

Here's a high-level overview of the login process:

  1. The user clicks on the "Log in with Discord" button on the website or application.

  2. The website or application sends a request to the Discord API to initiate the login process.

  3. The `Discord API` redirects the user to the Discord login page, where they can enter their login credentials.

  4. If the login is successful, the `Discord API` redirects the user back to the website or application and issues a special token (called an `access token`) to the website or application.

  5. The website or application can use the access token to access the user's Discord account and perform actions on behalf of the user.