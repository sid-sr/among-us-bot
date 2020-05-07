# Among Us Discord Bot
A simple Discord bot written in Python to track stats of Among Us matches. <br>
Still a work in progress right now.

## Usage:
To contribute/run the bot on your own server:

* Run ```pip install requirements.txt```
* Set ```DISCORD_TOKEN``` and ```DISCORD_GUILD``` in .env-sample and rename the file to .env
* Create an empty data.pkl file for saving data.
* Run ```python bot.py```
* If successful, server info and console logging will start on terminal.

## Logs:
* v1.1 using decorators for all functions
* v1.2 uses subclass that inherits discord.Client and img folder
* v1.3 added pickling to save data in case of server restart

## TODO:

- [X] Add basic functionality
- [X] Add help info
- [ ] Work on matplotlib
- [X] Add leaderboard
- [X] Switch code to subclasses
