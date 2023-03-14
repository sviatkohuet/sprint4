import random

class Region:

    def __init__(self, name):
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
            res += f'The {self.linked_regions[key].name} на {key}\n'
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

    def __init__(self, name):
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

    def __init__(self, name):
        super().__init__(name)
        self.type = 'frontline'
        self.linked_rooms = {}
        self.character = None


class Crimea(FrontLineRegion):

    def __init__(self, name):
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

    def __init__(self, name, description):
        self.name = name
        self.description = description


    def describe(self):
        """Describes the enemy"""
        return self.description


class Enemy(Character):
    defeats = 0

    def __init__(self, name, description):
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

    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description

    def fight(self, number):
        """Fights the enemy"""
        if number == int(random.choice(range(1, 5))):
            return True
        return False


class Friend(Character):

    def __init__(self, name, description):
        super().__init__(name, description)
        self.item = None

    def set_item(self, item):
        self.item = item

    def talk(self):
        print(f'Привіт мене звати {self.name}')

    def give_item(self):
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

    def __init__(self, name):
        super().__init__(name)
        self.description = None

    def heal(self):
        pass


class Weapon(Item):

    def __init__(self, name):
        super().__init__(name)

