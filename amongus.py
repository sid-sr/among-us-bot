'''
	Author: Siddharth Sriraman
	Class definitions and misc. functions to store data on Among Us matches.
'''
import discord
import message_info

# to return the user name without the #XXXX part at the end
def format_user_name(user_name):
	return ''.join(str(user_name).split('#')[:-1])


class AmongUsData(object):
	'''Class to store among us data of players.'''
	def __init__(self, user_list, exc=None):
		'''Initialise all scores in a dictionary (data_dict) to 0.'''
		self.data_dict = {}
		for user in user_list:
			self.data_dict[user] = [0, 0]
		if exc in self.data_dict:
			del self.data_dict[exc]

	def add_point(self, user_name, win=True):
		'''Add a point to the given user_name'''
		if user_name not in self.data_dict.keys():
			raise Exception(f'User {user_name} not found!')
		else:
			self.data_dict[user_name][0] += int(win)
			self.data_dict[user_name][1] += 1

	def reset_points(self):
		'''Reset all points to 0 for all users.
		'''
		for user in self.data_dict:
			self.data_dict[user] = [0, 0]

	def get_points(self, user_name):
		'''Return points for the given user_name
		   Returns pair of [total wins, total Impostor games]
		'''
		if user_name not in self.data_dict.keys():
			raise Exception(f'User {user_name} not found!')
		else:
			return self.data_dict[user_name]

	def get_leaderboard_data(self):
		'''Return a list of (user_name, point pair, ratio) triplets.'''
		return [[x[0], x[1], (x[1][0]/x[1][1] if x[1][1] else 0)] for x in self.data_dict.items()]

class AmongUsClient(discord.Client):
	'''Subclass to handle events without decorators'''
	def __init__(self, guild):
		super().__init__()
		# remains None if on_ready is not successful
		self.au_data = None
		self.GUILD = guild

	async def on_ready(self):
		server = discord.utils.get(self.guilds, name=self.GUILD)		
		self.au_data = AmongUsData([format_user_name(name) for name in self.users], exc=format_user_name(self.user))
		print(f'Running on server: {server.name}\nServer ID: {server.id}')
		print(f'{self.user} has connected to Discord!')
		print('\nLog: ')

	async def on_member_join(self, member):
	    await member.create_dm()
	    await member.dm_channel.send(f'Hi {member.name}, welcome to the Among Us Discord server!')

	async def on_message(self, message):
		if message.author == self.user:
			return

		# Console logging
		print("Message Received: '{}' from '{}'".format(message.content, message.author))

		user_name = format_user_name(message.author)
		if message.content[:message_info.len_trigger] == message_info.trigger:
			msg = message.content[message_info.len_trigger:]

			if msg == message_info.help_com:
				await message.channel.send(message_info.help_message.format(user_name))
			elif msg == message_info.clear_com:
				self.au_data.reset_points()
				await message.channel.send(message_info.reset_msg)					
			elif msg == message_info.map_com:
				file = discord.File("./img/map.jpg", filename="map.jpg")
				embed = discord.Embed()
				embed.set_image(url="attachment://map.jpg")
				await message.channel.send(content=message_info.map_msg, file=file, embed=embed)	
			elif msg == message_info.lb_com:
				res = ''
				lb_data = self.au_data.get_leaderboard_data()
				lb_data.sort(key=lambda x: x[2], reverse=True)
				ratios = [x[2] for x in lb_data]
				ranks = [ratios.index(x[2]) for x in lb_data]
				
				for num, data in zip(ranks, lb_data):
					user, score, ratio = data
					res += '%2d. %-25s  --  %2d  / %2d : %.2f\n'%(num+1, user, score[0], score[1], ratio)
				res+='```'

				await message.channel.send(message_info.leaderboard + res)
			else:
				win, msg_len = 0, 0
				if msg[:message_info.len_ap_loss] == message_info.loss_com:
					win = False
					msg_len = message_info.len_ap_loss
				elif msg[:message_info.len_ap_win] == message_info.win_com:
					win = True
					msg_len = message_info.len_ap_win				
				try:
					user_to_add = msg[msg_len:]
					old_pts = self.au_data.get_points(user_to_add).copy()
					self.au_data.add_point(user_to_add, win=win)
					pts = self.au_data.get_points(msg[msg_len:])
					await message.channel.send(message_info.success_message.format(user_to_add, old_pts[0], old_pts[1], pts[0], pts[1]))
				except Exception as exc:
					print(exc)
					await message.channel.send(message_info.error_message)
