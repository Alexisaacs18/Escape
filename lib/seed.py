import os
import sys
from models.room import Room
from models.connect import CURSOR, CONN
from models.display import Display
from models.inspectable import Inspectable
from models.item import Item


##### Room seeds ######
Room.drop_table()
Room.create_table()

kitchen_description = """ You wake up, dazed and confused to find that you are in a mysterious, unknown kitchen that hasn't been used in a few years. You see a SINK with a pile of dirty dishes, some CABINETS with most of the cabinet doors barely hanging by the hinges, a TRASH CAN that is in bad need of being taken out, and a door with a square-shaped pad-lock that is locked. To escape, you will need to inspect each of these to find the clue that unlocks the door. What would you like to inspect first?"""
kitchen = Room("Kitchen", True, kitchen_description)
# kitchen.add_to_table()

dining_room_description = """ You enter the next room which is a run down version of what used to be a nice looking dining room. You see a TABLE with a bunch of clutter on it, some CHAIRS, a busted in CHINA CABINET, and a BAR CART. There is also a door with a lock with a symbol of a circle on it. Find the key for this lock!"""
dining_room = Room("Dining Room", False, dining_room_description)

bedroom_description = """You now enter the bedroom. You notice that there is a broken BED against the far wall, a CLOSET with the doors torn off, a DESK with a mess of papers scattered everywhere and a door with a giant triangle shaped lock. You also notice that the door has been barred off with wooden PLANKS, preventing anyone from accessing the door. This must be the way out!"""
bedroom = Room("Bedroom", True, bedroom_description)
# bedroom.add_to_table()


##### Inspectable seeds ######
Inspectable.drop_table()
Inspectable.create_table()

sink_description = """ You look inside the sink and find a key with a square shaped end."""
sink = Inspectable("Sink", kitchen, False, sink_description)

cabinet_description = """You check the cabinets but you don't find any clues or items that will help you unlock the door."""
cabinet = Inspectable("Cabinet", kitchen, False, cabinet_description)

trash_can_description = """You search through the trash can and find a crowbar. Maybe this will help you in your journey."""
trash_can = Inspectable("Trash Can", kitchen, False, trash_can_description)

square_lock_description = """You approch the square shaped lock. Do you want to use your key?"""
square_lock = Inspectable("Square Lock", kitchen, False, square_lock_description)

table_description = """You search the table in the middle of the room but do not find any clues."""
table = Inspectable("Table", dining_room, False, table_description)

chairs_description = """You look on each chair and do not find any clues or items."""
chairs = Inspectable("Chairs", dining_room, False, chairs_description)

china_cabinet_description = """You search through the China cabinet to find nothing more than broken dishes."""
china_cabinet = Inspectable("China Cabinet", dining_room, False, china_cabinet_description)

bar_cart_description = """You search through the bottles and glassware and find a key inside a decanter. Upon opening the decanter and retrieving the key, you notice that it has a circle symbol on it. This must be for the lock on the door!"""
bar_cart = Inspectable("Bar Cart", dining_room, False, bar_cart_description)

circle_lock_description = """You approach the door with the circle symbol. Do you want to use the key that you found?"""
circle_lock = Inspectable("Circle Lock", dining_room, False, circle_lock_description)

bed_description = """You pull the blankets off the bed but do not find any usefull clues."""
bed = Inspectable("Bed", bedroom, False, bed_description)

closet_description = """You make your way to the closet and search through the tattered clothes. You find an old baseball bat that you might could use."""
closet = Inspectable("Closet", bedroom, False, closet_description)

desk_description = """You search through the papers on the desk but don't find anything you can use. You open a drawer and find a key with the triangle symbol! You are almost free!"""
desk = Inspectable("Desk", bedroom, False, desk_description)

planks_description = """You run to the door with with the triangle shaped key in excitment about getting out but you remember you need to get through the planks. What do you use to get through these?"""
planks = Inspectable("Planks", bedroom, False, planks_description)

triangle_lock_description = """You finally get through the planks and are now at the triangle shaped lock! Would you like to use the key?"""
triangle_lock = Inspectable("Triangle Lock", bedroom, False, triangle_lock_description)

###### Item seeds ######
Item.drop_table()
Item.create_table()

square_key_description = """You have a key with a square shaped end that fits to a specific lock"""
square_key = Item("Square Key", sink, square_key_description)