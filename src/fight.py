import random
import numpy
import matplotlib.pyplot as plt


# damage : negate damage for dice
def attack(nb_attack, to_hit, to_wound, rend, enemy_save, damage):
	attack_hit = 0
	for i in range(nb_attack):
		if roll(6) > to_hit:
			attack_hit += 1
	attack_wound = 0
	for i in range(attack_hit):
		if roll(6) > to_wound:
			attack_wound += 1
	for i in range(attack_wound):
		if roll(6) - rend > enemy_save:
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

def endringmaster_round_var1(enemy_save):
	aethercannon = attack(1,3,2,2,enemy_save,-3)
	suit_weapon = attack(6,3,3,1,enemy_save,1)
	gaze = attack(1,3,2,1,enemy_save,-3)
	return aethercannon + suit_weapon + gaze

def endringmaster_plot(nb_try):
	wounds = []
	for i in range(nb_try):
		wounds.append(endringmaster_round_var1(6))

	plt.boxplot(wounds)
	plt.title('Endringmaster')
	plt.show()

def thunderers_round_var1(enemy_save):
	aethershot = attack(2,3,4,1,enemy_save,1)
	double = attack(4,3,4,1,enemy_save,1)
	fumigator = attack(3,3,3,1,enemy_save,1)
	aethercannon = attack(1,4,2,2,enemy_save,-3)
	mortar = attack(1,4,3,0,enemy_save,-3)
	return aethershot + double + fumigator + aethercannon + mortar

def thunderers_plot(nb_try):
	wounds = []
	for i in range(nb_try):
		wounds.append(thunderers_round_var1(6))

	plt.boxplot(wounds)
	plt.title('Thunderers')
	plt.show()

def skywardens_round_var1(enemy_save, nb_unit):
	skypike = 0
	for i in range(nb_unit):
		skypike += attack(2,4,3,1,enemy_save,-3)
	gun = attack(1,4,5,0,enemy_save,1)
	skyhook = attack(1,4,3,2,enemy_save,3)
	drill = attack(2,3,3,1,enemy_save,-3)
	return skypike + gun + skyhook + drill

def skywardens_plot(nb_try):
	wounds = []
	for i in range(nb_try):
		wounds.append(skywardens_round_var1(6, 7))

	plt.boxplot(wounds)
	plt.title('Skywardens')
	plt.show()

skywardens_plot(100000)