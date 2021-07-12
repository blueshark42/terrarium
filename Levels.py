import Entities
import random
from termcolor import colored

class Level:
    def __init__(self, level_name, enemies, weapons, chance_for_drop, min_exp, max_exp):
      self.level_name = level_name
      self.enemies = enemies
      self.weapons = weapons
      self.chance_for_drop = chance_for_drop
      self.min_exp = min_exp
      self.max_exp = max_exp

    def get_drop(self):
      if self.weapons == None or len(self.weapons) < 1:
        print("There's nothing to find here")
        return None

      if random.randint(0, 100) > self.chance_for_drop:
        print ("You didn't find anything this time.")
        return None

      chance = random.randint(0, 100)
      self.weapons.sort(key=lambda a: a[1])

      for item in self.weapons:
        if item[1] >= chance:
          print("Yes! You found a: " + colored(item[0].name) + "!")
          return item

      print ("You didn't find anything this time.")


forest = Level("Forest", [Entities.wolf, Entities.shark, Entities.ghost], None, None, 1, 3)
cave = Level("Cave", [Entities.trap, Entities.magma_spit, Entities.caveman], [(Entities.iron_fists, 79), (Entities.crab_claws, 68), (Entities.iron_sword, 42)], 80, 5, 9)
levels = [forest, cave]
