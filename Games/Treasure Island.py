print('''
--------------------------------------------
        WELCOME TO THE MINI GAME
    Pirate Island: The Lost Treasure
--------------------------------------------
You are Captain Drake, a pirate explorer searching for the legendary treasure of Skull Island.
Rumors say the treasure is protected by traps, ghosts, and cursed pirates.

Choose carefully — one wrong move can end your journey.
--------------------------------------------
A violent storm crashes against your pirate ship as you approach the mysterious Skull Island. 
Dark clouds fill the sky, lightning flashes across the ocean, and huge waves slam against the sides of your ship. 
You must quickly decide what to do before the storm destroys everything.''')

choice1 = input('''
1. Steer the ship towards the BEACH
2. Steer the ship towards the DOCK
3. Steer the ship towards the REEFS
4. Remain on the SHIP

Your Choice ? 
''')

if choice1 == '1' :
    print('''
--------------------------------------------
You safely land on the sandy beach of Skull Island.
Strange footprints lead toward the jungle, and your treasure hunt begins.
--------------------------------------------
After landing on the island, you move deeper inland and discover two possible paths ahead.''')
    choice2 = input('''
1. Walk towards the JUNGLE
2. Walk towards the CAVE
3. Set up camp and REST

Your Choice ? 
''')

    if choice2 == '1':
        print('''
--------------------------------------------
You carefully travel through the jungle and continue your search for the hidden treasure.
The deeper you go, the more mysterious the island becomes.

As you continue through the island, you arrive at a massive ancient stone gate covered in moss and pirate symbols. 
The gate blocks the path forward, and the jungle around it is silent and eerie. You must decide how to get past it.
--------------------------------------------
''')

        choice3 = input('''
1. CLIMB the gate
2. OPEN the gate

Your Choice ? 
''')

        if choice3 == '1':
            print('''
--------------------------------------------
As you climb over the ancient gate, loose stones suddenly break beneath your feet. 
You fall into a hidden pit filled with sharp spikes.
YOU DIE. GAME OVER
--------------------------------------------
''')

        elif choice3 == '2':
            print('''
--------------------------------------------
With great effort, you slowly push the heavy stone gate open. 
It creaks loudly as a pathway appears before you. An ancient temple appears before you.

Inside the temple, you find three different hallways leading further into the ruins.

1. LEFT Hallway
2. RIGHT Hallway
3. MIDDLE Hallway
--------------------------------------------
''')

            choice4 = input("Your Choice ? ")

            if choice4 == '1':
                print('''
--------------------------------------------
You enter the left hallway.
The floor suddenly cracks open, and flames burst from the walls, surrounding you in fire.
YOU DIE. GAME OVER
--------------------------------------------''')

            elif choice4 == '3':
                print('''
--------------------------------------------
You enter the middle hallway.
Hidden poison darts suddenly shoot from small holes in the walls and strike you before you can escape.
YOU DIE. GAME OVER
--------------------------------------------''')

            elif choice4 == '2':
                print('''
--------------------------------------------
You enter the right hallway.
You safely make your way through the hallway and continue deeper into the temple.

You enter a large treasure chamber illuminated by glowing torches. 
In the center of the room sits a massive golden chest covered in jewels and ancient pirate symbols.

What will you do ?
1. OPEN the chest.
2. EXAMINE the chest carefully.
--------------------------------------------
''')

                choice5 = input("Your Choice ? ")

                if choice5 == '1':
                    print('''
--------------------------------------------
The moment the chest opens, a hidden explosive trap activates and destroys the treasure chamber.
YOU DIE. GAME OVER
--------------------------------------------''')

                elif choice5 == '2':
                    print('''
--------------------------------------------
While examining the chest, you discover a hidden switch connected to a deadly trap mechanism beside the treasure chest.
You carefully pull the hidden switch beside the treasure chest. 
A loud clicking sound echoes through the chamber as the deadly trap mechanism shuts down. 
Slowly, you open the golden chest and discover Captain Blackbeard’s legendary treasure hidden inside.

CONGRATULATIONS! YOU FOUND THE TREASURE AND WON THE GAME!
--------------------------------------------''')

                else:
                    print('''
--------------------------------------------
You chose an invalid option.
YOU DIE. GAME OVER
--------------------------------------------
''')

            else:
                print('''
--------------------------------------------
You chose an invalid option.
YOU DIE. GAME OVER
--------------------------------------------
''')

        else:
            print('''
--------------------------------------------
You chose an invalid option.
YOU DIE. GAME OVER
--------------------------------------------
''')

    elif choice2 == '2' :
        print('''
--------------------------------------------
You enter the cave and discover signs that someone may have been there before you. 
Your adventure continues deeper underground.

At the end of the cave, you see a treasure chest and a pool of water.
What will you do ?

1. OPEN the treasure
2. DIVE into the pool
--------------------------------------------
''')

        choice3 = input("Your Choice ? ")
        if choice3 == '1':
            print('''
--------------------------------------------
As soon as you touch the gold coins, the cave begins to shake violently. 
Rocks fall from above as the entire cave collapses around you.
YOU DIE. GAME OVER
--------------------------------------------
''')

        elif choice3 == '2':
            print('''
--------------------------------------------
As soon as you dive into yhe pool a giant crocodile suddenly jumps out of the water 
and attacks you before you can escape
YOU DIE. GAME OVER
--------------------------------------------
''')

        else:
            print('''
--------------------------------------------
You chose an invalid option.
YOU DIE. GAME OVER
--------------------------------------------
''')

    elif choice2 == '3':
        print('''
--------------------------------------------
You decide to set up a small camp near the beach and rest before continuing your treasure hunt.

During the night, a group of pirates attack you. You are asleep and cannot defend yourself.
YOU DIE. GAME OVER
--------------------------------------------
''')

    else:
        print('''
--------------------------------------------
You chose an invalid option.
YOU DIE. GAME OVER
--------------------------------------------
''')


elif choice1 == '2' :
    print('''
--------------------------------------------
As you step onto the old pirate dock, a group of rough-looking pirates surrounds you. 
Their captain stares at you suspiciously while the others grip their swords tightly. 
You must decide how to handle the situation.

1. FIGHT
2. RUN
--------------------------------------------
''')

    choice2 = input("Your Choice ? ")

    if choice2 == '2':
        print('''
--------------------------------------------
You sprint to escape but pirates quickly surround you. 
You turn to fight against the pirates, but they greatly outnumber you. 
After a long battle, the pirate captain defeats you and throws you into the dark ocean near the docks.
YOU DIE. GAME OVER
--------------------------------------------
''')

    elif choice2 == '1':
        print('''
-------------------------------------------- 
You bravely fight against the pirates, but they greatly outnumber you. 
After a long battle, the pirate captain defeats you and throws you into the dark ocean near the docks.
YOU DIE. GAME OVER
--------------------------------------------
''')

    else:
        print('''
--------------------------------------------
You chose an invalid option.
YOU DIE. GAME OVER
--------------------------------------------
''')

elif choice1 == '3' :
    print('''
--------------------------------------------
Your ship hits the sharp coral reefs hidden beneath the water. 
The hull breaks apart, and the ocean swallows your ship.
YOU DIE. GAME OVER
--------------------------------------------
''')

elif choice1 == '4' :
    print('''
--------------------------------------------
You stay aboard the ship hoping the storm will pass, 
but the powerful waves destroy the vessel during the night.
YOU DIE. GAME OVER
--------------------------------------------
''')

else :
    print('''
--------------------------------------------
You chose an invalid option.
YOU DIE. GAME OVER
--------------------------------------------
''')
