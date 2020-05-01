<p align="center">
  <img width="460" height="300" src="https://steamcdn-a.akamaihd.net/steam/apps/945360/header.jpg?t=1581973789">
</p>

# Among Us Discord Bot
---
A simple Discord bot written in Python to track stats of Among Us matches. <br>
Still a work in progress right now.

## Usage:
---
To contribute/run the bot on your own server:

* Run ```pip install requirements.txt```
* Set ```DISCORD_TOKEN``` and ```DISCORD_GUILD``` in .env-sample and rename the file to .env
* Run ```python bot.py```
* If successful, server info and console logging will start on terminal.

## Logs:
---
* v1.1 using decorators for all functions
* v1.2 uses subclass that inherits discord.Client and img folder

## TODO:

- [X] Add basic functionality
- [X] Add help info
- [ ] Work on matplotlib
- [X] Add leaderboard
- [X] Switch code to subclasses
