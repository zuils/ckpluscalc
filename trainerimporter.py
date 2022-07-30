import csv
import re
import sys
 
class Mon:
	def __init__(self, name, level, item, mon, move1, move2, move3, move4):
		self.name = name
		self.level = level
		self.item = item
		self.mon = mon
		self.move1 = move1
		self.move2 = move2
		self.move3 = move3
		self.move4 = move4
 
pokemon = []
 
def parse_move(string):
	if string=='Ancientpower':
		string = 'Ancient Power'
	elif string=='Bubblebeam':
		string = 'Bubble Beam'
	elif string=='Conversion2':
		string = 'Conversion 2'
	elif string=='Double Edge':
		string = 'Double-Edge'
	elif string=='Dragonbreath':
		string = 'Dragon Breath'
	elif string=='Dynamicpunch':
		string = 'Dynamic Punch'
	elif string=='Extremespeed':
		string = 'Extreme Speed'
	elif string=='Faint Attack':
		string = 'Feint Attack'
	elif string=='Hi Jump Kick':
		string = 'High Jump Kick'
	elif string=='Lock On':
		string = 'Lock-On'
	elif string=='Mud Slap':
		string = 'Mud-Slap'
	elif string=='Poisonpowder':
		string = 'Poison Powder'
	elif string=='Psychic M':
		string = 'Psychic'
	elif string=='Selfdestruct':
		string = 'Self-Destruct'
	elif string=='Softboiled':
		string = 'Soft-Boiled'
	elif string=='Solarbeam':
		string = 'Solar Beam'
	elif string=='Sonicboom':
		string = 'Sonic Boom'
	elif string=='Thunderpunch':
		string = 'Thunder Punch'
	elif string=='Thundershock':
		string = 'Thunder Shock'
	elif string=='Vicegrip':
		string = 'Vise Grip'
	return string.replace('(', '').replace(')', '')
 
def parse_trainer(string):
	x = string.split(" ")
	return x[0]+' '+x[3].capitalize()
 
def main():
	output = ''
	prior = 'First'
	path = 'Up to Lance - Trainers.csv'
	o_path = 'src/js/data/sets/gen2.js'
	with open(path) as f:
		reader = csv.DictReader(f)
		for row in reader:
			if row['Trainer']:
				t_name = parse_trainer(row['Trainer'])
			if row['Pokemon']:
				if row['Level'] != '1':
					pokemon.append(Mon(t_name,row['Level'],row['Item'],row['Pokemon'],parse_move(row['Move 1']),parse_move(row['Move 2']),parse_move(row['Move 3']),parse_move(row['Move 4'])))
	pokemon.sort(key=lambda x: x.mon, reverse=False)
	output = output+'var SETDEX_GSC = {'
	for elements in pokemon:
		if prior == 'First':
			output = output+'"'+ elements.mon+'":{'
			prior = elements.mon
		elif prior != elements.mon:
			output = output+'},"'+ elements.mon+'":{'
			prior = elements.mon
		else:
			output = output+','
		#add stuff here
		output = output+('"'+elements.name+'":{"level":'+elements.level+',"item":"'+elements.item+'","moves":[')
		if elements.move1 != '':
			output = output+'"'+elements.move1+'"'
		if elements.move2 != '':
			output = output+',"'+elements.move2+'"'
		if elements.move3 != '':
			output = output+',"'+elements.move3+'"'
		if elements.move4 != '':
			output = output+',"'+elements.move4+'"'
		output = output+']}'
 
	output = output+'}};'
	with open(o_path, 'w') as f:
		f.write(output)
			#var SETDEX_GSC = {"Aerodactyl":{"OU Standard":{"level":100,"item":"Leftovers","moves":["Earthquake","Hidden Power Rock","Wing Attack","Fire Blast"]},"OU Curse":{"level":100,"item":"Leftovers","moves":["Curse","Earthquake","Hidden Power Rock","Substitute"]},
			#"Substitute"]},"OU Defensive":{"level":100,"item":"Leftovers","moves":["Reflect","Rest","Whirlwind","Hidden Power Rock"]}},"Aipom":{"OU Baton Pas
			#"]}}};
 
if __name__ == '__main__':
	main()
 
