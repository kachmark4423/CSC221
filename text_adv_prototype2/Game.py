# CSC 221
# Text Adventure Prototype 2
# Khalil Kachmar
# 10/30/21

from Room import Room
#import Player


"""
Version history:
    v1 - built using Room references (basically a graph). 
        downside: you have to create all rooms, then link
        them together afterwards.
        
    v2 - used constant room IDs to make it possible to add
        and link rooms in one pass. 
        downside: "this looks like BASIC" (from the peanut gallery)
        
    v3 - realization: if the Room names are unique, that's a
        unique ID. I therefore changed
        the container for all Rooms to be a dictionary --
        now it's easy enough to look up the room by name.
        
    v4 - items for possible future actions added to rooms. 
         "Take" added as new verb
         player inventory list added to game


"""

class Game:
    """
    The Game class organizes all game data in a central location.
    Usage:
    - Set up game using your choice of room configurations
      (TODO: Read these from a file in future)
    - call loop()
    """

    def __init__(self):
        """ Initialize object (with no rooms) """
        #self.player = player.Player()
        self.rooms = { } # stored in dictionary
        self.here = None # TODO: move this to Player
        self.isPlaying = True
        self.isVerbose = True # auto-look on move
     

    def __str__(self):
        pass

    def __repr__(self):
        pass


    def setup(self):
        """ setup(): create a graph of rooms for play. """
        # just a test -- needs work
        bedroom = Room( "Bedroom", 
                   "This is an average bedroom. A leather case sits on the table",
                   { "north": "Bathroom",
                     "east": "Living Room"}, 
                     ["lock-pick"])
    
       
        
        livingRoom = Room ( "Living Room",
                           "A fouton being used as a bed, a recliner and a tv."
                           "A pair of shoes sit next to the front door.",
                           { "north" : "Dining Room", "west" : "Bedroom" }, 
                           ["shoes"])
        
        
        bathroom = Room ( "Bathroom", 
                         "The shower seems to be dripping. A pistol sits"
                         "on the sink counter",
                         { "south" : "Bedroom" }, 
                         ["pistol"])
        
        diningRoom = Room ("Dining Room", "There is a case of ammo on the table",
                           {"south":"Living Room", "west": "Kitchen"},
                           ["ammo"])
        
        kitchen = Room ("Kitchen", "Typical kitchen. It's a bit cluttered but"
                        " no dirty dishes. The fridge seems to be open", 
                        {"east":"Dining Room"},
                        ["magazine"])
        
        # Place rooms in a dictionary.
        # (Game will handle this in the full version)
        self.rooms = { bedroom.name: bedroom, 
                    livingRoom.name: livingRoom,
                    bathroom.name: bathroom,
                    kitchen.name: kitchen,
                    diningRoom.name: diningRoom}
        
        self.here = bedroom # starting location

    def loop(self):
        """ loop(): the main game loop.
        Continues until the user quits. """
        self.isPlaying = True
        global inventory
        inventory = []
        while self.isPlaying:
            self.playerAction()
        print("Game over, thanks for playing")
        


    def end(self):
        """ finish game, inform user of score and turns played. """
        pass
    
    def playerAction(self):
        """ Ask user for input, validate it, update the game state. """
        command = input(">")
        command = command.lower()
        words = command.split() # split on whitespace
        if len(words) < 1:
            print("No input detected")
            return
        
        verb = words[0]
        if verb == "go":
            direction = words[1]
            # Can we go in the chosen direction from here?
            if self.here.exits.get(direction) == None:
                print("You can't go that way.")
            else:   
                # this key does exist
                newRoomName = self.here.exits[direction]
                newRoom     = self.rooms[newRoomName]
                self.here   = newRoom
                if self.isVerbose:
                    self.here.describe()
        elif verb == "look":
            self.here.describe()
        elif verb == "quit":
            self.isPlaying = False
            print("quitting")

        elif verb == "take":
            item = words[1]

            if item.lower() not in self.here.items:
                print(f"Can't take {item}")
            else:
                global inventory
                print(f"You have picked up {item}")
                inventory.append(item)
        elif verb == "inventory" or verb == 'i':
            print(inventory)
        
        else: # first word is verb
            print("I don't know how to", words[0])


def main():
    game = Game()
    game.setup()
    game.loop()
    game.end()


if __name__ == "__main__":
    main()
