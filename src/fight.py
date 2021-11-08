import random


def attack(nb_attack, to_hit, to_wound, enemy_rend, damage):
	attack_hit = 0
	for attack in range(nb_attack):
		if random.randint(1,6) > to_hit:
			attack_hit += 1
	return attack_hit

print(attack(3, 3, 0, 0, 0))