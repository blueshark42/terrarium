# Printing the text for the game
from Levels import levels
import Print
from Entities import player, WeaponRarity
from termcolor import colored


def main_menu():
  print("1 - fight\n2 - character\n3 - exit")


def choose_level():
  print("Choose level:")

  for i in range(len(levels)):
    print("{} - {}".format(i+1, levels[i].level_name))

  print("{} - Back\n".format(len(levels)+1))


def character():
  # lvl_empty = "▱"
  lvl_full = "▰"

  print(colored("Your stats: ", attrs=["bold"]))
  print(colored("Level: ", attrs=["bold"]) + colored("{}".format(player.level), "yellow"), end="    ")

  tiles = 10
  xp_req = player.xp_required()
  pl_xp = player.experience
  full = pl_xp / (pl_xp + xp_req) * tiles

  level_bar = ""
  for i in range(tiles):
    if i < full:
      level_bar += colored(lvl_full, "cyan")
    else:
      level_bar += colored(lvl_full, "grey")

  level_bar += " {}/{} Exp".format(str(pl_xp), str(xp_req + pl_xp))

  print(level_bar)

  print(colored("Health: ", attrs=["bold"]) + colored("{}".format(player.health), "green"))
  print(colored("Equipped Weapon: ", attrs=["bold"]) + print_weapon(player.weapon) + "\n")

  print("Common, ", end="")
  print(colored("Rare", "blue")+", ", end="")
  print(colored("Epic", "magenta")+", ", end="")
  print(colored("Legendary", "yellow", attrs=["bold"])+", ", end="")
  print(colored("Godly", "red", attrs=["bold", "underline"]), end="")
  print("\n === INVENTORY ===")
  i = 1
  for item in player.weapons:
    print(str(i) + " - " + print_weapon(item))
    i += 1

  print("\nChoose ID to equip weapon, 0 - Back")


def print_weapon(weapon):
  str = ""
  if weapon.rarity == WeaponRarity.COMMON:
    str += weapon.name
  elif weapon.rarity == WeaponRarity.RARE:
    str += colored(weapon.name, "blue")
  elif weapon.rarity == WeaponRarity.EPIC:
    str += colored(weapon.name, "magenta")
  elif weapon.rarity == WeaponRarity.LEGENDARY:
    str += colored(weapon.name, "yellow", attrs=["bold"])
  elif weapon.rarity == WeaponRarity.GODLY:
    str += colored(weapon.name, "red", attrs=["bold", "underline"])

  return str + " (" + colored("{} - {}".format(weapon.min_damage, weapon.max_damage), "red") + ")"

def equipped_weapon():
  print("\nEquipped weapon: " + Print.print_weapon(player.weapon))


def invalid_choice():
  print("Invalid choice!\n")