from Adventure import Room, Inventory, DarkRoom, Flashlight, Item, Food, SecurityGuard, Knife, Tazer

entrance = Room('Entrance', 'You are at the entrance of Westfield Plaza Bonita. Be careful its dark!', 'k')
centercourt = Room('Center Court', 'You are at the center of Westfield Plaza Bonita.', 'h')
footlocker = DarkRoom('Foot Locker', 'You are at Foot Locker.', 'd')
nyxstore = DarkRoom('Nyx Store', 'You are at the NYX Store.', 'uh')
hollister = DarkRoom('Hollister', 'You are at Hollister.', 'b1')
pinkstore = DarkRoom('PINK Store', 'You are at the PINK Store.', 'b2')
secondcourt = DarkRoom('Second Court', 'You are at the second court of Westfield Plaza Bonita.', 'b3')
arcade = DarkRoom('Arcade', 'You are at the Arcade.', 'lr')
amc = DarkRoom('AMC', 'You are inside AMC.', 'lr')
jcpenny = DarkRoom('JCPenny', 'You are at JCPenny.', 'lr')
thirdcourt = DarkRoom('Third Court', 'You are at the third court of Westfield Plaza Bonita.', 'lr')
playground = DarkRoom('Playground', 'You are at the playground.', 'lr')
jackinthebox = DarkRoom('Jack in the Box', 'You are at Jack in the Box.', 'lr')
starbucks = DarkRoom('Starbucks', 'You are at Starbucks.', 'lr')
forever21 = DarkRoom('Forever 21', 'You are at Forever 21.', 'lr')


entrance.add_connection(centercourt, "path to the Center Court", ["west", "w"])
centercourt.add_connection(entrance, "path to the entrance", ["east", "e"])
centercourt.add_connection(footlocker, "door to the Footlocker", ["west", "w"])
footlocker.add_connection(centercourt, "path to the Center Court", ["east", "e"])
centercourt.add_connection(nyxstore, "door to the NYX", ["northwest", "nw"])
nyxstore.add_connection(centercourt, "path to the Center Court", ["southeast", "se"])
centercourt.add_connection(hollister, "door to Hollister", ["northeast", "ne"])
hollister.add_connection(centercourt, "path to Center Court", ["southwest", "sw"])
centercourt.add_connection(secondcourt, "path to the Second Court", ["south", "s"])
secondcourt.add_connection(centercourt, "path to the Center Court ", ["north", "n"])
secondcourt.add_connection(arcade, "door to the arcade", ["east", "e"])
arcade.add_connection(secondcourt, "path to Second Door ", ["west", "w"])
secondcourt.add_connection(amc, "door to the AMC", ["west", "w"])
amc.add_connection(secondcourt, "path to the Second Court", ["east", "e"])
secondcourt.add_connection(jcpenny, "door to JCPenny", ["south", "s"])
jcpenny.add_connection(secondcourt, "path to the Second Court", ["north", "n"])
jcpenny.add_connection(playground, "path to the playround", ["west", "w"])
playground.add_connection(jcpenny, "door to JCPenny", ["east", "e"])
centercourt.add_connection(thirdcourt, "path to the Third Court", ["north", "n"])
thirdcourt.add_connection(centercourt, "path to the Center Court", ["south", "s"])
thirdcourt.add_connection(jackinthebox, "door to Jack in the Box", ["northwest", "nw"])
jackinthebox.add_connection(thirdcourt, "path to the Third Court", ["southeast", "se"])
thirdcourt.add_connection(starbucks, "door to Starbucks", ["north", "n"])
starbucks.add_connection(thirdcourt, "path to the Third Court", ["south", "s"])
thirdcourt.add_connection(forever21, "door to Forever 21", ["northeast", "ne"])
forever21.add_connection(thirdcourt, "path to the Third Court", ["southwest", "sw"])


centercourt.add_item(Flashlight())
amc.add_item(Tazer("tazer"))
hollister.add_item(Knife("knife"))
jackinthebox.add_item(Food("croissant"))
jcpenny.add_item(Item("perfume"))
guards= [SecurityGuard("Security Guard #1"), SecurityGuard("Security Guard #2")]
nyxstore.add_guard(guards[0])
playground.add_guard(guards[1])



#dining.add_room('s', kitchen)
#dining.add_room('n', hallway)
#hallway.add_room('s', dining)
#hallway.add_room('u', hallway2)
#hallway.add_room('e', livingroom)
#livingroom.add_room('w', hallway)
#hallway2.add_room('d', hallway)
#hallway2.add_room('n', bedroom1)
#hallway2.add_room('e', bedroom2)
#hallway2.add_room('w', bedroom3)
#bedroom1.add_room('s', hallway2)
#bedroom2.add_room('w', hallway2)
#bedroom3.add_room('e', hallway2)



inventory = Inventory()
current_room = entrance
current_room.enter_room(inventory)

while True:
    for guard in guards:
        guard.move()
    current_room.enter_room(inventory)
    command = raw_input("What would you like to do?")
    if command in ("exit", "x", "quit", "q"):
        break

    result = current_room.process_command(command, inventory)
    if isinstance(result, Room):
        current_room = result
        continue
    elif isinstance(result, str):
        print result
        continue

    result = inventory.process_command(command)
    if len(result) == 0:
        print "I don't know what you mean"

