import os, random

# ¤ ¤ Comment Ranking ¤ ¤ #

#   = Nr. 1 prio , Most important
##  = Nr. 2
### = Nr. 3 

#¤ = Comment
# ¤ ¤ = HeadLine = ¤ ¤ # 



# ¤ ¤ BOOL STATEMENTS FOR GAME/MENU/PLAY/HELP/ ¤ ¤ #
run = True
menu = True
play = False
help = False

key = False             ### Quest/puzzle

fight = False           ### Fighting
standing = True         ### Not dead


# ¤ ¤  PLAYER  (global) ¤ ¤ # 

### Make function (def) for PLAYER if possible?

HP = 50
HPMAX = HP
ATK = 4
pot = 1
gold = 0
x = 0
y = 0


# ¤ ¤  MAP  ¤ ¤  #

map =  [["shop",   "plains", "plains", "plains", "forest", "mountain",     "cave"],
        ["cave",   "forest", "forest", "forest", "forest",    "hills", "mountain"],
        ["forest", "fields", "bridge",  "hills", "forest",   "plains",    "hills"],
        ["hills",    "shop",   "town",  "swamp", "plains",    "hills", "mountain"],
        ["plains", "fields", "fields", "plains",  "hills", "mountain", "mountain"]]

# ¤ ¤ Movement on map by length of Y and X on map
y_len = len(map)-1
x_len = len(map[0])-1

map_info = {
    "town": {
        "t": "TOWN CENTRE",             # ¤ ¤ ¤  "t" = terrain
        "e": False,                     # ¤ ¤ ¤  "e" = enemie (True, False)
        "d": "I'ts a small town."},     # ¤ ¤ ¤  "d" = description
    "plains": {
        "t": "PLAINS",          
        "e": True,              
        "d": "You are out on the on the open plains. The landsscape is relativly flat."},
    "forest": {
        "t": "WOODS",
        "e": True,
        "d": "You are in the deep dark woods."}, 
    "fields": {
        "t": "FIELDS",
        "e": False,
        "d": "You see the field stretch for ever and ever."},
    "bridge": {
        "t": "BRIDGE",
        "e": True,
        "d": "The bridge looks old and also very sturdy."},
    "shop": {
        "t": "SHOP",
        "e": False,
        "d": "The shop is very clean and tidy, but the shop-keeper seems fishy."},
    "swamp": {
        "t": "SWAMP",
        "e": False,
        "d": "Swamp thing, you make my heart sing."},
    "cave": {
        "t": "CAVE",
        "e": False,
        "d": "It's just an empty dark cave... or is it?"},
    "mountain": {
        "t": "MOUNTAIN",
        "e": True,
        "d": "There is a road leading up to the mountains."},
    "hills": {
        "t": "HILLS",
        "e": True,
        "d": "Green grass hills."},
}


# ¤ ¤  ENEMIES  ¤ ¤ # 

e_list = ["Orc"]                # Make more enemies

mobs = {
    "Orc":{
        "e_hp": 15,
        "e_atk" : 3,
        "e_gold": 18 
    }

}

# ¤ ¤  NPC(:S)  ¤ ¤ # 

npc_list = []                   # Make NPC(:s)

# ¤ ¤  MENUS BORDERS ETC  ¤ ¤ #

def clear():
    os.system("clear")            #¤ "clear" on MAC/Docker, cls on Windows

def draw_border():
    clear()
    draw_len_tnaim()
    print(f"Coord: X{x} Y{y}")  
    draw_len_tnaim()
    print(f"\n{map_info[map[y][x]]['t']}:\n{map_info[map[y][x]]['d']}\n")
    l = len(f"{name} | HP: {HP} / {HPMAX} | Gold: {gold}")
    print(l * "~")
    print(f"{name} | HP: {HP} / {HPMAX} | Gold: {gold}")
    print(l * "~" +"\n")

def intro_menu():
    print("~" * 14)
    print("1, New Game")
    print("2, Load Game")
    print("3, Rules/Help")
    print("4, Quit")
    print("~" * 14)

def draw_len_tnaim():
    langd = len(f"Location: {map_info[map[y][x]]['t']}")
    print("-" * langd)

def draw_len_desc_name():
    langd = len(f"Room: {map_info[map[y][x]]['d']}")
    print("-" * langd)

# ¤ ¤  SAVE  ¤ ¤ # 

def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(gold),
        str(x),
        str(y),
        str(key)
        ]
    f = open("load.txt", "w")   #¤  "w" = write to "load.txt"

    for item in list:
        f.write(item + "\n")    #¤  Iterates over list and adds newline for each "item"
    f.close()

# ¤ ¤  BATTLE  ¤ ¤ # 

def battle():
    global fight, play, run, HP, pot, gold         #¤ global = gets the values outside func.
    enemy = random.choice(e_list)
    e_hp = mobs[enemy]["e_hp"]
    hpmax = e_hp
    e_atk = mobs[enemy]["e_atk"]
    e_gold =  mobs[enemy]["e_gold"]

    while fight:
        clear()
        print("Defeat the " + enemy + "i")
        print(enemy + "'s HP:" + str(e_hp) + "/" + str(hpmax))
        print(name + "'s HP:" + str(HP) + "/" + str(HPMAX))
        print("Potion:" + str(pot))
        print("1) Attack ")
        if pot > 0:
            print("2) -  USE POTION (25HP)")

        choice = input("->")

        if choice == "1":        #¤ Iniate the attack, 1:st player, if 2:nd enemy turn
            e_hp -= ATK
            print(name + " dealt " + str(ATK) + " damage to the " + enemy)
            if e_hp >= 0:        #¤ If enemy has e_hp, it can atk
                HP -= e_atk
                print(enemy + " dealt " + str(ATK) + " damage to the " + name)
            input(" ")
        
        elif choice  == "2":     # Make potion work
            pass

        #¤ If player dies
        if HP <= 0:
            print(enemy + " DEFEATED " + name +"....")
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("...")
            quit()
        #¤ If Enemy dies
        if e_hp <= 0:
            print(name + " DEFEATED the " + enemy + "....")
            fight = False
            gold += e_gold
            print("You found " +str(e_gold) + " gold.")
            input("#>> ")
            clear()


# # # # # # # # # # # # # # # # # # # # # # # # 

while run:
    while menu:
        clear()
        # # # print(logo) make logo
        intro_menu()

        if help:
            clear()
            print("""This is the help section.\n\n-* Press Return to go back to menu *-""")        ## Add atuff to Rules/Help
            help = False
            choice = ""
            input("> ")         ### Implement Sleep function instead of input

        else:
            choice = input(">> ")

        # Start Game
        if choice == "1":
            clear()
            name = input("What name do you want for your character?\n>> ").title()
            menu = False
            play = True

        # Load Game
        elif choice == "2":
            f = open("load.txt", "r")               #¤ "r" = read from load.txt to get values/objects 
            load_list = f.readlines()
            name = load_list[0][:-1]
            HP = int(load_list[1][:-1])             #¤ Had to convert back to orginal type ex int() and bool
            ATK = int(load_list[2][:-1])
            pot = int(load_list[3][:-1])
            gold = int(load_list[4][:-1])
            x = int(load_list[5][:-1])
            y = int(load_list[6][:-1])
            key = bool(load_list[7][:-1])
            clear()
            print(f"Welcome back {name}")
            input(">> ")        ### Implement Sleep function instead of input
            menu = False
            play = True
        elif choice == "3":
            help = True
        elif choice == "4":
            quit()

    while play:
        # save()      #¤ Autosave but it makes new game contiue where last load ended
        clear()

        if not standing:
            if (f"Location: {map_info[map[y][x]]['e']}"):      #¤ if there is an 'e' = fight 
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()

        if play:
            draw_border()
            if y > 0:               # Y
                print(f"1) You see {map_info[map[y-1][x]]['t']} to the South.")      ## Update numbers to direction 1=S, 2=E etc.. 
            if x < x_len:
                print(f"2) You see {map_info[map[y][x+1]]['t']} to the East.")  
            if y < y_len:
                print(f"3) You see {map_info[map[y+1][x]]['t']} to the North.")
            if x > 0:
                print(f"4) You see {map_info[map[y][x-1]]['t']} to the West.")
            print("-"*16)
            print("0 - Save & Quit.")
            print("-"*16)

            dest = input("> ")          ### and add .lower or .upper 

            if dest == "0":
                play = False
                menu = True
                save()
            elif dest == "1":           ##     s
                if y > 0:
                    y -= 1
                    standing = False
            elif dest == "2":           ##     e
                if x < x_len:
                    x += 1
                    standing = False
            elif dest == "3":           ##     n
                if y < y_len:
                    y += 1
                    standing = False
            elif dest == "4":           ##     w
                if x > 0:
                    x -= 1
                    standing = False

























        # look = input("In What direction? ")
        # if look == "W"

# for i in map:
#   print(*i)

# current_tile = map[y][x]
# print(current_tile)
# name_of_tile = biom[current_tile]["t"]
# print(name_of_tile)
# enemy_tile = biom[current_tile]["e"]
# print(enemy_tile)