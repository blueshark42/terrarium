# Enemies, player, objects
import random
from enum import Enum
from termcolor import colored


class WeaponRarity(Enum):
  COMMON = 0
  RARE = 1
  EPIC = 2
  LEGENDARY = 3
  GODLY = 4

class Weapon:
  def __init__(self, name, min_damage, max_damage, rarity, enchanted):
    self.name = name
    self.min_damage = min_damage
    self.max_damage = max_damage
    self.rarity = rarity
    self.enchanted = enchanted

  def get_damage(self):
    return random.randint(self.min_damage, self.max_damage)


# Player weapons
#forest
wooden_sword = Weapon("Wooden Sword", 2, 5, WeaponRarity.COMMON, False)
rock = Weapon("Rock", 4, 8, WeaponRarity.COMMON, False)
stone_knife = Weapon("Stone Knife", 12, 18, WeaponRarity.COMMON, False)
#cave
iron_fists = Weapon("Iron Fists", 41, 52, WeaponRarity.COMMON, False)
crab_claws = Weapon("Crab Claws", 62, 75, WeaponRarity.RARE, False)
iron_sword = Weapon("Iron Sword", 64, 87, WeaponRarity.RARE, False)
#hell
molten_greatsword = Weapon("Molten Greatsword", 129, 240, WeaponRarity.EPIC, False)
magma_bomb = Weapon("Magma Bomb", 247, 290, WeaponRarity.EPIC, False)
meteorite_dagger = Weapon("Meteorite Dagger", 231, 268, WeaponRarity.EPIC, False)
devils_kiss = Weapon("Devil's Kiss", 348, 389, WeaponRarity.LEGENDARY, False)
#aethers nebula
angel_of_death = Weapon("Angel of Death", 497, 803, WeaponRarity.LEGENDARY, False)
entropic_claymore = Weapon("Entropic Claymore", 486, 672, WeaponRarity.LEGENDARY, False)
galaxia = Weapon("Galaxia", 512, 590, WeaponRarity.LEGENDARY, False)
void_vortex = Weapon("Void Vortex", 734, 872, WeaponRarity.LEGENDARY, False)
shellshock = Weapon("Shellshock", 120, 1034, WeaponRarity.LEGENDARY, False)
#devourers haven
gods_devastation = Weapon("God's Devastation", 1403, 2034, WeaponRarity.LEGENDARY, False)
nadir = Weapon("Nadir", 1703, 1833, WeaponRarity.LEGENDARY, False)
planetary_annihilation = Weapon("Planetary Annihilation", 2031, 2405, WeaponRarity.LEGENDARY, False)

the_last_mourning = Weapon("The Last Mourning", 3403, 5302, WeaponRarity.GODLY, False)
grand_guardian = Weapon("Grand Guardian", 3603, 7382, WeaponRarity.GODLY, False)

# Enemy weapons
claws = Weapon("Claws", 28, 34, WeaponRarity.COMMON, False) # Wolf
teeth = Weapon("Teeth", 27, 32, WeaponRarity.COMMON, False) # Shark
jumpscare = Weapon("Jumpscare", 42, 45, WeaponRarity.COMMON, False) # Ghost

poison_dart = Weapon("Poison Dart", 34, 42, WeaponRarity.RARE, False) # Trap
magma_spit = Weapon("Magma Spit", 67, 78, WeaponRarity.EPIC, False) # Lava Hound
knife = Weapon("Knife", 27, 49, WeaponRarity.RARE, False) # Caveman

# astral scythe, crimson crusher, absolute zero, brimlash
# storm ruler, forsaken scimitar, terror blade, cosmic shiv
# eradicator, nanoblack reaper, darkecho deathbow, storm net
# pristine fury, soul piercer

class Enemy:
  def __init__(self, name, weapon, health):
    self.name = name
    self.weapon = weapon
    self.health = health

  def attack(self):
    return self.weapon.get_damage()

# Enemies
wolf = Enemy("Wolf", claws, 10)
shark = Enemy("Shark", teeth, 13)
ghost = Enemy("Ghost", jumpscare, 7)

trap = Enemy("Trap", poison_dart, 10)
magma_spit = Enemy("Lava Hound", magma_spit, 164)
caveman = Enemy("Caveman", knife, 134)

# cultist, devil, armored digger, shocked atlas
# plaguebringer, cloud elemental, leviathan, polterghast
# devourer of gods, anahita, soul cataclysm, thunder void
# holy guardian, nuclear supreme calamitas


class Player:
  def __init__(self, max_health, weapons):
    self.max_health, self.health = max_health, max_health
    self.weapon = wooden_sword
    self.weapons = weapons
    self.experience = 0
    self.level = 0
    self.level_exp = [0, 5, 14, 27, 63, 89, 125]

  def attack(self):
    return self.weapon.get_damage()

  def xp_required(self):
    return self.level_exp[self.level] + self.level_exp[self.level+1] - self.experience

  def xp_next_level(self):
    return self.level_exp[self.level+1]

  def give_exp(self, amount):
    self.experience += amount

    required_exp = self.level_exp[self.level] + self.level_exp[self.level+1]
    if self.experience >= required_exp:
      self.level += 1
      print(colored("Level up! Lvl: {}".format(self.level), "blue"))


player = Player(100, [wooden_sword])

# all_weapons = [wooden_sword, rock, stone_knife, iron_fists, crab_claws, iron_sword, molten_greatsword, magma_bomb, meteorite_dagger, devils_kiss, angel_of_death, entropic_claymore, galaxia, void_vortex, shellshock, gods_devastation, nadir, planetary_annihilation, the_last_mourning, grand_guardian]