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


endringmaster_plot(100000)