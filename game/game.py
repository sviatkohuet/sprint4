"""Game module"""

class Room:
    """Room class"""

    def __init__(self, name):
        """Room constructor"""
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def get_details(self):
        """Prints the room details"""
        res = ''
        res += self.name+'\n'
        res += '--------------------\n'
        res += self.description + '\n'
        for key in self.linked_rooms.keys():
            res += f'The {self.linked_rooms[key].name} is {key}\n'
        res += f'{self.character.name} is here!\n{self.character.describe()}\n'\
              if self.character is not None else ''
        res += f'The [{self.item.get_name()}] is here! - {self.item.describe()}\n'\
              if self.item is not None else ''
        print(res.strip())

    def get_character(self):
        """Returns the character in the room"""
        return self.character

    def get_item(self):
        """Returns the item in the room"""
        return self.item

    def set_description(self, text):
        """Sets the room description"""
        self.description = text

    def link_room(self, room, direction):
        """Links the room to another room in a given direction"""
        self.linked_rooms[direction] = room

    def set_character(self, character):
        """Sets the character in the room"""
        self.character = character

    def set_item(self, item):
        """Sets the item in the room"""
        self.item = item

    def move(self, command):
        """Moves the player to a new room"""
        new_room = self.linked_rooms[command]
        return new_room

class Enemy:
    """Enemy class"""
    defeats = 0

    def __init__(self, name, description):
        """Enemy constructor"""
        self.name = name
        self.description = description
        self.conversation = None
        self.weakness = None

    def fight(self, weapon):
        """Fights the enemy"""
        if weapon == self.weakness:
            return True
        return False

    @classmethod
    def get_defeated(cls):
        """Returns the number of defeated enemies"""
        cls.defeats += 1
        if cls.defeats == 2:
            cls.defeats = 0
            return 2
        return cls.defeats

    def talk(self):
        """Talks to the enemy"""
        print(f'[{self.name} says]: {self.conversation}')

    def describe(self):
        """Describes the enemy"""
        return self.description

    def set_conversation(self, text):
        """Sets the enemy conversation"""
        self.conversation = text

    def set_weakness(self, weakness):
        """Sets the enemy weakness"""
        self.weakness = weakness


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
