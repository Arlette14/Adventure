from Adventure import Room, Inventory, DarkRoom, Flashlight
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
thirdcourt = Room('Third Court', 'You are at the third court of Westfield Plaza Bonita.', 'lr')
playground = DarkRoom('Playground', 'You are at the playground.', 'lr')
jackinthebox = DarkRoom('Jack in the Box', 'You are at Jack in the Box.', 'lr')
starbucks = DarkRoom('Starbucks', 'You are at Starbucks.', 'lr')
forever21 = DarkRoom('Forever 21', 'You are at Forever 21.', 'lr')


entrance.add_connection(centercourt, "passage", ["west", "w"])
centercourt.add_connection(entrance, "passage", ["east", "e"])
centercourt.add_connection(footlocker, "passage", ["west", "w"])
footlocker.add_connection(centercourt, "passage", ["east", "e"])
centercourt.add_connection(nyxstore, "passage", ["northwest", "nw"])
nyxstore.add_connection(centercourt, "passage", ["southeast", "se"])
centercourt.add_connection(hollister, "passage", ["northeast", "ne"])
hollister.add_connection(centercourt, "passage", ["southwest", "sw"])
centercourt.add_connection(secondcourt, "passage", ["south", "s"])
secondcourt.add_connection(centercourt, "passage", ["north", "n"])
secondcourt.add_connection(arcade, "passage", ["east", "e"])
arcade.add_connection(secondcourt, "passage", ["west", "w"])
secondcourt.add_connection(amc, "passage", ["west", "w"])
amc.add_connection(secondcourt, "passage", ["east", "e"])
secondcourt.add_connection(jcpenny, "passage", ["south", "s"])
jcpenny.add_connection(secondcourt, "passage", ["north", "n"])
jcpenny.add_connection(playground, "passage", ["west", "w"])
playground.add_connection(jcpenny, "passage", ["east", "e"])
centercourt.add_connection(thirdcourt, "passage", ["north", "n"])
thirdcourt.add_connection(centercourt, "passage", ["south", "s"])
thirdcourt.add_connection(jackinthebox, "passage", ["northwest", "nw"])
jackinthebox.add_connection(thirdcourt, "passage", ["southeast", "se"])
thirdcourt.add_connection(starbucks, "passage", ["north", "n"])
starbucks.add_connection(thirdcourt, "passage", ["south", "s"])
thirdcourt.add_connection(forever21, "passage", ["northeast", "ne"])
forever21.add_connection(thirdcourt, "passage", ["southwest", "sw"])

centercourt.add_item(Flashlight())





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





