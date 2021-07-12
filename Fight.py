import random
import Print
from termcolor import colored
from Entities import player

def win(level):
  print(colored("You won!\n\n", "yellow", attrs=["bold"]))
  item = level.get_drop()
  if item != None:
    player.weapons.append(item)

  exp = random.randint(level.min_exp, level.max_exp)
  print(colored("XP received: {}".format(exp), "yellow"))
  player.give_exp(exp)

  player.health = player.max_health
  Print.main_menu()


def lose():
  print(colored("You lost!\n\n", "red", attrs=["bold"]))
  player.health = player.max_health
  Print.main_menu()


def flee():
  print(colored("You fled!\n\n", "blue", attrs=["bold"]))
  player.health = player.max_health
  Print.main_menu()


def print_stats(enemy, player):
  print(colored("=== {} ===".format(enemy.name), "yellow"))
  print(colored("Weapon: ", attrs=["bold"]) + Print.print_weapon(enemy.weapon))
  print(colored("Health: ", attrs=["bold"]) + colored("{}\n".format(enemy.health), "green"))

  print(colored("=== You ===", "yellow"))
  print(colored("Weapon: ", attrs=["bold"]) + Print.print_weapon(player.weapon))
  print(colored("Health: ", attrs=["bold"]) + colored("{}\n".format(player.health), "green"))


def begin_fight(level):
  choice = None
  enemy = get_enemy(level.enemies)

  print("You have encountered a " + colored(enemy.name, "yellow") + "!")
  print(colored("Weapon: ", attrs=["bold"]) + Print.print_weapon(enemy.weapon))
  print(colored("Health: {}\n".format(enemy.health), "green"))

  while choice != 3:
    print("1 - Attack\n2 - Heal\n3 - Flee")
    try:
      choice = input("Choice: ")
      choice = int(choice)
    except ValueError:
      pass

    if choice == 1:
      damage = player.attack()

      print("Hit! Damage given: {}.".format(damage))

      if damage >= enemy.health:
        win(level)
        return

      enemy.health -= damage
      print_stats(enemy, player)

      input("Continue...")

      damage = enemy.attack()
      print("Hit! Damage received: {}.".format(damage))

      if damage >= player.health:
        lose()
        return

      player.health -= damage
      print_stats(enemy, player)


    elif choice == 2:
      pass
    elif choice == 3:
      flee()
    else:
      Print.invalid_choice()


def get_enemy(possible_enemies):
  return random.choice(possible_enemies)