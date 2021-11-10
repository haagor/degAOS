import random
import numpy
import matplotlib.pyplot as plt


weapon = {
	'endringmaster_aethercannon': 	[1,3,2,2,-3],
	'endringmaster_suitweapon': 	[6,3,3,1,1],
	'endringmaster_gaze': 			[1,3,2,1,-3],
	'thunderers_aethershot':		[2,3,4,1,1],
	'thunderers_double':			[4,3,4,1,1],
	'thunderers_fumigator':			[3,3,3,1,1],
	'thunderers_aethercannon':		[1,4,2,2,-3],
	'thunderers_mortar':			[1,4,3,0,-3],
	'skywardens_skypike':			[2,4,3,1,-3],
	'skywardens_gun':				[1,4,5,0,1],
	'skywardens_skyhook':			[1,4,3,2,3],
	'skywardens_drill':				[2,3,3,1,-3]
}

# damage : negate damage for dice
def attack(nb_attack, to_hit, to_wound, rend, damage, enemy_save):
	attack_hit = 0
	for i in range(nb_attack):
		if roll(6) >= to_hit:
			attack_hit += 1
	attack_wound = 0
	for i in range(attack_hit):
		if roll(6) >= to_wound:
			attack_wound += 1
	for i in range(attack_wound):
		if roll(6) - rend >= enemy_save:
			attack_wound -= 1
	total_damage = 0
	for i in range(attack_wound):
		if damage < 0:
			dgt = roll(-damage)
		else:
			dgt = damage
		total_damage += dgt
	return total_damage

def roll(dice):
	return random.randint(1,dice)

def degats(weapons, enemy_save):
	dgts = 0
	for w in weapons:
		n = w.split('*')[0]
		if n.isdigit():
			for i in range(int(n)):
				dgts += attack(*weapon[w.split('*')[1]], enemy_save)
		else:
			dgts += attack(*weapon[w], enemy_save)
	return dgts

def endringmaster_plot(nb_try):
	wounds = []
	for i in range(nb_try):
		wounds.append(degats(
			[
			'endringmaster_aethercannon',
			'endringmaster_suitweapon',
			'endringmaster_gaze',
			],
			6))

	plt.boxplot(wounds)
	plt.title('Endringmaster')
	plt.show()

def thunderers_plot(nb_try):
	wounds = []
	for i in range(nb_try):
		wounds.append(degats(
			[
			'thunderers_aethershot',
			'thunderers_double',
			'thunderers_fumigator',
			'thunderers_aethercannon',
			'thunderers_mortar',
			],
			6))

	plt.boxplot(wounds)
	plt.title('Thunderers')
	plt.show()

def skywardens_plot(nb_try):
	wounds = []
	for i in range(nb_try):
		wounds.append(degats(
			[
			'7*skywardens_skypike',
			'7*skywardens_gun',
			'thunderers_fumigator',
			'skywardens_skyhook',
			],
			6))

	plt.boxplot(wounds)
	plt.title('Skywardens')
	plt.show()

skywardens_plot(100000)