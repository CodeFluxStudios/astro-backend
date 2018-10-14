# Astro Backend
This is the backend server for the astro bot. It handles user authorization and gets data from the user.

# Installation
After downloading, run **pip3 install -r requirements.txt** inside the project folder to install all dependencies. After that generate a config using **generate_config.py** In it, edit the values of *BotId* and *BotSecret* to your discord bot's ID and secret. After that you can run **main.py** to start the server. The server will be accessible under **localhost:5000**.

# Routes
Following routes are available:
- /login - Redirect the user to the discord authorization server
- /callback - Handles the authorization server's answer
- /session - Shows the current user token
- /logout - Clears the user's session
- /api/servers - Shows the user's discord guilds 
- /api/user - Shows the user's discord account information


