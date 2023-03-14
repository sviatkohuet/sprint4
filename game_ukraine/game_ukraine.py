"""Game Ukraine module"""

import random

class Region:
    """Base class for all regions"""

    def __init__(self, name):
        """Initializes the region"""
        self.name = name
        self.description = None
        self.linked_regions = {}
        self.character = None
        self.item = None

    def get_details(self):
        """Prints the room details"""
        res = ''
        res += self.name+'\n'
        res += '--------------------\n'
        for key in self.linked_regions.keys():
            res += f'{self.linked_regions[key].name} на {key}\n'
        res += f'\n{self.character.name} тут!\n{self.character.describe()}\n'\
              if self.character is not None else ''
        res += f'[{self.item.get_name()}] тут!'\
              if self.item is not None else ''
        print(res.strip())

    def get_character(self):
        """Returns the character in the room"""
        return self.character


    def link_region(self, region, direction):
        """Links the room to another room in a given direction"""
        self.linked_regions[direction] = region

    def set_character(self, character):
        """Sets the character in the room"""
        self.character = character


    def move(self, command):
        """Moves the player to a new room"""
        if command in self.linked_regions.keys():
            new_room = self.linked_regions[command]
        return new_room


class PeacefulRegion(Region):
    """Class for peaceful regions"""

    def __init__(self, name):
        """Initializes the peaceful region"""
        super().__init__(name)
        self.type = 'peaceful'
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_item(self, item):
        """Sets the item in the room"""
        self.item = item

    def get_item(self):
        """Returns the item in the room"""
        return self.item


class FrontLineRegion(Region):
    """Class for front line regions"""

    def __init__(self, name):
        """Initializes the front line region"""
        super().__init__(name)
        self.type = 'frontline'
        self.linked_rooms = {}
        self.character = None


class Crimea(FrontLineRegion):
    """Class for Crimea region"""

    def __init__(self, name):
        """Initializes the Crimea region"""
        super().__init__(name)
        self.character = None

    def get_details(self):
        """Prints the room details"""
        res = ''
        res += self.name+'\n'
        res += '--------------------\n'
        res += f'\n{self.character.name} тут!\n{self.character.describe()}\n'\
              if self.character is not None else ''
        res += f'[{self.item.get_name()}] тут!'\
              if self.item is not None else ''
        print(res.strip())

class Character:
    """Base class for all characters"""

    def __init__(self, name, description):
        """Initializes the character"""
        self.name = name
        self.description = description


    def describe(self):
        """Describes the enemy"""
        return self.description


class Enemy(Character):
    """Enemy class"""
    defeats = 0

    def __init__(self, name, description):
        """Enemy constructor"""
        super().__init__(name, description)
        self.weakness = None

    def set_weakness(self, weakness):
        """Sets the enemy weakness"""
        self.weakness = weakness

    def fight(self, weapon):
        """Fights the enemy"""
        if weapon == self.weakness:
            return True
        return False

    @classmethod
    def get_defeated(cls):
        """Returns the number of defeated enemies"""
        cls.defeats += 1
        if cls.defeats == 4:
            cls.defeats = 0
            return 4
        return cls.defeats


class Putin(Enemy):
    """Putin class"""

    def __init__(self, name, description):
        """Putin constructor"""
        super().__init__(name, description)
        self.name = name
        self.description = description

    def fight(self, number):
        """Fights the enemy"""
        if number == int(random.choice(range(1, 5))):
            return True
        return False


class Friend(Character):
    """Friend class"""

    def __init__(self, name, description):
        """Friend constructor"""
        super().__init__(name, description)
        self.item = None

    def set_item(self, item):
        """Sets the item for the friend"""
        self.item = item

    def talk(self):
        """Talks to the friend"""
        print(f'Привіт мене звати {self.name}')

    def give_item(self):
        """Gives the item to the player"""
        return self.item


class Item:
    """Item class"""

    def __init__(self, name):
        """Item constructor"""
        self.name = name
        self.description = None

    def describe(self):
        """Describes the item"""
        return self.description

    def get_name(self):
        """Returns the item name"""
        return self.name

    def set_description(self, text):
        """Sets the item description"""
        self.description = text


class HealItem(Item):
    """Heal item class"""

    def __init__(self, name):
        """Heal item constructor"""
        super().__init__(name)
        self.description = None



class Weapon(Item):
    """Weapon class"""

    def __init__(self, name):
        """Weapon constructor"""
        super().__init__(name)

