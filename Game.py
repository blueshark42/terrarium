import Print
import Fight
from Entities import player
from Levels import levels


Print.main_menu()
choice = None


def get_int():
  inp = input("Choice: ")
  try:
    user_num = int(inp)
    return user_num
  except ValueError:
    Print.invalid_choice()
    return(get_int())


while choice != 3:
  choice = get_int()

  if choice == 1:
    Print.choose_level()
    choice = get_int()
    
    if choice == len(levels)+1:
      Print.main_menu()
    elif choice < 1 or choice > len(levels)+1:
      Print.invalid_choice()
    else:
      Fight.begin_fight(levels[choice-1])

  elif choice == 2:
    Print.character()
    choice = int(input("Choice: "))

    if choice == 0:
      Print.main_menu()
    elif choice > 0 and choice <= len(player.weapons):
      player.weapon = player.weapons[choice-1]
      Print.equipped_weapon()
      input("Continue...\n")
      Print.main_menu()
  elif choice == 3:
    exit(0)
  else:
    Print.invalid_choice()
