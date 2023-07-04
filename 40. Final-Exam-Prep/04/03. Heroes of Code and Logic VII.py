num_heroes = int(input())
heroes = {}
for i in range(num_heroes):
    initialize = input()
    hero_name, hp_size, mana_size = initialize.split(" ")
    heroes[hero_name] = []                       # hero_name: [0->HP,1->MP]
    heroes[hero_name].append(int(hp_size))
    heroes[hero_name].append(int(mana_size))
commands = input()
while commands != "End":
    action, other = commands.split(" - ", 1)
    if action == "CastSpell":
        hero_name, mp_needed, spell_name = other.split(" - ")
        mp_needed = int(mp_needed)
        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero_name, damage, attacker = other.split(" - ")
        damage = int(damage)
        heroes[hero_name][0] -= damage
        if heroes[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
    elif action == "Recharge":
        hero_name, amount = other.split(" - ")
        amount = int(amount)
        if heroes[hero_name][1] + amount > 200:
            amount_to_max = 200 - heroes[hero_name][1]
            print(f"{hero_name} recharged for {amount_to_max} MP!")
            heroes[hero_name][1] = 200
        else:
            heroes[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")
    elif action == "Heal":
        hero_name, amount = other.split(" - ")
        amount = int(amount)
        if heroes[hero_name][0] + amount > 100:
            amount_to_max = 100 - heroes[hero_name][0]
            print(f"{hero_name} healed for {amount_to_max} HP!")
            heroes[hero_name][0] = 100
        else:
            heroes[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")
    commands = input()
for key in heroes.keys():
    if heroes[key][0] > 0:
        print(f"{key}")
        print(f"  HP: {heroes[key][0]}")
        print(f"  MP: {heroes[key][1]}")
