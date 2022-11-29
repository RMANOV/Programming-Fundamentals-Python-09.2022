

# On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for your party.
# On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a single space in the following format: 
# "{hero name} {HP} {MP}"
# -	HP stands for hit points and MP for mana points
# -	a hero can have a maximum of 100 HP and 200 MP
# After you have successfully picked your heroes, you can start playing the game. 
# You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given. 
# There are several actions that the heroes can perform:
# "CastSpell – {hero name} – {MP needed} – {spell name}"
# •	If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message: 
# o	"{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
# •	If the hero is unable to cast the spell print:
# o	"{hero name} does not have enough MP to cast {spell name}!"
# "TakeDamage – {hero name} – {damage} – {attacker}"
# •	Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
# o	"{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
# •	If the hero has died, remove him from your party and print:
# o	"{hero name} has been killed by {attacker}!"
# "Recharge – {hero name} – {amount}"
# •	The hero increases his MP. If it brings the MP of the hero above the maximum value (200), 
# MP is increased to 200. (the MP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} recharged for {amount recovered} MP!"
# "Heal – {hero name} – {amount}"
# •	The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100), 
# HP is increased to 100 (the HP can't go over the maximum value).
# •	 Print the following message:
# o	"{hero name} healed for {amount recovered} HP!"
# Input
# •	On the first line of the standard input, you will receive an integer n
# •	On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a space in the following format
# •	You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
# Output
# •	Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):
# "{hero name}
#   HP: {current HP}
#   MP: {current MP}"
# Constraints
# •	The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
# •	The HP/MP amounts in the commands will never be negative.
# •	The hero names in the commands will always be valid members of your party. No need to check that explicitly.

number_of_heroes = int(input())
heros_dict = {}

for _ in range(number_of_heroes):
    hero, hp, mp = input().split()
    hp = int(hp)
    mp = int(mp)
    heros_dict[hero] = {'hp': hp, 'mp': mp}

command = input()

while not command == 'End':
    command = command.split(' - ')
    action = command[0]
    hero = command[1]

    if action == 'CastSpell':
        mp_needed = int(command[2])
        spell_name = command[3]
        if heros_dict[hero]['mp'] >= mp_needed:
            heros_dict[hero]['mp'] -= mp_needed
            print(f'{hero} has successfully cast {spell_name} and now has {heros_dict[hero]["mp"]} MP!')
        else:
            print(f'{hero} does not have enough MP to cast {spell_name}!')

    elif action == 'TakeDamage':
        damage = int(command[2])
        attacker = command[3]
        heros_dict[hero]['hp'] -= damage
        if heros_dict[hero]['hp'] > 0:
            print(f'{hero} was hit for {damage} HP by {attacker} and now has {heros_dict[hero]["hp"]} HP left!')
        else:
            del heros_dict[hero]
            print(f'{hero} has been killed by {attacker}!')

    elif action == 'Recharge':
        amount = int(command[2])
        if heros_dict[hero]['mp'] + amount > 200:
            amount = 200 - heros_dict[hero]['mp']
        heros_dict[hero]['mp'] += amount
        print(f'{hero} recharged for {amount} MP!')

    elif action == 'Heal':
        amount = int(command[2])
        if heros_dict[hero]['hp'] + amount > 100:
            amount = 100 - heros_dict[hero]['hp']
        heros_dict[hero]['hp'] += amount
        print(f'{hero} healed for {amount} HP!')

    command = input()

# heros_dict = dict(sorted(heros_dict.items(), key=lambda x: (-x[1]['hp'], x[0])))
for hero, stats in heros_dict.items():
    print(hero)
    print(f'  HP: {stats["hp"]}')
    print(f'  MP: {stats["mp"]}')