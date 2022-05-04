Överlämning

KrypIn

It's an old text RPG game, made with python 3.9
My first idea was that this was going to be a text adventure/RPG, with some puzzles of different kinds (riddles, quest(ions) and keys). The map was going to be randomized for every new game that you started.
But as the Project/Game evolved, I now see it as Game-engine / template / blueprint, where you can modify it to fit what you kind of game you want to make. So from here and onward there will be examples of what the 'Game' can look like, but I'm just going to add features to it, so the creative phase will be in what kind of new addons to the enginge we can add, rather than make a fully playable game. But with that being said I need to change my initial plan with the sprints. 
If there is time to implemate story, then do it but it's not a priority.

SPRINT 1 

1. Skapa en karaktär (str, int, input, db(character)
⦁	Name
⦁	Hit Points

2. Kan gå i olika riktningar (Class, Directions: n,s,ö,v,u,n)
	Directions (all includes go, either gn or gå norr)
⦁	gn or gå norr == ”north”
⦁	gs or gå söder == ”south”
⦁	ge or gå öst == “east”
⦁	gv or gå väst == “west”
⦁	gu or gå upp == ”up”
⦁	gd or gå ner == “down”

3. (Completed but in the way I first intented) 
Titta i omgivningarna = (Part of storyn), kunna titta i den riktning du tänker att gå till och få en lätt överblick (dock ej alltid möjligt):
⦁	Skriva description till varje plats/rum
⦁	Titta or Look <Direction>, get brief info back 

4. Spara sin framgång och kunna fortsätta därifrån man var.
		
5. (Cancled, (Maybe) if everything done and you have nothing else to do)
Kunna välja vilken karaktär du har tänkt börja/fortsätta med

6. Skapa Fiender
⦁	Fiende med hp och möjligt item drop



SPRINT 2
7. Skapa Npc
⦁	Npc med hp och möjligt ett item drop

8. Lätta puzzle (suggestions) (str, input, sqlite3(inventory))
⦁	Riddles
⦁	Key-door
⦁	Quest(ions)

9. Inventory (backpack): Tools: (Py, sqlite3(db))
⦁	Hantera föremål
⦁	plocka upp
⦁	slänga
⦁	Låta föremålet ligga kvar i den ruta/rum man lämnade det i. 

Olika kategorier:
⦁	Notiser/meddelande
⦁	Vapen
⦁	Konsumerbara artiklar (potions)
⦁	Nycklar

10. Insert some ASCII art
⦁	Start screen
⦁	On map / de

11. Add Color to 
	Character 
⦁	HP
⦁	Gold
⦁	Player
⦁	Enemie
⦁	NPC