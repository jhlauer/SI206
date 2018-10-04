#TODO
#write unittests
#write docstrings for all functions and classes
#'''DOCSTRING-sentence or 2 re. what function/class does. new line. list of parameters & what it represents/description'''

class Room:
    def __init__(self, dict_rooms, room_treasure, room_description, room_name):
        self.dict_rooms = dict_rooms
        self.room_treasure = room_treasure
        self.room_description = room_description
        self.room_name = room_name

    def __str__(self):
        return (str(self.room_name) + ": " + str(self.room_description))

    def get_room_treasure(self):
        return "Treasure in this room: " + str(self.room_treasure)
    
    def get_room_description(self):
        return str(self.room_description)

    def get_room_name(self):
        return "You are in: " + str(self.room_name)

    def set_room_treasure(self, treasure_list):
        self.room_treasure = treasure_list

    def set_room_description(self, description):
        self.room_description = description

    def set_room_name(self, name):
        self.room_name = name

class Player:
    def __init__(self, current_room):
        self.player_treasure = []
        self.current_room = current_room
        self.num_lives = 3
        self.num_pts = 0

    def __str__(self):
        return ("Player has " + str(self.num_pts) + " points.")
    
    def get_player_treasure(self):
        return self.player_treasure
    
    def get_num_points(self):
        for item in self.player_treasure:
            self.num_pts += item.get_treasure_num_pts()
        return self.num_pts

    def get_num_lives(self):
        return self.num_lives

    def get_current_room(self):
        return "Current room: " + str(self.current_room)

    def add_secret_lives(self):
        self.num_lives += 1

    def set_current_room(self, new_room):
        self.current_room = new_room

    def set_num_lives(self, lives):
        self.num_lives =int(lives)

    def set_num_pts(self, pts):
        self.num_pts =int(pts)

class Treasure:
    def __init__(self, name, description, num_pts):
        self.name = name
        self.description = description
        self.num_pts = num_pts

    def __str__(self):
        return str(self.name) + " is worth " + str(self.num_pts)

    def get_treasure_name(self):
        return str(self.name)

    def get_treasure_description(self):
        return str(self.description)

    def get_treasure_num_pts(self):
        return self.num_pts

    def set_treasure_name(self, name):
        self.name = name 

    def set_treasure_description(self, description):
        self.descritpion = description

    def set_treasure_num_pts(self, pts):
        self.num_pts = pts

class Game:
    def __init__(self):
        #treasure set up
        t1 = Treasure("Diamond", "Diamond ring", 20)
        t2 = Treasure("Jade", "Necklace", 10)
        t3 = Treasure("Ruby", "Earrings", 10)
        t4 = Treasure("Sapphire", "Bracelet", 10)
        t5 = Treasure("Gold", "Ring", 10)
        t6 = Treasure("Silver", "Necklace", 10)
        t7 = Treasure("Bronze", "Bracelet", 10)
        t8 = Treasure("Rose-gold", "Earrings", 10)
        t9 = Treasure("Emerald", "Pendant", 10)
        t10 = Treasure("Pearl", "Earrings", 10)
        
        #room set up
        r1 = Room({}, [], "Start room", "Room 1")
        r2 = Room({}, [t1, t2], "Kitchen", "Room 2")
        r3 = Room({}, [], "Living Room", "Room 3")
        r4 = Room({}, [t5, t6], "Bathroom", "Room 4")
        r5 = Room({}, [t3, t4, t7, t9, t10], "Dining Room", "Room 5")
        r6 = Room({}, [t8], "Bedroom", "Room 6")
        r7 = Room({}, [], "Exit room", "Room 7")
        r1.dict_rooms['e'] = r2
        r1.dict_rooms['s'] = r4
        r2.dict_rooms['w'] = r1
        r2.dict_rooms['s'] = r3
        r3.dict_rooms['n'] = r2
        r3.dict_rooms['w'] = r4
        r3.dict_rooms['s'] = r6
        r4.dict_rooms['n'] = r1
        r4.dict_rooms['s'] = r5
        r4.dict_rooms['e'] = r3
        r5.dict_rooms['n'] = r4
        r5.dict_rooms['e'] = r6
        r6.dict_rooms['w'] = r5
        r6.dict_rooms['n'] = r3
        r6.dict_rooms['e'] = r7
        r7.dict_rooms['w'] = r6
        self.player = Player(r1)
        self.start_room = r1
        self.exit_room = r7

    def get_exit_room(self):
        return "Exit room is " + str(self.exit_room)

    def get_player_data(self):
        return (self.player.__str__())

    def set_player_data(self, p):
        self.player = p

    def set_exit_room(self, er):
        self.exit_room = er

    def play(self):
        if self.player.current_room != self.exit_room:
            if self.player.num_lives > 0:
                print("Current room: " + str(self.player.current_room)) 
                print(self.player.current_room.get_room_treasure())

            #while player is alive
            # while player not in exit room
            while self.player.get_num_lives() > 0 and self.player.current_room != self.exit_room: 
                print("Number of lives remaining: " + str(self.player.get_num_lives()))
                direction = input("What direction would you like to move? ('n', 's', 'w', or 'e')")
                try:
                    #moving rooms
                    current_room = self.player.current_room
                    next_room = current_room.dict_rooms[direction]
                    self.player.current_room = next_room
                    print("You have traveled to " + str(self.player.current_room))

                    #collecting treasure
                    for item in current_room.room_treasure:
                        self.player.player_treasure.append(item)

                except:
                    #wrong direction
                    x = self.player.get_num_lives() - 1
                    self.player.set_num_lives(x)
                    if self.player.get_num_lives() > 0:
                        print("Sorry, you can't go this way! -1 life :(")
                    else:
                        print("Sorry, you can't go this way!")
                    
            
            #player in exit room 
            while self.player.current_room == self.exit_room:
                #enough points
                if self.player.get_num_points() >= 100:
                    print("CONGRATS! You have enough points to exit the game. You won!")
                    return
                #not enough points
                elif self.player.get_num_points() < 100:
                    print("You do not have enough points to exit the game. You will be taken back to the start room. Keep looking for more treasure!")
                    self.player.current_room = self.start_room
            
            #no more lives
            print("You have no more lives left. Game over!")   
            return

g = Game()
g.play()



