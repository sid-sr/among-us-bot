'''
Author: Siddharth Sriraman
Some constants to print for message events on the server.
'''

# Command names:
trigger = '**'
add_point = 'add point '
win_com = 'win '
loss_com = 'loss '
help_com = 'help'
map_com = 'map'
map_msg = "Here's the default map!"
clear_com = 'clear lb'
lb_com = 'leaderboard'
reset_msg = 'Leaderboard has been reset!'

len_ap = len(add_point)
len_ap_win = len(win_com)
len_ap_loss = len(loss_com)
len_trigger = len(trigger)

# Messages/Responses.

error_message = ':frowning: An error has occured. Try again later.'
success_message = '''
Point update for {}: {}/{} -> {}/{} point(s)
(this is <total wins : total games played> ratio)
'''
help_message = '''
```
Hi {}!

I track Among Us game stats like player wins, leaderboards, visualisations etc.
You can add impostor game wins to the server to track the best player/other stats over time.

Basic usage:
• Each command starts with ** trigger.
• **win <user_name>             --	Add 1 point to given server member for an Impostor win
• **loss <user_name>            --	Add 1 point to given server member for an Impostor defeat.
• **leaderboard                 --	Display current leaderboard.
• **clear lb                    --    Clear current leaderboard.
• **map                         --    Display default map.
```
'''

leaderboard = '''
```
Current Leaderboard:
Based on ratio of games won as Impostor to games played as Impostor.

'''